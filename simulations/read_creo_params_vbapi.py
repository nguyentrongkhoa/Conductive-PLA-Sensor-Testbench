"""
Read and change the parameters of the Creo parts/assemblies in the sibling ``cad``
folder using the Creo Parametric VB API (pfcls COM, asynchronous connection).

Requirements
------------
* Windows, Creo Parametric already running.
* pip install pywin32   (64-bit Python to match 64-bit Creo)
* The VB API COM library registered once (admin prompt), e.g.:
      regsvr32 "C:\\Program Files\\PTC\\Creo 13.4.0.0\\Common Files\\x86e_win64\\obj\\pfcls.dll"
  If that file does not exist, the VB API feature is not installed with Creo.

Usage
-----
  python read_creo_params_vbapi.py                          # list all .prt/.asm in ../cad
  python read_creo_params_vbapi.py list fp_121_dms_substrat.prt
  python read_creo_params_vbapi.py set  fp_121_dms_substrat.prt THICKNESS 0.4
  python read_creo_params_vbapi.py set  fp_121_dms_substrat.prt NOTE_TXT hello --type STRING
  python read_creo_params_vbapi.py set  ... --save          # regenerate + save afterwards
"""

import argparse
import json
import sys
from pathlib import Path

import win32com.client as win32

# pfcls ParamValueType enum: STRING=0, INTEGER=1, BOOLEAN=2, DOUBLE=3, NOTE=4
TYPE_NAMES = {0: "STRING", 1: "INTEGER", 2: "BOOL", 3: "DOUBLE", 4: "NOTE"}
TYPES = ("STRING", "INTEGER", "BOOL", "DOUBLE")


# --------------------------------------------------------------------------- #
# COM helpers
# --------------------------------------------------------------------------- #
def dispatch(name):
    """Create a pfcls COM object; progid is pfcls.pfcX / pfcls.CCpfcX / pfcls.MpfcX."""
    last = None
    for progid in (f"pfcls.pfc{name}", f"pfcls.CCpfc{name}", f"pfcls.Mpfc{name}"):
        try:
            return win32.Dispatch(progid)
        except Exception as exc:  # noqa: BLE001
            last = exc
    raise RuntimeError(f"Could not create COM object for '{name}': {last}")


def seq(com_seq):
    """Yield the items of a pfcls sequence (0-based Count/Item)."""
    if com_seq is None:
        return
    for i in range(com_seq.Count):
        yield com_seq.Item(i)


def value_of(pv):
    """Return (type_name, python_value) for a pfcls ParamValue."""
    t = int(pv.discr)
    name = TYPE_NAMES.get(t, str(t))
    val = {0: lambda: pv.StringValue, 1: lambda: pv.IntValue,
           2: lambda: bool(pv.BoolValue), 3: lambda: pv.DoubleValue,
           4: lambda: pv.NoteId}.get(t, lambda: None)()
    return name, val


def make_value(type_, value):
    """Build a pfcls ParamValue of the given type from a text value."""
    mi = dispatch("ModelItem")
    if type_ == "DOUBLE":
        return mi.CreateDoubleParamValue(float(value))
    if type_ == "INTEGER":
        return mi.CreateIntParamValue(int(value))
    if type_ == "BOOL":
        return mi.CreateBoolParamValue(str(value).strip().lower() in ("1", "true", "yes", "y"))
    return mi.CreateStringParamValue(str(value))


def guess_type(value):
    if value.strip().lower() in ("true", "false", "yes", "no"):
        return "BOOL"
    for cast, name in ((int, "INTEGER"), (float, "DOUBLE")):
        try:
            cast(value)
            return name
        except ValueError:
            pass
    return "STRING"


# --------------------------------------------------------------------------- #
# Creo access
# --------------------------------------------------------------------------- #
def connect():
    conn = dispatch("AsyncConnection").Connect(None, None, None, None)
    return conn, conn.Session


def retrieve(session, filename):
    descr = dispatch("ModelDescriptor").CreateFromFilename(filename)
    try:
        opts = dispatch("RetrieveModelOptions").Create()
        opts.AskUserAboutReps = False
        return session.RetrieveModelWithOpts(descr, opts)
    except Exception:  # noqa: BLE001
        return session.RetrieveModel(descr)


def read_params(model):
    out = []
    for p in seq(model.ListParams()):
        entry = {"name": p.ID}
        try:
            entry["type"], entry["value"] = value_of(p.Value)
        except Exception as exc:  # noqa: BLE001
            entry["type"], entry["value"] = "?", f"<unreadable: {exc}>"
        try:
            entry["designated"] = bool(p.IsDesignated)
        except Exception:  # noqa: BLE001
            pass
        try:
            entry["units"] = p.Units.Name if p.Units is not None else ""
        except Exception:  # noqa: BLE001
            entry["units"] = ""
        out.append(entry)
    return out


def print_params(filename, params):
    print("\n" + "=" * 78)
    print(filename)
    print("=" * 78)
    if not params:
        print("  (no parameters)")
        return
    w = max(len(p["name"]) for p in params)
    for p in params:
        unit = f" {p['units']}" if p.get("units") else ""
        print(f"  {p['name']:<{w}}  [{p['type']:<7}]  {p['value']}{unit}")


def set_param(session, filename, name, value, type_=None, save=False):
    model = retrieve(session, filename)
    old = model.GetParam(name)          # None if it does not exist yet

    if old is not None:
        old_type, old_val = value_of(old.Value)
        type_ = (type_ or old_type).upper()
        old.Value = make_value(type_, value)
        shown_old = old_val
    else:
        type_ = (type_ or guess_type(value)).upper()
        model.CreateParam(name, make_value(type_, value))
        shown_old = "<new parameter>"
    print(f"{filename}: {name} [{type_}]  {shown_old}  ->  {value}")

    if save:
        model.Regenerate(None)
        model.Save()
        print(f"{filename}: regenerated and saved")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main():
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description="Read/set Creo parameters via the VB API.")
    ap.add_argument("--cad", type=Path, default=here.parent / "cad")
    ap.add_argument("--json", type=Path, default=here / "creo_params.json")
    sub = ap.add_subparsers(dest="cmd")

    p_list = sub.add_parser("list")
    p_list.add_argument("files", nargs="*")

    p_set = sub.add_parser("set")
    p_set.add_argument("file")
    p_set.add_argument("name")
    p_set.add_argument("value")
    p_set.add_argument("--type", choices=TYPES)
    p_set.add_argument("--save", action="store_true")

    args = ap.parse_args()
    cad = args.cad.resolve()
    if not cad.is_dir():
        sys.exit(f"CAD folder not found: {cad}")

    try:
        conn, session = connect()
    except Exception as exc:  # noqa: BLE001
        sys.exit(f"Could not connect to Creo (running? pfcls.dll registered?): {exc}")

    try:
        session.ChangeDirectory(str(cad))   # so assemblies find their components

        if args.cmd == "set":
            set_param(session, args.file, args.name, args.value,
                      type_=args.type, save=args.save)
            return

        files = getattr(args, "files", None) or [
            f.name for f in sorted(list(cad.glob("*.prt")) + list(cad.glob("*.asm")),
                                   key=lambda f: f.name.lower())]
        result = {}
        for name in files:
            try:
                params = read_params(retrieve(session, name))
            except Exception as exc:  # noqa: BLE001
                print(f"\n{name}\n  ! could not read: {exc}")
                result[name] = {"error": str(exc)}
                continue
            print_params(name, params)
            result[name] = params
        args.json.write_text(json.dumps(result, indent=2, ensure_ascii=False),
                             encoding="utf-8")
        print(f"\nSaved to {args.json}")
    finally:
        try:
            conn.Disconnect(2)   # leaves Creo running
        except Exception:  # noqa: BLE001
            pass


if __name__ == "__main__":
    main()

"""
Read (and optionally change) the parameters of the Creo parts/assemblies in the
sibling ``cad`` folder, using CREOSON + creopyson.

Setup (once)
------------
1. pip install creopyson
2. Download CREOSON (github.com/SimplifiedLogic/creoson), unzip it and run
   CreosonServerWithSetup.exe (it listens on http://localhost:9056 by default).
   The first run asks for the Creo start command; afterwards CREOSON can attach to
   a running Creo session (or start one).
3. Have Creo Parametric running.

Usage
-----
  python read_creo_params.py                       # list params of every .prt/.asm in ../cad
  python read_creo_params.py list fp_121_dms_substrat.prt
  python read_creo_params.py set  fp_121_dms_substrat.prt THICKNESS 0.4
  python read_creo_params.py set  fp_121_dms_substrat.prt MATERIAL_NAME cPLA --type STRING
  python read_creo_params.py set  ... --save       # regenerate + save the model afterwards

Common options: --cad <folder>  --host <host> --port <port>  --json <file>
"""

import argparse
import json
import sys
from pathlib import Path

import creopyson

TYPES = ("STRING", "DOUBLE", "INTEGER", "BOOL", "NOTE")


# --------------------------------------------------------------------------- #
# Reading
# --------------------------------------------------------------------------- #
def read_params(client, filename):
    """Open the model (kept in session) and return its parameter dicts."""
    client.file_open(filename, display=True, activate=True)
    return client.parameter_list(file_=filename)


def print_params(filename, params):
    print("\n" + "=" * 78)
    print(filename)
    print("=" * 78)
    if not params:
        print("  (no parameters)")
        return
    width = max(len(str(p.get("name", ""))) for p in params)
    for p in params:
        flag = " (designated)" if p.get("designate") else ""
        print(f"  {str(p.get('name')):<{width}}  [{str(p.get('type')):<7}]  {p.get('value')}{flag}")


# --------------------------------------------------------------------------- #
# Writing
# --------------------------------------------------------------------------- #
def cast(value, type_):
    if type_ == "DOUBLE":
        return float(value)
    if type_ == "INTEGER":
        return int(value)
    if type_ == "BOOL":
        return str(value).strip().lower() in ("1", "true", "yes", "y")
    return str(value)


def guess_type(value):
    v = value.strip().lower()
    if v in ("true", "false", "yes", "no"):
        return "BOOL"
    try:
        int(value)
        return "INTEGER"
    except ValueError:
        pass
    try:
        float(value)
        return "DOUBLE"
    except ValueError:
        return "STRING"


def set_param(client, filename, name, value, type_=None, save=False):
    client.file_open(filename, display=True, activate=True)
    existing = {p["name"].upper(): p for p in client.parameter_list(file_=filename)}
    old = existing.get(name.upper())

    # prefer: explicit --type > type of the existing param > guess from the text
    type_ = (type_ or (old or {}).get("type") or guess_type(value)).upper()
    new_value = cast(value, type_)

    client.parameter_set(name, new_value, file_=filename, type_=type_)
    shown_old = old.get("value") if old else "<new parameter>"
    print(f"{filename}: {name} [{type_}]  {shown_old}  ->  {new_value}")

    if save:
        client.file_regenerate(filename)
        client.file_save(filename)
        print(f"{filename}: regenerated and saved")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main():
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description="Read/set Creo parameters via CREOSON.")
    ap.add_argument("--cad", type=Path, default=here.parent / "cad",
                    help="folder with the .prt/.asm files (default: ../cad)")
    ap.add_argument("--host", default="localhost")
    ap.add_argument("--port", type=int, default=9056)
    ap.add_argument("--json", type=Path, default=here / "creo_params.json",
                    help="where 'list' saves its result")
    sub = ap.add_subparsers(dest="cmd")

    p_list = sub.add_parser("list", help="print parameters (default: all files in cad)")
    p_list.add_argument("files", nargs="*", help="file names inside the cad folder")

    p_set = sub.add_parser("set", help="set or create a parameter")
    p_set.add_argument("file")
    p_set.add_argument("name")
    p_set.add_argument("value")
    p_set.add_argument("--type", choices=TYPES, help="force the Creo parameter type")
    p_set.add_argument("--save", action="store_true", help="regenerate and save afterwards")

    args = ap.parse_args()
    cmd = args.cmd or "list"
    cad = args.cad.resolve()
    if not cad.is_dir():
        sys.exit(f"CAD folder not found: {cad}")

    client = creopyson.Client(ip_adress=args.host, port=args.port)
    try:
        client.connect()
    except Exception as exc:  # noqa: BLE001
        sys.exit(f"Could not reach the CREOSON server on {args.host}:{args.port}: {exc}")

    try:
        client.creo_cd(str(cad))   # so assemblies find their components

        if cmd == "set":
            set_param(client, args.file, args.name, args.value,
                      type_=args.type, save=args.save)
            return

        files = getattr(args, "files", None) or [
            f.name for f in sorted(list(cad.glob("*.prt")) + list(cad.glob("*.asm")),
                                   key=lambda f: f.name.lower())]
        result = {}
        for name in files:
            try:
                params = read_params(client, name)
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
            client.disconnect()
        except Exception:  # noqa: BLE001
            pass


if __name__ == "__main__":
    main()

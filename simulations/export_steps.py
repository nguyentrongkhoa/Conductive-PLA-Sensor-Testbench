"""
Read the DoE Excel file line by line, set the parameters in Creo (via creo_api.py /
CREOSON), regenerate the model and export the sensor assembly as a STEP file
named sensor_1.stp, sensor_2.stp, ...

The number comes from the line in the Excel file: the first data line (Excel row 2,
just below the header) becomes sensor_1. Use --excel-row-numbers if you want the raw
Excel row number instead (first data line = sensor_2).

Before running: CREOSON server running (localhost:9056) and Creo started, see creo_api.py.

Usage
-----
    python export_steps.py                          # every row of doe_params.xlsx
    python export_steps.py --start 3 --end 5        # only sensors 3 to 5
    python export_steps.py --out C:\\temp\\steps    # other output folder
    python export_steps.py --overwrite              # re-export existing STEP files

The parameters are set in every Creo model of the cad folder that has a parameter of
that name. Parameters missing in all models (maybe H_LAYER, N_LAYER) are skipped with
a warning. The model files are NOT saved. After each sensor the models are erased from
the Creo session (use --no-erase to keep them), so every sensor starts from the files on
disk, and the cad files stay unchanged.

Regeneration order: changed parts, then sub-assemblies (e.g. fp_120), then the top
assembly. If a sensor fails, the error is printed and the script goes on with the next.
"""

import argparse
import shutil
import sys
from pathlib import Path

import creopyson
from openpyxl import load_workbook

import creo_api
from generate_params_clean import PARAM_COLS

HERE = Path(__file__).resolve().parent
ASSEMBLY = "fp_100_sensor_asm.asm"     # top-level assembly that is exported
_ERASE_WARNED = []

# Values derived from the sheet; only set if a Creo model has a parameter of that name.
# Grid thickness = number of layers * layer height (constraint 4 in the notes).
DERIVED = {
    "T_G": lambda p: round(p["N_LAYER"] * p["H_LAYER"], 4),
}


# --------------------------------------------------------------------------- #
# Excel
# --------------------------------------------------------------------------- #
def read_rows(xlsx_path):
    """Yield (excel_row, {param: value}) for every data line of the sheet."""
    ws = load_workbook(xlsx_path, read_only=True, data_only=True).active
    header = None
    for excel_row, row in enumerate(ws.iter_rows(values_only=True), start=1):
        if excel_row == 1:
            header = list(row)
            continue
        if not row or row[0] is None:
            continue                                   # empty line
        values = dict(zip(header, row))
        yield excel_row, {k: values[k] for k in PARAM_COLS if k in values}


# --------------------------------------------------------------------------- #
# Creo
# --------------------------------------------------------------------------- #
def build_param_map(client, cad_dir):
    """{PARAM_NAME_UPPER: [model files that have it]} for all .prt/.asm in cad."""
    pmap = {}
    for f in sorted(list(cad_dir.glob("*.prt")) + list(cad_dir.glob("*.asm")),
                    key=lambda f: f.name.lower()):
        for p in creo_api.read_params(client, f.name):
            pmap.setdefault(p["name"].upper(), []).append(f.name)
    return pmap


def apply_params(client, pmap, params):
    """Set all parameters of one Excel line. Returns the set of files that were changed."""
    values = dict(params)
    for name, fn in DERIVED.items():
        if name.upper() in pmap:
            values[name] = fn(params)

    touched = set()
    for name, value in values.items():
        for filename in pmap.get(name.upper(), []):
            creo_api.set_param(client, filename, name, value)   # no save
            touched.add(filename)
    return touched


def regenerate(client, touched, subassemblies):
    """Regenerate bottom-up: changed parts, then sub-assemblies, then the top assembly."""
    order = ([f for f in sorted(touched) if f.lower().endswith(".prt")]
             + sorted(subassemblies) + [ASSEMBLY])
    for filename in order:
        client.file_open(filename, display=True, activate=True)
        client.file_regenerate(filename)


def reset_session(client, cad_dir):
    """Close and erase all cad models from the Creo session WITHOUT saving, so the next
    sensor starts from the files on disk (also keeps the session from filling up)."""
    files = sorted(cad_dir.glob("*.asm")) + sorted(cad_dir.glob("*.prt"))
    for f in files:
        try:
            client.file_close_window(f.name)
        except Exception:  # noqa: BLE001 - not open / already closed
            pass
    for f in files:
        try:
            client.file_erase(file_=f.name, erase_children=True)
        except Exception as exc:  # noqa: BLE001
            if not _ERASE_WARNED:      # warn once; models not in the session also raise
                _ERASE_WARNED.append(1)
                print(f"   (erase of {f.name} reported: {exc}; further such messages hidden)")


def export_step(client, target, tmp_dir):
    """Export the assembly as STEP into a temp folder, then move it to `target`."""
    shutil.rmtree(tmp_dir, ignore_errors=True)
    tmp_dir.mkdir(parents=True)
    client.file_open(ASSEMBLY, display=True, activate=True)
    client.interface_export_file(file_type="STEP", file_=ASSEMBLY, dirname=str(tmp_dir))
    files = [f for f in tmp_dir.iterdir() if f.suffix.lower() in (".stp", ".step")] \
        or list(tmp_dir.iterdir())
    if not files:
        raise RuntimeError("Creo did not write a STEP file.")
    newest = max(files, key=lambda f: f.stat().st_mtime)
    target.unlink(missing_ok=True)
    shutil.move(str(newest), str(target))
    shutil.rmtree(tmp_dir, ignore_errors=True)


# --------------------------------------------------------------------------- #
# Main loop
# --------------------------------------------------------------------------- #
def run(xlsx_path, out_dir, cad_dir, host="localhost", port=9056, start=None, end=None,
        overwrite=False, excel_row_numbers=False, erase=True):
    out_dir.mkdir(parents=True, exist_ok=True)
    client = creopyson.Client(ip_adress=host, port=port)
    client.connect()
    results = []
    try:
        client.creo_cd(str(cad_dir))
        subassemblies = [f.name for f in cad_dir.glob("*.asm") if f.name != ASSEMBLY]
        pmap = build_param_map(client, cad_dir)
        if erase:
            reset_session(client, cad_dir)   # start from the files on disk
        missing = [c for c in PARAM_COLS if c.upper() not in pmap]
        if missing:
            print("Not found in any Creo model (skipped): " + ", ".join(missing))

        for excel_row, params in read_rows(xlsx_path):
            number = excel_row if excel_row_numbers else excel_row - 1
            if (start is not None and number < start) or (end is not None and number > end):
                continue
            target = out_dir / f"sensor_{number}.stp"
            if target.exists() and not overwrite:
                print(f"sensor_{number}: exists, skipped (use --overwrite)")
                results.append((number, "skipped"))
                continue
            print(f"\n=== sensor_{number} (Excel row {excel_row}) ===")
            try:
                touched = apply_params(client, pmap, params)
                regenerate(client, touched, subassemblies)
                export_step(client, target, out_dir / "_export_tmp")
                print(f"-> {target}")
                results.append((number, "ok"))
            except Exception as exc:  # noqa: BLE001 - keep going with the next line
                print(f"!! sensor_{number} failed: {exc}")
                results.append((number, f"FAILED: {exc}"))
            if erase:
                reset_session(client, cad_dir)
    finally:
        try:
            client.disconnect()
        except Exception:  # noqa: BLE001
            pass

    print("\nSummary:")
    for number, status in results:
        print(f"  sensor_{number}: {status}")
    return results


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Set Creo params from the DoE Excel file and export STEP files.")
    ap.add_argument("--xlsx", type=Path, default=HERE / "doe_params.xlsx")
    ap.add_argument("--out", type=Path, default=HERE / "step_files", help="output folder for the STEP files")
    ap.add_argument("--cad", type=Path, default=HERE.parent / "cad")
    ap.add_argument("--host", default="localhost")
    ap.add_argument("--port", type=int, default=9056)
    ap.add_argument("--start", type=int, help="first sensor number to process")
    ap.add_argument("--end", type=int, help="last sensor number to process")
    ap.add_argument("--overwrite", action="store_true", help="re-export existing STEP files")
    ap.add_argument("--excel-row-numbers", action="store_true",
                    help="number sensors by the raw Excel row (first data line = sensor_2)")
    ap.add_argument("--no-erase", action="store_true",
                    help="keep the models in the Creo session between sensors")
    a = ap.parse_args()
    if not a.xlsx.exists():
        sys.exit(f"Excel file not found: {a.xlsx}")
    run(a.xlsx, a.out, a.cad.resolve(), a.host, a.port, a.start, a.end,
        a.overwrite, a.excel_row_numbers, erase=not a.no_erase)

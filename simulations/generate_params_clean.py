"""
Generate random sets of the 12 strain-gauge parameters under the design
constraints, and append them to an Excel file for a DoE tool.

This is the cleaned-up version of the notes in generate_params.py
(that file is untouched).

PARAMETERS (the 12 columns)
 1. N_LEG         even integer, 4 ... 20
 2. B_GAUGE       real, 2 ... 10
 3. G_LEGS        real, 0.8 ... 2
 4. H_LAYER       0.15, 0.2, 0.3 or 0.4 mm
 5. N_LAYER       2, 3, 4 or 5
 6. L_A           real, 10 ... 50 mm
 7. L_E           real, 1 ... 10 mm
 8. L_START_LOOP  real, 1 ... 10 mm
 9. W             real, 0.8 ... 5
10. B_S           derived from constraint 2
11. L_S           derived from constraints 3 and 5
12. T_S           derived from constraint 4

CONSTRAINTS (one boolean column each)
 C1  B_S <= ANS_W_FK <= B_S + 30
       carrier at least as wide as the substrate
 C2  B_S = L_A + L_E + L_START_LOOP + 5
       substrate wider than the strain gauge height by 5 mm
 C3  L_S >= ((G_LEGS + B_GAUGE) * N_LEG) / 2 + 5
       substrate longer than the strain gauge by at least 5 mm
 C4  (N_LAYER + 1) * H_LAYER <= T_S <= (N_LAYER + 5) * H_LAYER
       substrate thicker than the strain gauge by at least 1 print layer
 C5  10 <= L_S + ANS_SUBSTRATE_OFFSET <= L_FK
       substrate lies entirely on the steel plate carrier and leaves 10 mm
       for the loading area

DEPENDENT CARRIER VALUES (two extra columns after the 12 parameters)
 ANS_W_FK = B_S + (0 ... 30)                   -> satisfies C1
 L_FK     = L_S + ANS_SUBSTRATE_OFFSET + (10 ... 30)
                                               -> satisfies C5, leaves >= 10 mm loading area
 They follow B_S and L_S instead of being fixed.

ASSUMPTIONS (please check)
 * ANS_SUBSTRATE_OFFSET is not given in the notes. It is a fixed PLACEHOLDER
   below: set your real value.
 * The extra carrier length behind the substrate (10 ... 30 mm) is my choice,
   see CARRIER_LENGTH_EXTRA.
 * C2 is used as an equality (B_S is derived), as written in the notes.
 * C4 in the notes reads ">= (N_LAYER+5)*H_LAYER"; I read that as an upper
   bound (<=). T_S is drawn as a whole number of layers within that window.

USAGE
    python generate_params_clean.py 20              # append 20 valid sets to doe_params.xlsx
    python generate_params_clean.py 20 --seed 1     # reproducible
    python generate_params_clean.py 20 --all        # keep sets that violate constraints too
    python generate_params_clean.py 20 --out my.xlsx

Requires: pip install openpyxl. Column R (resistance) is left empty for the
simulation results.
"""

import argparse
import random
from pathlib import Path

from openpyxl import Workbook, load_workbook

# --------------------------------------------------------------------------- #
# Fixed value (NOT in the notes -> PLACEHOLDER, set your real value)
# --------------------------------------------------------------------------- #
ANS_SUBSTRATE_OFFSET = 0.0   # position of the substrate on the carrier, mm

# Carrier size relative to the substrate (min, max) in mm
CARRIER_WIDTH_EXTRA = (0.0, 30.0)    # ANS_W_FK = B_S + extra       (constraint 1)
CARRIER_LENGTH_EXTRA = (10.0, 30.0)  # L_FK = L_S + offset + extra  (constraint 5, >= 10 mm loading area)

EPS = 1e-6
H_LAYER_CHOICES = (0.15, 0.2, 0.3, 0.4)
N_LAYER_CHOICES = (2, 3, 4, 5)

# --------------------------------------------------------------------------- #
# Constraints: name -> function(p) -> bool   (each becomes a boolean column)
# --------------------------------------------------------------------------- #
CONSTRAINTS = {
    "C1_carrier_wider_than_substrate":
        lambda p: p["B_S"] - EPS <= p["ANS_W_FK"] <= p["B_S"] + 30 + EPS,
    "C2_substrate_wider_than_gauge":
        lambda p: abs(p["B_S"] - (p["L_A"] + p["L_E"] + p["L_START_LOOP"] + 5)) < EPS,
    "C3_substrate_longer_than_gauge":
        lambda p: p["L_S"] >= ((p["G_LEGS"] + p["B_GAUGE"]) * p["N_LEG"]) / 2 + 5 - EPS,
    "C4_substrate_thicker_than_gauge":
        lambda p: ((p["N_LAYER"] + 1) * p["H_LAYER"] - EPS <= p["T_S"]
                   <= (p["N_LAYER"] + 5) * p["H_LAYER"] + EPS),
    "C5_substrate_on_carrier":
        lambda p: 10 - EPS <= p["L_S"] + ANS_SUBSTRATE_OFFSET <= p["L_FK"] + EPS,
}

# 12 parameters + the two carrier values that depend on B_S and L_S
PARAM_COLS = ["N_LEG", "B_GAUGE", "G_LEGS", "H_LAYER", "N_LAYER", "L_A",
              "L_E", "L_START_LOOP", "W", "B_S", "L_S", "T_S", "ANS_W_FK", "L_FK"]
CONSTRAINT_COLS = list(CONSTRAINTS)
RESULT_COL = "R"
HEADER = PARAM_COLS + CONSTRAINT_COLS + [RESULT_COL]


def check_constraints(p):
    """Return {constraint_name: bool} for a parameter set."""
    return {name: bool(fn(p)) for name, fn in CONSTRAINTS.items()}


# --------------------------------------------------------------------------- #
# 1) one set of parameters
# --------------------------------------------------------------------------- #
def _uniform(rng, lo, hi):
    return round(rng.uniform(lo, hi), 2)


def _draw_valid(rng):
    """One draw that satisfies C2, C3, C4, C5 by construction (C1 checked after)."""
    p = {
        "N_LEG": rng.randrange(4, 21, 2),
        "B_GAUGE": _uniform(rng, 2, 10),
        "G_LEGS": _uniform(rng, 0.8, 2),
        "H_LAYER": rng.choice(H_LAYER_CHOICES),
        "N_LAYER": rng.choice(N_LAYER_CHOICES),
        "L_A": _uniform(rng, 10, 50),
        "L_E": _uniform(rng, 1, 10),
        "L_START_LOOP": _uniform(rng, 1, 10),
        "W": _uniform(rng, 0.8, 5),
    }
    p["B_S"] = round(p["L_A"] + p["L_E"] + p["L_START_LOOP"] + 5, 2)            # C2
    layers = rng.randint(p["N_LAYER"] + 1, p["N_LAYER"] + 5)                    # C4
    p["T_S"] = round(layers * p["H_LAYER"], 3)
    lo = max(((p["G_LEGS"] + p["B_GAUGE"]) * p["N_LEG"]) / 2 + 5,               # C3
             10 - ANS_SUBSTRATE_OFFSET)                                         # C5
    p["L_S"] = round(rng.uniform(lo, lo + 60), 2)   # C3, C5 (the +60 mm range is my choice)
    p["ANS_W_FK"] = round(p["B_S"] + rng.uniform(*CARRIER_WIDTH_EXTRA), 2)      # C1
    p["L_FK"] = round(p["L_S"] + ANS_SUBSTRATE_OFFSET
                      + rng.uniform(*CARRIER_LENGTH_EXTRA), 2)                  # C5
    return p


def _draw_any(rng):
    """Draw with B_S, L_S, T_S sampled freely, so constraints can be violated."""
    p = _draw_valid(rng) or {}
    if not p:
        p = {"N_LEG": rng.randrange(4, 21, 2), "B_GAUGE": _uniform(rng, 2, 10),
             "G_LEGS": _uniform(rng, 0.8, 2), "H_LAYER": rng.choice(H_LAYER_CHOICES),
             "N_LAYER": rng.choice(N_LAYER_CHOICES), "L_A": _uniform(rng, 10, 50),
             "L_E": _uniform(rng, 1, 10), "L_START_LOOP": _uniform(rng, 1, 10),
             "W": _uniform(rng, 0.8, 5)}
    p["B_S"] = _uniform(rng, 5, 90)
    p["L_S"] = _uniform(rng, 5, 200)
    p["T_S"] = round(rng.uniform(0.1, 3.0), 3)
    p["ANS_W_FK"] = _uniform(rng, 5, 120)
    p["L_FK"] = _uniform(rng, 20, 250)
    return p


def generate_params(rng=None, valid_only=True, max_tries=100_000):
    """Draw one set of the 12 parameters.

    valid_only=True  -> returns a set that satisfies ALL constraints.
    valid_only=False -> B_S, L_S and T_S are drawn freely, so constraints may fail.

    Returns (params, flags): the parameter values and one boolean per constraint.
    """
    rng = rng or random.Random()
    for _ in range(max_tries):
        p = _draw_valid(rng) if valid_only else _draw_any(rng)
        if p is None:
            continue
        flags = check_constraints(p)
        if not valid_only or all(flags.values()):
            return p, flags
    raise RuntimeError("No valid parameter set found: check the constraints and "
                       "ANS_SUBSTRATE_OFFSET.")


# --------------------------------------------------------------------------- #
# 2) n sets -> Excel
# --------------------------------------------------------------------------- #
def append_sets_to_excel(n, path=None, seed=None, valid_only=True):
    """Generate n parameter sets and append them to an .xlsx file (created if missing).

    Columns: 12 parameters | one boolean column per constraint | R (empty).
    Sets already present in the file are skipped (no duplicates).
    Returns the number of rows appended.
    """
    path = Path(path) if path else Path(__file__).resolve().parent / "doe_params.xlsx"
    rng = random.Random(seed)

    if path.exists():
        wb = load_workbook(path)
        ws = wb.active
        header = [c.value for c in ws[1]]
        if header != HEADER:
            raise ValueError(f"{path.name} has a different header than expected:\n{header}")
        seen = {tuple(c.value for c in row[:len(PARAM_COLS)])
                for row in ws.iter_rows(min_row=2)}
    else:
        wb = Workbook()
        ws = wb.active
        ws.title = "DoE"
        ws.append(HEADER)
        seen = set()

    added, attempts = 0, 0
    while added < n:
        attempts += 1
        if attempts > 100 * n + 1000:
            raise RuntimeError("Could not find enough distinct parameter sets.")
        params, flags = generate_params(rng, valid_only=valid_only)
        key = tuple(params[c] for c in PARAM_COLS)
        if key in seen:
            continue
        seen.add(key)
        ws.append([params[c] for c in PARAM_COLS]
                  + [flags[c] for c in CONSTRAINT_COLS]
                  + [None])
        added += 1

    ws.freeze_panes = "A2"
    for i, name in enumerate(HEADER, start=1):
        ws.column_dimensions[ws.cell(row=1, column=i).column_letter].width = max(8, len(name) + 2)
    wb.save(path)
    return added


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Append random strain-gauge parameter sets to an Excel file.")
    ap.add_argument("n", type=int, help="number of sets to generate")
    ap.add_argument("--out", type=Path, default=None,
                    help="xlsx file (default: doe_params.xlsx next to this script)")
    ap.add_argument("--seed", type=int, default=None, help="random seed for reproducible sets")
    ap.add_argument("--all", action="store_true",
                    help="keep sets that violate constraints (booleans show which)")
    a = ap.parse_args()
    k = append_sets_to_excel(a.n, a.out, a.seed, valid_only=not a.all)
    print(f"Appended {k} rows to {a.out or 'doe_params.xlsx'}")

---
topic: Test plan and design of experiments
date: 2026-11-17
tags:
  - forschungsprojekt
  - versuche
  - doe
---
# Versuchsplanung
Back to [[Home]] · Geometry parameters: [[Implementation]] · Print parameters: [[Druckparameter]]

## Responses (what we measure per sensor)
| Response | How | Target (requirement) |
|---|---|---|
| R0 | 4-wire, room temperature, before bonding | scatter of a batch ≤ ±5 % (for bridge matching) |
| Gauge factor k / sensitivity | ΔR/R0 vs. strain or force | as high as possible |
| Linearity error | best-fit line, % FS | 3–5 % FS (4.3) |
| Hysteresis | max. difference loading/unloading, % FS | 5–10 % FS (4.4) |
| Creep/drift | ΔR during 30 s / 5 min hold at constant force | small (4.5) |
| Repeatability | spread over 4 cycles and over the 5 identical sensors | – |
| Zero after unloading | ΔR0 after cycle | permanent deformation ≤ 1 % (4.2) |
| Temperature drift | unloaded sensor, log DS18B20 | – |

## Load protocol (based on Chadda et al.)
1. Clamp, wait until R and temperature are stable.
2. **3 settling cycles** 0 → 100 N → 0.
3. Load in ≥ **5 steps** (requirement 11.1), e.g. 0/20/40/60/80/100 N, with a constant force rate (Chadda: 0.2 N/s) and a **30 s hold** at each step and at the top.
4. Unload with the same rate and steps (→ hysteresis).
5. Repeat 4×.
6. Same in compression (must 1.6) and in tension (wish 1.7).
7. Log: time, force (HX711 reference), displacement (dial gauge), bridge signal, temperature.

## Factors
**Geometry (Creo parameters):**
| Factor | Levels | Literature hint |
|---|---|---|
| Strand/leg width `W` | 0.8 / 1.2 mm | almost no effect on errors (Gooding) |
| Number of legs / end loops `N_LEG` | 2 / 4 / 6 | more loops → less hysteresis, less sensitivity (Gooding) |
| Active gauge length `L_A` | 6 / 10 / 14 mm | Chadda 6 mm |
| Grid thickness `T_G` | 0.3 / 0.45 mm | thicker → all errors up (Gooding) |
| Distance grid ↔ clamp | 10 / 15 / 20 mm | Chadda: ≥ 10 mm from clamp |
| Bonded vs. embedded | 2 variants | [[Implementation#6. Variant B – co-printed]] |

**Printing:**
| Factor | Levels | Literature hint |
|---|---|---|
| Nozzle temperature Protopasta | 225 / 250 °C | Stano: 250 °C best |
| Ironing | off / on | Stano: −48 % resistance |
| Infill overlap | 0 / 0.2 mm | Stano |
| Nozzle size | 0.4 / 0.6 mm | Gooding used 0.6 (inconsistent extrusion) |
| Bed temperature | 60 °C fixed | |

## Plan
- Time is short (demo 17.12.) → **screening first**: 2^(k−p) fractional factorial or a 2³ full factorial on the 3 most important factors (suggestion: `T_G`, `N_LEG`, nozzle temperature), with the v1 design as the centre point.
- Each design point: **≥ 5 identical sensors** (requirement 10.3) → enough for mean ± standard deviation.
- Analyse effects with a Pareto chart / ANOVA (like Gooding with Minitab; Python `statsmodels` works too).
- Optional: compare a **second conductive filament** (other brand or conductive TPU) with the v1 design using a two-sample **t-test** on k and hysteresis.

## Print log
Use one row per printed sensor (requirement 10.2 + 11.2):

| ID | Date | Design (W/N_LEG/L_A/T_G) | Variant | Nozzle °C | Bed °C | Layer | Speed | Ironing | R0 [kΩ] | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| DMS-001 | | 0.8/4/10/0.3 | bonded | 225 | 60 | 0.15 | | off | | |

## Test report template (requirement 11.2)
Date · operator · sensor ID · setup photo · amplifier settings · load protocol · temperature · raw data file name · results (k, linearity, hysteresis, creep) · remarks.



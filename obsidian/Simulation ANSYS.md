---
topic: FEM in ANSYS, parametric sweep from Creo
date: 2026-11-17
tags:
  - forschungsprojekt
  - simulation
  - ansys
---
# Simulation in ANSYS
Back to [[Home]] · Geometry: [[Implementation]] · Success criterion E1: FEM results match the defined forces and deformations ([[Projektauftrag]])

## What to simulate
1. **Structural:** strain field in the gauge section at 0–100 N (tension and compression), buckling check (eigenvalue buckling) for compression, stress at the transition radii.
2. **Electrical conduction:** R0 of the grid from ρ (R = V/I with a voltage on pad 1, ground on pad 2).
3. **Coupled:** ΔR from the deformed geometry (geometric part of k). The ANSYS help page saved earlier describes coupled-field analyses incl. piezoresistivity: [Ansys guide](https://ansyshelp.ansys.com/public/account/secured?returnurl=/views/secured/corp/v251/en/ans_thry/thy_coup3.html). Piezoresistive coefficients for Protopasta are not known → fit them to the measured k.

## Material input
| Material | E | ν | ρ_el | Source |
|---|---|---|---|---|
| PLA (carrier, substrate) | 3300 MPa | ≈ 0.35 (assumption) | insulator | Maurizi (E) |
| Protopasta | ≈ 3000 MPa | ≈ 0.35 | 30 Ω·cm in-plane, 115 Ω·cm out-of-plane (orthotropic) | Chadda (E), Maurizi (ρ) |
| Steel 1.4310 (Chadda reference) | 186 GPa | | | Chadda |
- The resistivity is anisotropic → use an orthotropic resistivity with the layer normal = z.
- Gooding et al.: simulated ΔR was 44 % too high because Poisson contraction was neglected → keep ν in the model.
- Hysteresis/creep: mechanical part via viscoelastic (Prony) model fitted to cyclic tests; the electrical hysteresis of the carbon network is **not** a built-in ANSYS model → model it empirically (strain from ANSYS + own resistivity law fitted to measurements, e.g. in Python post-processing).

## Model hints
- Model the DMS and adhesive layer as bonded contact to the carrier, or merge into one body for v1.
- Mesh: at least 3–4 elements across leg width and thickness; sweep/hex mesh along the legs; refine at the loops; mesh study until R changes < 1 %.
- Boundary conditions as in the stand: one grip fixed, displacement or force on the other grip (only the clamped areas).
- Named selections for `pad_in`, `pad_out`, `grip_fixed`, `grip_load` – define them by geometry rules (e.g. faces at x = min), so they survive re-imports during a sweep.

## Automated parameter sweep (design one gauge, let a script vary it)
**Route A – Workbench + Creo parameters (least code)**
- Prefix the Creo parameters with `DS_` (e.g. `DS_W`, `DS_L_A`, `DS_N_LEG`) → they appear in the Workbench Parameter Set via the Creo CAD connection.
- Outputs (R0, max strain, ΔR, buckling factor) as output parameters, sweep as design points; a Workbench journal script fills the table, updates all points and exports CSV → plot with matplotlib.
- Downside: Workbench reopens Creo for every design point (slow, needs a free Creo licence).


Before automating: regenerate the Creo model by hand at the extreme parameter values (smallest gap, most legs) – most sweep failures are regeneration errors.

## Validation
- Compare simulated strain with the analytical F/(E·A) ([[Implementation#Check at 100 N]]) and with the measured ΔR of the real sensors.
- Report the deviation; expect the measured k to be higher than the purely geometric k ≈ 2.

Add Protopasta conductive PLA as material in ANSYS:
[Young's modulus](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921296/table/tab1/)

What-if - Correlation - DoE - Response surface - Optimization - Six Sigma [Tutorial](https://www.youtube.com/watch?v=CaXvEyfy5D0)
[Analyzing thin structures in Ansys](https://www.youtube.com/watch?v=r2v3kB3C0yc)

NOTE: when installing Creo Interface for Ansys, make sure to run CAD configuration manager as admin
NOTE: changing params in Ansys also affects Creo files directly

R/R₀ = (1 + ε) / (1 − νε)²

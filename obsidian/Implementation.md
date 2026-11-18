---
topic: Sensor geometry and Creo build guide
date: 2026-11-17
tags:
  - forschungsprojekt
  - cad
  - creo
  - implementation
---
# Implementation – first sensor design (v1)
Back to [[Home]] · Related: [[Druckparameter]], [[Kontaktierung und Kleben]], [[Messschaltung]], [[Simulation ANSYS]], [[Versuchsplanung]]

> [!info] Status
> Proposal v1 from 17.11.2026, derived from the requirements and the literature. **All values are starting points** – they are Creo parameters, so the DoE can vary them later. Check the grip dimensions against the real stand before printing.

## 1. Concept
Two separate parts, like a conventional foil strain gauge (Chadda et al.), as planned in the Projektantrag ("substrate and sensor made separately"):
1. **DMS element**: thin PLA substrate + meander grid of Protopasta, printed in one job with dual extrusion.
2. **Federkörper (carrier / spring element)**: flat PLA strip (plain rectangle, no fillets) that is clamped in the Kraft-Weg-Messplatz and loaded **axially** (compression = must 1.6, tension = wish 1.7).

The DMS is bonded with EA 3430 to the middle of the carrier. **Two DMS** (front + back) are active, **two more** sit on an unloaded PLA coupon as dummies → full bridge ([[Messschaltung#Recommended setup]]).

Why axial instead of a bending beam: the existing stand pulls/pushes a flat specimen in line with the lead screw (see [[Labor]]), axial strain is uniform over the gauge section (no position sensitivity), and the same part works for tension and compression.

Variant B for the DoE: the **same grid co-printed** into the carrier surface (embedded, like Maurizi/Gooding) → compare bonded vs. embedded ([[Versuchsplanung]]).

## 2. DMS element
Red = value you type in (input parameter) · green = calculated by a relation. All figures in mm.

![[dms_1_draufsicht.png]]
*Top view to scale, with every parameter at its position.*

![[dms_2_querschnitt.png]]
*Where `B_GRID`, `Y_LEG1` and `Y_LEGN` come from, and the layer stack `T_S` / `T_G` / `DTM_GRID`.*

![[dms_3_schleifen_pads.png]]
*Why `N_LEG` must be even, how `N_FAR` / `N_NEAR` and the pattern spacing `2*P` follow, and how `PAD_Y0` is derived.*

### Parameters
| Creo parameter | Value | Meaning | Reason |
|---|---|---|---|
| `L_S` | 30 mm | substrate length | requirement 2.1 (30–50 mm), fits gauge section |
| `B_S` | 10 mm | substrate width | 1 mm margin on the 12 mm carrier |
| `T_S` | 0.3 mm | substrate thickness (2 × 0.15) | thin for good strain transfer (Chadda 0.2–0.3) |
| `N_LEG` | 4 (even!) | number of legs | both pads end up on one side; Chadda used 4 |
| `W` | 0.8 mm | leg width | = 2 lines of the 0.4 nozzle (Elgeneidy: ≥ 2× nozzle), Chadda/Maurizi 0.8 |
| `G` | 0.8 mm | gap between legs | 2 nozzle widths, no bridging |
| `L_A` | 10 mm | active grid length | gives R0 ≈ 30 kΩ; Chadda 6 mm |
| `L_E` | 1.6 mm | end-loop length (along x) | loops 2× wider than legs → low transverse sensitivity |
| `T_G` | 0.3 mm | grid thickness (2 × 0.15) | thin = less hysteresis (Gooding); 1 layer left gaps (Chadda) |
| `X0` | 12 mm | start of active grid | grid centred in the carrier, room for leads and pads |
| `W_L` | 1.6 mm | lead width | 2× leg width → low lead resistance |
| `PAD_X0` / `PAD_X1` | 1 / 7.5 mm | pad start / end in x | pad 6.5 mm long |
| `PAD_W` | 4 mm | pad width | 6.5 × 4 = **26 mm²** ≥ 25 mm² (requirement 2.3) |
| `PAD_GAP` | 1 mm | gap between pads | |

Derived (relations): `P = W + G` = 1.6 mm pitch · `B_GRID = N_LEG*W + (N_LEG-1)*G` = 5.6 mm · `Y_LEG1 = (B_S - B_GRID)/2 + W/2` = 2.6 mm.

### Feature coordinates (origin = lower-left corner of the substrate, x = load axis, z = 0 bottom of substrate)
| Feature | x from–to | y from–to | z |
|---|---|---|---|
| Substrate (PLA) | 0 – 30 | 0 – 10 | 0 – 0.3 |
| Legs 1–4 (centres y = 2.6 / 4.2 / 5.8 / 7.4) | 12.0 – 22.0 | centre ± 0.4 | 0.3 – 0.6 |
| Far loop legs 1–2 | 22.0 – 23.6 | 2.2 – 4.6 | 0.3 – 0.6 |
| Far loop legs 3–4 | 22.0 – 23.6 | 5.4 – 7.8 | 0.3 – 0.6 |
| Near loop legs 2–3 | 10.4 – 12.0 | 3.8 – 6.2 | 0.3 – 0.6 |
| Lead 1 (from leg 1) | 7.5 – 12.0 | 1.4 – 3.0 | 0.3 – 0.6 |
| Lead 2 (from leg 4) | 7.5 – 12.0 | 7.0 – 8.6 | 0.3 – 0.6 |
| Pad 1 | 1.0 – 7.5 | 0.5 – 4.5 | 0.3 – 0.6 |
| Pad 2 | 1.0 – 7.5 | 5.5 – 9.5 | 0.3 – 0.6 |
Clearances: lead ↔ near loop 0.8 mm, far loop ↔ far loop 0.8 mm, pad ↔ pad 1.0 mm. Current path: pad 1 → lead 1 → leg 1 → far loop → leg 2 → near loop → leg 3 → far loop → leg 4 → lead 2 → pad 2.

### Resistance estimate
$R = \rho\,L/A$ with leg cross-section A = 0.8 × 0.3 = 0.24 mm². Loops and leads converted to an equivalent leg length: legs 40 mm + 3 loops ≈ 2.4 mm + 2 leads ≈ 4.5 mm → **≈ 47 mm equivalent**.

| Effective resistivity | R' per mm of leg | R0 |
|---|---|---|
| 15 Ω·cm | 625 Ω/mm | **≈ 29 kΩ** |
| 30 Ω·cm (manufacturer, in-plane) | 1250 Ω/mm | **≈ 59 kΩ** |
Chadda's grid (4 × 6 mm, 0.8 × 0.3 mm) measured 18.7 kΩ, which back-calculates to an effective ρ of roughly 15 Ω·cm → expect the lower end, ~30 kΩ. The pads are wide and short, so their resistance is negligible. **Measure R0 of the first print and update the bridge resistors.**

## 3. Federkörper
The carrier (spring element) that is clamped in the stand.

![[federkoerper_1_draufsicht.png]]
*Top view to scale: `L_GRIP`, `L_GAUGE`, `L_TOT`, `B_FK`, `X_DMS`, and why the DMS origin sits at x = 23 mm.*

| Creo parameter | Value                          | Meaning                                                    |
| -------------- | ------------------------------ | ---------------------------------------------------------- |
| `L_GRIP`       | 20 mm                          | grip length (clamping zone) – **adapt to the jaws**        |
| `L_GAUGE`      | 40 mm                          | free length between the jaws                               |
| `B_FK`         | 12 mm                          | width of the whole strip – **adapt to the jaws**           |
| `T_FK`         | 3.0 mm                         | thickness (20 layers × 0.15)                               |
| `L_TOT`        | relation = **80 mm**           | total length                                               |
| `X_DMS`        | relation = 23 mm               | x position of the DMS origin                               |

Relations in FP-110 (**Tools → Relations**), plain characters only:
```
L_TOT = 2*L_GRIP + L_GAUGE
X_DMS = L_GRIP + L_GAUGE/2 - X0 - L_A/2
```
`X0` and `L_A` are the DMS parameters from FP-121 (grid start and active length); if Creo doesn't know them in the carrier part, type `17` instead of `X0 + L_A/2` or copy both as parameters.

The carrier is one rectangle: no transition radius, no `R_FIL`, `L_TR`, `B_GRIP`, `B_GAUGE`. The width stays at 12 mm, so the strain at 100 N is unchanged (about 630 µm/m). The drawback is a stress concentration at the jaw edges, but it lies 15 mm away from the grid and does not affect it.

DMS placement: centred in width and in the free length → the grid centre is at x = 40 mm = middle of `L_GAUGE`, 15 mm away from each jaw, so it sees uniform strain. Second DMS mirrored on the back face.

### Check at 100 N
E_PLA ≈ 3300 MPa (as in Maurizi et al.).
| Quantity | Formula | Value |
|---|---|---|
| Cross-section | 12 × 3 | 36 mm² |
| Stress | F/A | **2.8 MPa** (far below PLA strength, keeps creep low) |
| Strain, bare carrier | F/(E·A) | 842 µm/m |
| Strain with 2 bonded DMS (each 10 × 0.6 mm² extra) | F/(E·(A + 2·6)) | **≈ 630 µm/m** (Chadda's target range was 500–1000) |
| Buckling, both ends clamped (free length ≈ 58 mm) | 4π²EI/L², I = 27 mm⁴ | **≈ 1050 N** → safety ≈ 10 |
| Buckling, worst case pinned ends | π²EI/L² | ≈ 260 N → safety 2.6 |
| Elongation of the free length | | ≈ 0.04 mm |

### Expected signal
| k | ΔR/R0 at 100 N | ΔR on 30 kΩ | per 2 N | Full bridge (2 active) |
|---|---|---|---|---|
| 1.7 (Maurizi) | 0.11 % | 32 Ω | 0.6 Ω | 0.54 mV/V |
| 2 | 0.13 % | 38 Ω | 0.8 Ω | 0.63 mV/V |
| 8.3 (Chadda) | 0.52 % | 157 Ω | 3.1 Ω | 2.6 mV/V |

> [!warning] Displacement is tiny
> The whole carrier only stretches about **0.04 mm** at 100 N. The Käfer MD12 (0.01 mm resolution) sees just 4 steps. That is normal for a strain-gauge force sensor (the characteristic to calibrate is **force → signal**, requirement 11.1), but if the supervisor expects a meaningful **force–displacement** curve, either measure the carriage travel including stand compliance, use the FMD 12 T (0.001 mm), or switch to a softer bending-beam carrier. Clarify at the jour fixe.

## 4. Building it in Creo Parametric
### Files and numbering (Lastenheft requires a numbering system)
| No.    | File                      | Content                                      |
| ------ | ------------------------- | -------------------------------------------- |
| FP-100 | `fp_100_sensor_asm.asm`   | carrier + 2 DMS (for the drawing and ANSYS)  |
| FP-110 | `fp_110_federkoerper.prt` | carrier                                      |
| FP-120 | `fp_120_dms_asm.asm`      | DMS print assembly (export to 3MF)           |
| FP-121 | `fp_121_dms_substrat.prt` | substrate (PLA, extruder 1)                  |
| FP-122 | `fp_122_dms_gitter.prt`   | grid + leads + pads (Protopasta, extruder 2) |
| FP-130 | `fp_130_klebelehre.prt`   | bonding jig                                  |
Store in `cad/` (version control: requirement 19.1).

### Parameters and relations
1. In each part: **Tools → Parameters**, create the parameters from the tables above (type Real; `N_LEG` Integer).
2. **Tools → Relations**, e.g. in FP-122:
```
P = W + G
B_GRID = N_LEG*W + (N_LEG-1)*G
Y_LEG1 = (B_S - B_GRID)/2 + W/2
Y_LEGN = Y_LEG1 + (N_LEG-1)*P
N_FAR = floor(N_LEG/2)
N_NEAR = floor(N_LEG/2) - 1
PAD_Y0 = B_S/2 - PAD_GAP/2 - PAD_W
/* N_LEG must be even, otherwise the second pad lands on the far end */
```
3. While sketching, **rename the dimension symbols** (right-click a dimension → Properties → Name, e.g. `leg_w`) and drive them by relations (`leg_w = W`). Then the sweep script ([[Simulation ANSYS]]) only changes parameters, never sketch dimensions.
4. For ANSYS later: give the parameters you want to vary in Workbench the prefix `DS_` (e.g. `DS_W`, `DS_L_A`). The ANSYS Creo connection filters by this name key; the **Designate** checkbox is not needed (it only publishes parameters to Windchill).

### Assemblies
- **FP-120** (print assembly): FP-121 and FP-122 both placed with **Default** constraint → shared origin. Used only for export.
![[sensor_3_seitenansicht.png]]

- **FP-100** (sensor assembly): FP-110 default; DMS front: coordinate-system constraint at x = `X_DMS`, y = -`B_S/2`, z = `T_FK`; DMS back: same x, flipped 180° about the x-axis, at z = 0 so it sits on the bottom face. (Adhesive layer neglected.)

### Export for printing
- FP-120: **File → Save As → 3MF** if your Creo version offers it (both parts in one file, positions kept) or export each part as STL in the **assembly coordinate system**. Import into ideaMaker, assign extruder 1 = PLA (substrate), extruder 2 = Protopasta (grid). Details: [[Druckparameter]].
- Print several DMS per job (at least 5 identical, requirement 10.3) plus 2 extra for the dummy coupon.
- FP-110: STL, 100 % infill, lines along x. Print an extra **dummy coupon** (e.g. a 30 × 12 × 3 mm plate) for the two dummy DMS.

## 5. Bonding jig
FP-130: a printed tray with a pocket matching the carrier outline (+0.2 mm clearance, depth = `T_FK`) and a hinged or loose **frame with a 30.2 × 10.2 mm window** whose edge starts at x = `X_DMS` from the grip end. Drop the DMS into the window → same position on every specimen (requirement 12.5). Flip the carrier for the back DMS. See [[Kontaktierung und Kleben]].

## 6. Variant B – co-printed
- Same FP-122 grid, placed so its top is 0.15 mm (1 layer) below the carrier top surface; cut the grid volume out of the carrier (Boolean/cut-out in Creo or let ideaMaker handle overlapping volumes by extruder priority).
- Leave the **pads uncovered** (no PLA above them) for contacting.
- Export carrier + grid as one 3MF with a shared origin.
- Compare with the bonded variant in [[Versuchsplanung]].

## 7. Checklist before the first print
- [ ] Measure jaw width and clamping length of the stand → adjust `L_GRIP`, `B_FK`
- [ ] Calibrate the nozzle X/Y offset of the Raise3D Pro2
- [ ] Slicer preview: 2 lines per leg, gaps empty, loops and pads solid
- [ ] Test print of the contact coupons ([[Kontaktierung und Kleben#Test plan for contacts]])
- [ ] After printing: R0 of every DMS → matched sets → order bridge resistors ([[Bestellung#Open points]])

## 8. What to vary later (Creo parameters → DoE)
`N_LEG` 2/4/6 · `W` 0.8/1.2 mm · `L_A` 6/10/14 mm · `T_G` 0.3/0.45 mm · bonded vs. embedded. See [[Versuchsplanung#Factors]].

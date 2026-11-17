---
topic: Literature summaries
date: 2026-11-17
tags:
  - forschungsprojekt
  - literatur
---
# Literatur
Back to [[Home]] · PDFs in `literature/`, full table with download script in `literature/README.md`

## Quick comparison
| Paper | Material | Build | R0 | k | Lin. / hyst. | Circuit |
|---|---|---|---|---|---|---|
| [[#Chadda et al. 2023]] | Protopasta on PLA substrate | glued on steel | 18.7 kΩ | **8.3** | ±4 % / creep | DMM |
| [[#Gooding et al.]] | graphene PLA in PLA | embedded | not checked (old note: ≈ 4.5 kΩ) | – | 5–6 % / ~20 % | voltage divider |
| [[#Maurizi et al. 2019]] | Protopasta in PLA | embedded, dual extrusion | – | 1.7–3.2 | linear | voltage divider |
| [[#Jasper 2026]] | Protopasta / Filaflex on PLA | printed on | 273 kΩ pad-to-pad | 0.4–1.3 | – | full bridge, NI 9237 |
| [[#Elgeneidy et al. 2018]] | conductive PLA in NinjaFlex | embedded | tens of kΩ (bridge R = 24 kΩ) | – | – | bridge + amplifier |
| [[#Lanzolla et al. 2022]] | PLA + CB + CNT | embedded | – | 0.077 Ω/g | hysteresis, temp. | dummy compensation |

## Chadda et al. 2023
*3D-Printed Strain Gauges Based on Conductive Filament for Experimental Stress Analysis* (TU Darmstadt). **Most useful paper for our design.**
- Two-layer design like a foil gauge: PLA substrate + Protopasta measuring grid, **bonded** to a steel plate (spring element).
- Grid: **4 tracks, 0.8 mm wide, active length 6 mm**; end loops wider than the tracks (inner radius 0.4 mm, outer 1 mm) against transverse sensitivity. Substrate 1 layer 0.2 mm, grid 2 layers × 0.15 mm (one layer left gaps).
- Prusa MK3s, nozzle 0.4 mm, bed 60 °C, PLA 215 °C, Protopasta **240 °C**; filament change between layers.
- FEA (COMSOL) to place the gauge: high strain (500–1000 µm/m) but below yield; gauge placed **10 mm from the clamping edge** to avoid the singularity there.
- Surface sanded + cleaned with acetone; bonded with cold-curing superglue (HBK Z70, cures in ~1 min under thumb pressure).
- Contact: **copper wires melted into the pads with a soldering iron**.
- Load: universal testing machine, 100 N reference cell, 30 N at 40 mm from the clamp; 3 settling cycles, then 0.2 N/s, 30 s hold, unload; ×4. Resistance with a Keithley DMM 7510.
- Results: R0 = 18 711.8 Ω, ΔR ≈ 64–67 Ω at 30 N, linearity error **±4 %**, R² = 0.996, **k = 8.3** (about 4× a metal foil gauge), creep present.
- Analytical model: cantilever deflection $z = FL^3/(3YI)$, gauge strain $\varepsilon = d\,L_{eff}^2F/(2YI)$, $\Delta R = S\cdot F$ with an experimentally found factor α.

## Gooding et al.
*3D Printed Strain Gauge Geometry and Orientation for Embedded Sensing* (UMKC).
- Graphene-PLA (BlackMagic3D, 0.6 Ω·cm) embedded one layer (0.2 mm) below the surface of PLA tensile bars 100 × 20 × 3.2 mm. **0.6 mm nozzle**, layer 0.2 mm.
- 3³ factorial design: end loops 1/3/5, strand width 1/1.5/2 mm, gauge thickness 0.2/0.4/0.6 mm; 27 designs × 3 copies.
- Instron load frame, wires heated and pushed into the tabs, voltage divider at 5 V, 2 kHz sampling.
- Average linearity 4.6–6.6 %, **hysteresis 17–26 %**, repeatability 4.5–8.3 %.
- More end loops → less hysteresis (24.3 → 19.2 %), but lower load sensitivity (−77 %). Thicker gauge → all errors up, sensitivity +45 %. Strand width: almost no effect.
- 5 loops → ~300 % higher resistance than 1 loop.
- Thickness was the only factor significant for all error types.
- Steep build orientations (45°, 90°) → weaker parts, conductive paths separate under strain.
- FEM: coupled thermal-electrical-mechanical simulation in ABAQUS; simulated ΔR **44 % higher** than measured because Poisson contraction was neglected; inconsistent extrusion also causes deviation.

## Maurizi et al. 2019
*Dynamic Measurements Using FDM 3D-Printed Embedded Strain Sensors* (Ljubljana/Perugia).
- Protopasta embedded in PLA beams by dual extrusion (Ultimaker 3), layer 0.1 mm, bed 60 °C, PLA 220 °C, Protopasta 225 °C, nozzle 0.4 mm, 100 % infill.
- **Resistivity of Protopasta: 30 Ω·cm in-layer, 115 Ω·cm out-of-layer** (manufacturer values).
- M-shaped sensor, 0.8 mm wide, 0.5 mm thick (5 layers); E = 3300 MPa, ρ = 1240 kg/m³ used for the beam.
- Voltage divider instead of Wheatstone bridge because ΔR is large (Ω instead of mΩ).
- Linear as long as the structure is linear; dynamic range from ~30 µε; usable up to a few kHz; temperature effect negligible in dynamics.
- k = 3.2 for the sensor without wide transverse parts, 1.7–1.8 for the sensors with wide end parts.

## Stano et al. 2024
*Effect of Process Parameters in Additively Manufactured Sensors prepared via Material Extrusion Processes* (Baylor).
- 2³ DoE on carbon-black PLA: ironing, nozzle temperature, infill overlap.
- Best: **ironing ON, 250 °C, overlap 0.2 mm** → resistance −47.9 %, UTS +31.9 %, elongation +25.8 %, flexural strength +28.1 %, intralayer voids −19.5 % (X-ray CT).

## Lanzolla et al. 2022
*Additive Manufacturing for Sensors: Piezoresistive Strain Gauge with Temperature Compensation*.
- PLA doped with carbon black + CNT; tested with an industrial robot (force/displacement profiles).
- Sensitivity 0.077 Ω/g and 12.54 Ω/mm (range 114 g, 0.7 mm).
- Resistance depends strongly on temperature → compensated with an **unloaded dummy sensor**.
- Hysteresis and viscoelasticity not negligible.

## Werkle et al. 2020
*Additive manufacturing of sensors – printing of conductor paths in loaded structures* (Uni Stuttgart, milling tools).
- Parameter study: print orientation, layer thickness, infill, temperature, speed, material combinations.
- 45° printing gave base resistances of about 20 kΩ and required conductor paths ≥ 1 mm thick (staircase effect).
- Four printed gauges in a full bridge on an aluminium body, bonded with 2K adhesive.

## Hashemi Sanatgar et al. 2022
*Piezoresistive Properties of 3D-Printed PLA Nanocomposites* (compression).
- Own PLA/MWNT and PLA/Ketjenblack filaments; percolation threshold 1 wt.% MWNT, 4 wt.% KB.
- Under compression resistance **drops** (negative pressure coefficient), about one decade up to 18 N.
- PLA/1 % MWNT: G = 7.6 in cycles, linear 10–100 kPa. KB composites not stable in cycles.

## Minetola & Giubilini 2024
*Multi-material FFF of an embedded strain gauge for low-cost real-time monitoring*.
- Graphene PLA (Grafylon) in PETG and N-ASA tensile specimens; Arduino + Wheatstone bridge; DIC.
- Works only in the **elastic range**; less accurate for small strains; partial detachment at the contacts (filament pieces stuck to the metal pins).

## Jasper 2026
KTU Kaunas, master thesis.
*Research and development of 3D printed strain sensors for structural state and health monitoring* (master thesis).
- Compared Protopasta PLA vs. Filaflex conductive TPU; Protopasta chosen. Pad-to-pad **273–275 kΩ** (Filaflex ≈ 1.1 MΩ).
- Serpentine track 0.4 mm wide, 0.2 mm thick on a 10 × 45 mm PLA substrate; nozzle 0.4, layer 0.2, Protopasta 225 °C, bed 60 °C, manual filament change.
- Two full-bridge layouts (137 kΩ and 100 kΩ); NI 9237 bridge module.
- Contact: copper tape was unstable; **thermal bonding with conductive PLA** (soldering iron ~350 °C) was stable and repeatable.
- Gauge factor 1.27 (compact layout, tension) vs. 0.40 (longitudinal layout).

## Elgeneidy et al. 2018
*Directly Printable Flexible Strain Sensors for Bending and Contact Feedback of Soft Actuators* – the template named in the project description.
- Conductive PLA tracks inside a NinjaFlex body, dual extrusion (LulzBot TAZ 5, FlexyDually). Sensor 1.2 mm thick, tracks 0.6 mm.
- Rules: track width **≥ 2× nozzle diameter**, track height < 0.5 mm, constant spacing, care with extruder switching.
- Base resistance varied ~5 % between five samples; bridge reference resistor set to 24 kΩ.
- Wiring: **conductive thread wound around the terminals and fixed with hot glue** (basis for AP 3).
- Self-heating caused drift → reduced current through the bridge and signal conditioning.

## Other papers in the folder
- Rossetti et al.: aerosol-jet silver sensors embedded by print-pause-print; **ironing** reduced surface roughness by ~89 %; sensitivity 0.87 ± 0.12.
- Georgopoulou et al. 2021: TPU gripper with integrated sensors; sensors linear up to 30 % strain; Shore hardness affects sensitivity.
- Books: Hoffmann (HBM) and Keil – theory, bridge circuits, wiring, adhesives → [[Grundlagen]], [[Messschaltung]].

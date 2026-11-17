---
topic: Printing the sensor on the Raise3D Pro2
date: 2026-11-17
tags:
  - forschungsprojekt
  - fertigung
  - 3d-druck
---
# Druckparameter
Back to [[Home]] · Printer: Raise3D Pro2 (dual extruder), slicer ideaMaker · Related: [[Implementation]], [[Versuchsplanung]]

## Starting values (to be confirmed by tests)
| Parameter | DMS substrate (PLA) | DMS grid (Protopasta) | Carrier (PLA) | Literature |
|---|---|---|---|---|
| Nozzle | 0.4 mm | 0.4 mm | 0.4 mm | Chadda, Maurizi, Jasper: 0.4; Gooding 0.6 caused inconsistent extrusion |
| Layer height | 0.15 mm | 0.15 mm | 0.15 mm | Chadda 0.15 (grid), Maurizi 0.1, Jasper 0.2 |
| Layers | 2 (= 0.3 mm) | 2 (= 0.3 mm) | 20 (= 3.0 mm) | one grid layer left gaps (Chadda) |
| Nozzle temp. | 215 °C | **225–240 °C** (DoE: up to 250 °C) | 215 °C | 225 (Maurizi, Jasper), 240 (Chadda), 250 best R (Stano) |
| Bed temp. | 60 °C | 60 °C | 60 °C | all |
| Infill | 100 % | 100 %, lines **along the legs (0°)** | 100 %, lines along the load axis | Maurizi 100 % |
| Extrusion width | 0.4 mm | 0.4 mm → 2 lines per 0.8 mm leg | 0.4 mm | |
| Ironing | – | test ON/OFF (top layer) | – | Stano: −48 % resistance with ironing |
| Infill overlap | – | test 0.2 mm | – | Stano |
| Speed | normal | slow (≈ 20–30 mm/s) for the grid | normal | – |
Document all values for every print (requirement 10.2) → print log in [[Versuchsplanung#Print log]].

## Dual extrusion on the Raise3D Pro2
- Model substrate and grid as **separate bodies/parts with a shared origin** in Creo; export from the assembly as one **.3mf** (or two STLs with the same coordinate system) so that ideaMaker keeps the alignment. See [[Implementation#Export for printing]].
- In ideaMaker assign extruder 1 = PLA, extruder 2 = Protopasta.
- Activate the **prime tower** (and ooze shield if needed) so the idle nozzle doesn't leak onto the part.
- Calibrate the X/Y offset between the two nozzles before printing sensors – a 0.2 mm offset is already a quarter of a leg width.
- Alternative without dual extrusion: pause at the layer change and swap filament manually (Chadda, Jasper).

## Orientation
- Print everything **flat on the bed**; the grid must lie in **one layer plane** (in-plane resistivity ~30 Ω·cm vs. ~115 Ω·cm across layers; steep orientations separate the paths under strain, Gooding).
- Raster of the grid parallel to the legs, so the current flows along the extrusion lines.
- The legs are 0.8 mm = 2 extrusion lines. Check in the slicer preview that the slicer does **not** drop or merge lines in the 0.8 mm gaps and the 0.8 mm wide legs (Elgeneidy: track width ≥ 2× nozzle).

## Quality checks after printing
- Visual: no gaps in the legs, no bridges between legs, no stringing between pads.
- Measure every DMS: R0 (4-wire), thickness with the Millimess gauge, mass.
- Discard sensors with R0 outside ±10 % of the batch median; sort the rest into matched sets for the bridge ([[Messschaltung#Bridge design]]).
- Re-measure R0 after about 24 h at room temperature before bonding; if R0 drifts after printing, make a fixed rest time part of the procedure.

## Filament handling
- Keep Protopasta dry (PLA absorbs moisture → bubbles, inconsistent extrusion); dry it if prints look porous.
- The carbon-filled filament is brittle → avoid sharp bends in the feed path; check the nozzle for wear if extrusion gets inconsistent.

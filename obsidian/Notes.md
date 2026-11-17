---
topic: Ideas, open questions, to-dos
date: 2026-11-17
tags:
  - forschungsprojekt
  - inbox
---
# Notes – ideas, open questions, to-dos
Back to [[Home]]

This note replaces the old unsorted notes from 15.10.2026. Every old item was moved into a topic note; the table shows where.

## Where the old notes went
| Old note | Now in |
|---|---|
| Sensor must work at room temperature (20–30 °C) | [[Anforderungsliste#Gaps and inconsistencies to fix before 10.12.]] (suggested 14.1) |
| Force-displacement measurement, up to 100 N | [[Projektauftrag]], [[Anforderungsliste]] |
| ANSYS can do piezoresistive simulations (+ link) | [[Simulation ANSYS]] |
| FDM makes conductive PLA anisotropic (Z vs. X/Y) | [[Grundlagen#Anisotropy from FDM printing]] |
| Behaviour under repeated loads? | [[Grundlagen#Behaviour of conductive PLA under load]], [[Versuchsplanung#Load protocol (based on Chadda et al.)]] |
| Same thermal expansion for carrier and conductive PLA | [[Grundlagen#Temperature]] |
| Kreuzer bridge, 3/4/6-wire measurements | [[Grundlagen#Lead resistance and wiring]], [[Messschaltung#Wiring]] |
| Second conductive filament + t-test | [[Versuchsplanung#Plan]] |
| Adhesives (EA 3430, Loctite 401, what to avoid) | [[Kontaktierung und Kleben]] |
| Prime tower for dual extrusion | [[Druckparameter#Dual extrusion on the Raise3D Pro2]] |
| Dual extrusion: parts with shared origin, export 3MF from the assembly | [[Implementation#Export for printing]] |
| Paper notes (Dynamic Measurement, 3D-Printed SG, Geometry & Orientation, Process Parameters) | [[Literatur]] |
| DoE factors (strand width, end loops, gauge length, distance to clamp, nozzle, temps, ironing) | [[Versuchsplanung#Factors]] |

## Open questions (for the jour fixe 19.11. and the team)
- [ ] Demo date: 17.12. (Projektaufgabe/Projektantrag) or 18.12. (Lastenheft)? Dates in the assignment still say 2025.
- [ ] Which sub-functions must be shown at the demo (Lastenheft Tabelle 4 is empty)?
- [ ] Is a real **force–displacement** curve expected, or is force → signal enough? The PLA carrier only stretches ~0.04 mm at 100 N ([[Implementation#Expected signal]]).
- [ ] What exactly is broken on the old Kraft-Weg-Messplatz? Repair or rebuild?
- [ ] Is the 10 kg load cell (≈ 98 N) enough as reference for 100 N, or do we need 20 kg?
- [ ] Which room: B001 (equipment), B402L (Projektantrag), B L17c (fabrication)?
- [ ] Manufacturer contact (Projektaufgabe Teilaufgabe 3): e.g. ask Protoplant (Protopasta) for resistivity vs. temperature, recommended print temperature, anisotropy data – and **log the contact**.
- [ ] Compression vs. tension: does k differ in sign/size? (Hashemi Sanatgar: resistance drops under compression.)
- [ ] Can the GSV-3USB handle a ~30 kΩ bridge, or do we use HX711/ADS1115?

## To-dos (next two weeks)
- [ ] Measure the jaws of the stand → set `L_GRIP`, `B_GRIP` ([[Implementation#7. Checklist before the first print]])
- [ ] Build FP-110/121/122 in Creo with parameters ([[Implementation#4. Building it in Creo Parametric]])
- [ ] Contact test coupons ([[Kontaktierung und Kleben#Test plan for contacts]])
- [ ] First print, R0 of 5+ sensors → order matching bridge resistors ([[Bestellung#Open points]])
- [ ] Fix the requirement list gaps ([[Anforderungsliste#Gaps and inconsistencies to fix before 10.12.]])
- [ ] Add today's AI use to the prompt log ([[Projektplanung#Rules on AI use (Anlage I of the assignment)]])
- [ ] Schematic diagram (black/white line drawing, A4, caption + legend) for 03.12.
- [ ] ProjectLibre plan: process-oriented PSP, Gantt, baseline, critical path, resources, costs

## Ideas
- Full bridge with front/back DMS + two dummies → temperature and bending compensation ([[Messschaltung#Recommended setup]]).
- Use the second HX711 channel or a second HX711 for the PLA bridge.
- Bonding jig for reproducible positioning ([[Implementation#5. Bonding jig]]).
- Later: python GUI with live force-signal plot and CSV export (E2).

---
topic: Requirement list (VDI 2222)
date: 2026-11-17
tags:
  - forschungsprojekt
  - requirements
---
# Anforderungsliste
Back to [[Home]] · Source: `project_management/Anforderungsliste.xlsx` (Version 001, 02.11.2026, status "In Arbeit")

F = Festforderung (must, yes/no) · Z = Zielforderung (optimise, "as … as possible") · W = Wunsch (nice to have). Source codes: LH = Lastenheft.

## Key requirements for the design
| No. | Requirement | Value | Type | Source |
|---|---|---|---|---|
| 1.1 | Convert force into a change in resistance (piezoresistive effect of conductive PLA) | – | F | LH |
| 1.2 | Convert ΔR into a voltage with a Wheatstone bridge | – | F | LH |
| 1.3 | Amplify and digitise the bridge voltage | – | F | LH |
| 1.4 | Compute force in N with a calibration function | – | F | LH |
| 1.5 | Calibrate and test against a reference force on the test stand | – | F | LH |
| 1.6 | Measure **compressive** forces along the main axis | – | F | supervisor |
| 1.7 | Also measure **tensile** forces | – | W | supervisor |
| 2.1 | Sensor element as short as possible | 30 / 50 mm | Z | – |
| 2.2 | Position and size of the load introduction area defined | – | F | assumption |
| 2.3 | Two contact areas for the electrical connection | 25 mm² | F | assumption |
| 2.4 | Clamp or place the sensor in the test stand (mechanical interface) | – | F | assumption |
| 4.1 | Measuring range | 0–100 N | F | supervisor |
| 4.2 | Permanent deformation after unloading | ≤ 1 % of nominal travel | F | assumption |
| 4.3 | Linearity error | 3 (target) – 5 (max) % FS | Z | Hoffmann |
| 4.4 | Hysteresis | 5 – 10 % FS | Z | Hoffmann |
| 4.5 | Creep/drift under constant load as small as possible | – | Z | – |
| 4.6 | Load introduction must not shift sideways | 2 mm | F | assumption |
| 5.1 | Supply via USB (5 V) or lab power supply | – | F | – |
| 5.2 | Electrical power in the sensor only as high as needed (no self-heating) | – | Z | – |
| 5.3 | Stable bridge supply | ≤ 1 % peak-to-peak | F | assumption |
| 5.4 | Battery operation possible | – | W | – |
| 6.1 | Thermal expansion of carrier ≈ conductive PLA | – | Z | Hoffmann |
| 6.2 | Low-resistance contacting | ≤ 5 % of R0 | F | assumption |
| 7.1 | Adjustable gain to use the ADC range | 10–100 | F | assumption |
| 7.2 | ADC resolution | 12–16 bit | F | assumption |
| 7.3 | t90 response time | ≤ 500 ms | F | assumption |
| 9.1 | Short manual (setup, calibration, measurement) | ≤ 3 pages | F | LH |
| 9.2 | Start a measurement in few steps | 5–10 steps | Z | – |
| 9.3 | Evaluation with a GUI, no programming needed | – | W | – |
| 10.1 | FDM print from **Protopasta conductive PLA, 1.75 mm** | – | F | Labor B001 |
| 10.2 | Document print parameters (temperature, speed, infill) | – | F | LH |
| 10.3 | At least **5 identical sensor elements** to assess scatter | – | F | assumption |
| 10.4 | Own PCB for the electronics | – | W | – |
| 10.5 | DMS carrier made of normal PLA, ideally 3D-printed | – | W | supervisor |
| 11.1 | Force-voltage curve with ≥ 5 load steps | 5 | F | LH |
| 11.2 | Test report with date, setup, parameters | – | F | LH |
| 12.2 | Assembly time per sensor | 10 min | Z | – |
| 12.3 | Electrical connection without soldering | – | W | – |
| 12.5 | Reproducible, defined positioning in the test stand (e.g. stop) | – | F | LH |
| 13.1 | Storage 0–40 °C | – | F | – |
| 17.1 | Total budget | ≤ 200 € | F | LH |
| 17.2 | Purchases agreed with the supervisor beforehand | – | F | LH |
| 18.1 | Order form finalised | 05.11.2026 | F | LH |
| 19.1 | CAD and source code under version control | – | F | LH |
| 19.2 | Documentation: report, drawings, circuit diagrams, source code | – | F | LH |

## Implications for the design
- 4.1 + resolution 2 N (Projektantrag) → the signal must resolve **2 % FS**. With the geometry in [[Implementation]] that means about 0.6–3 Ω change on ~30 kΩ.
- 1.6 (compression is a must) → the spring element must not **buckle** at 100 N → checked in [[Implementation#3. Federkörper]].
- 6.1 → carrier from plain PLA, same matrix as Protopasta (also W 10.5).
- 10.3 → print at least 5 sensors per variant; fits the statistics in [[Versuchsplanung]].
- 12.3 (no soldering) conflicts with the literature, where wires are melted into the pads with a soldering iron. See [[Kontaktierung und Kleben]].

## Gaps and inconsistencies to fix before 10.12.
- Sections **3 Kinematik, 8 Sicherheit, 14 Gebrauch, 15 Instandhaltung, 16 Recycling** are empty. Ideas: 3.1 test speed of the stand (mm/min), 3.2 travel range; 8.1 max. voltage on exposed pads (SELV), 8.2 overload stop / end switch at the stand; 14.1 operating temperature 20–30 °C (from [[Notes]]); 15.1 sensor element replaceable without tools; 16.1 PLA parts separated from electronics for disposal.
- **12.1 and 12.4 are identical** (wiring diagram + pin assignment).
- Row **1.7** has a stray "1." in the number column; row **9,2** uses a comma.
- 2.1: unclear whether 30 / 50 mm means Min/Soll or Soll/Max – make the column explicit.
- 2.3: "25 mm²" is in the Soll column; should probably be Min.
- 4.2 and 7.3 need a basis (source) instead of "Annahme" where possible.
- Projektaufgabe asks for the **Suchmatrix nach VDI 2222** with at least three requirements entered – not in the xlsx yet.

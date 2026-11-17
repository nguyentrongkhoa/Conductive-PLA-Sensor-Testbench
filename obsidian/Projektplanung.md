---
topic: Work packages, milestones, risks, budget
date: 2026-11-17
tags:
  - forschungsprojekt
  - projektmanagement
---
# Projektplanung
Back to [[Home]] · Sources: `miscellaneous/Projektantrag.tex`, `miscellaneous/Arbeitspakete.tex`, `glossar/`

Planning tool: **ProjectLibre** (allowed besides MS Project and OpenProject). The work packages must also be entered in OpenProject (KoCAD lab).

## Roles
| Person | Role | Background |
|---|---|---|
| Khoa Nguyen | Electronics development and programming | prototyping, PCB design, STM32 programming |
| Joffre Nunez Rodriguez | CAD design and fabrication | Creo Parametric, 3D printing |

## Work packages (Projektantrag)
**AP 1 – Project management, concept, requirement analysis**
Requirements, time and resource plan, budget (< 200 €); Lasten- and Pflichtenheft; state of the art (conductive PLA force sensors, based on Elgeneidy et al. 2018); mechanical, electrical and software interfaces.

**AP 2 – Mechanical design and CAD**
Design and build the test stand for clamping and loading the sensors: CAD of guide and specimen holders, interfaces for the load cell and adjustment elements, selection/purchase of mechanical parts, manufacturing / 3D printing of prototype parts.

**AP 3 – Electrical engineering and sensor connection**
Reliable contacting of the PLA sensors (conductive thread, metal pins), measuring circuit (e.g. Wheatstone bridge), wiring, amplification, connection to a microcontroller such as an STM32.

**AP 4 – Software and control**
Firmware for data acquisition, GUI or script (Python/MATLAB) for real-time force-displacement curves, filter and calibration algorithms.

**AP 5 – Integration, calibration, documentation**
Hardware-in-the-loop tests, calibration with reference loads and travel, documentation and operating manual, final presentation and handover.

> [!tip] Lastenheft rule
> Each person needs at least two detailed work packages of similar size. Suggested split: Khoa → AP 3 + AP 4, Joffre → AP 2 + sensor CAD/printing from [[Implementation]]; AP 1 and AP 5 shared.

## PSP (Projektstrukturplan) – product-oriented version from the glossary entry
Definition (DIN 69901-5:2009-01): complete hierarchical representation of all elements (sub-tasks and work packages) of the project structure as a diagram or list.

```
0 Kraftsensor aus leitendem PLA
├── 1 Konstruktion
│   ├── 1.1 DMS
│   └── 1.2 Kraft-Weg-Messplatz
├── 2 Elektronik
│   ├── 2.1 Brückenschaltung
│   └── 2.2 Verstärkerschaltung
└── 3 Software
    ├── 3.1 Datenaufzeichnung
    └── 3.2 Datenauswertung
```
Talking points (from the speaking notes): the PSP says *what*, not *when*; 100 % rule; break down until a package can be estimated and assigned (rule of thumb 8–80 h, not a standard); alternative structures: object-, function- or phase-oriented. For the Lastenheft, a **process-oriented** PSP with phases is required in addition.

## Milestones
| No. | Date | Milestone |
|---|---|---|
| M1 | 29.10.2026 | Projektantrag submitted |
| M2 | 05.11.2026 | BOM done, parts ordered |
| M3 | 12.11.2026 | Concept and technical presentation |
| M4 | 26.11.2026 | First sensor printed and contacted, ΔR measurable |
| M5 | 03.12.2026 | Measuring chain running, first force-displacement curve |
| M6 | 10.12.2026 | Pflichtenheft, project plan, requirement list submitted |
| M7 | 17.12.2026 | Functional model demonstrated |
| M8 | 14.01.2027 | Calibration with reference loads done |
| M9 | 28.01.2027 | Technical report, handover to the lab |

Constraints: lab use only during exercise hours, **Thursdays 12:15–14:30**. Labs named in the documents: B402L (GOS) in the Projektantrag, fabrication in B L17c, equipment in **B001** (see [[Labor]]).

## Risks (Projektantrag)
| No. | Risk | Prob. | Impact | Countermeasure |
|---|---|---|---|---|
| R1 | Unreliable contact (contact resistance, drift) | high | high | test several contact variants early ([[Kontaktierung und Kleben]]) |
| R2 | ΔR too small, too much noise | medium | high | bridge, amplifier, digital filters ([[Messschaltung]]) |
| R3 | Late delivery of parts | medium | medium | order early, use lab parts |
| R4 | Time pressure / absence | medium | medium | buffers, clear split, shared docs |
| R5 | Budget overrun | low | medium | 10 % reserve, lab parts |

Additional risks found while reviewing the literature:
- **R6 Creep and hysteresis of conductive PLA** (20 % hysteresis reported by Gooding et al.) may exceed the Z-limits 4.4/4.5 → load protocol with settling cycles, hold phases, see [[Versuchsplanung]].
- **R7 Bridge offset from scatter of R0** (~5 % between prints) may saturate the amplifier → trimmer in the bridge, see [[Messschaltung]].

## Budget (Projektantrag estimate)
| Item | Estimate |
|---|---|
| Mechanics (linear guide, drive) | 60 € |
| Electronics/sensors (load cell, displacement sensor, amplifier, µC) | 70 € |
| Consumables (≈ 500 g conductive PLA, PLA, cables) | 40 € |
| Reserve 10 % | 17 € |
| **Total** | **187 €** |
Actual orders: see [[Bestellung]].

## Rules on AI use (Anlage I of the assignment)
- AI may only help with **wording** and **research**; no copying of generated content; the team is fully responsible for correctness.
- Every use beyond spell checking must be disclosed: formal statement at the end of the report + **prompt log** table (tool, date, purpose, prompt).
- Undeclared use counts as cheating → whole exercise failed.
- The Projektantrag already has a prompt log (Claude 15.10.2026, Gemini 19.10.2026).

> [!warning] To log
> Restructuring these notes with Claude (17.11.2026) and the proposed sensor geometry in [[Implementation]] count as AI use → add both to the prompt log.

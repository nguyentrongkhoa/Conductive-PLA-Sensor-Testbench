---
topic: Project overview
date: 2026-11-17
tags:
  - forschungsprojekt
  - index
---
# Force sensor made of conductive PLA ("DMS") – overview

**Project (Thema 15):** Entwicklung eines Kraft-Weg-Messplatzes für Kraftsensoren aus leitendem PLA als „DMS"
**Module:** M08 F.- o. E.-Projekt, Master Mechatronik, BHT Berlin, WS 2026/27
**Supervisor:** Prof. Dr.-Ing. Karsten Pietsch
**Team:** Khoa Nguyen (electronics, programming) · Joffre Nunez Rodriguez (CAD, fabrication)
**Duration:** 15.10.2026 – 28.01.2027 · **Budget:** < 200 €

## Goal in one sentence
Develop and 3D-print a strain gauge (DMS) from conductive PLA (Protopasta) that measures forces from 0 to 100 N with a resolution of at least 2 N, and show its force-displacement/force-signal curve on a (repaired or rebuilt) Kraft-Weg-Messplatz in the lab.

## Map of notes
| Area | Note |
|---|---|
| Assignment, deliverables, deadlines | [[Projektauftrag]] |
| Requirements (VDI 2222) | [[Anforderungsliste]] |
| Work packages, milestones, risks, budget, AI rules | [[Projektplanung]] |
| Lab equipment and test stand | [[Labor]] |
| Orders and costs | [[Bestellung]] |
| Theory: strain gauges and conductive PLA | [[Grundlagen]] |
| Literature summaries | [[Literatur]] |
| Measurement circuit and amplifier | [[Messschaltung]] |
| Bonding and electrical contacting | [[Kontaktierung und Kleben]] |
| Printing the sensor on the Raise3D Pro2 | [[Druckparameter]] |
| **Sensor geometry and Creo build guide** | [[Implementation]] |
| FEM in ANSYS (parametric) | [[Simulation ANSYS]] |
| Test plan and design of experiments | [[Versuchsplanung]] |
| Ideas, open questions, to-dos | [[Notes]] |

## Next milestones
| Date | Milestone |
|---|---|
| 19.11.2026 | Jour fixe: Lastenheft finalised incl. acceptance criteria for the demo |
| 26.11.2026 | M4: first sensor printed and contacted, change in resistance measurable |
| 03.12.2026 | M5: measuring chain runs, first force-displacement curve; presentation of the schematic |
| 10.12.2026 | M6: Pflichtenheft, project plan, requirement list submitted |
| 17.12.2026 | M7: demo of the functional model |
| 14.01.2027 | M8: calibration with reference loads finished |
| 28.01.2027 | M9: technical report submitted, handover to lab |

Details and date conflicts between the documents: see [[Projektauftrag#Deadlines]].

## Folder structure of the repo
- `literature/` papers and books (overview in `literature/README.md`, summaries in [[Literatur]])
- `datasheets/` Raise3D Pro2 manual, Käfer MD12 dial gauge, GSV-3USB amplifier
- `project_management/` Anforderungsliste.xlsx, Bestellscheine, Projektantrag, Projektbeschreibung
- `miscellaneous/` LaTeX sources of Projektantrag and Arbeitspakete
- `glossar/` glossary entry and speaking notes on the PSP (Projektstrukturplan)
- `pics/` photos of the lab equipment
- `cad/` Creo files (currently empty → see [[Implementation]])
- `obsidian/` this vault

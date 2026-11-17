---
topic: Assignment, Lastenheft, deliverables
date: 2026-11-17
tags:
  - forschungsprojekt
  - organisation
---
# Projektauftrag
Back to [[Home]]

Sources: `project_management/Projektbeschreibung.pdf` (Steckbrief Thema 15), `2026-27-WS-F.o-E.-projekt-Lastenheft-Rev1.pdf`, `2026-27-WS-Projektaufgabe-2.pdf`, `miscellaneous/Projektantrag.tex`

## Topic (Steckbrief)
- **Thema 15:** Kraft-Weg-Messplatz for force sensors made of conductive PLA as a "DMS".
- Scope: **SW** control software · **ET** sensor connection · **CAD** connection of the sensor to the test stand.
- Inspiration: Elgeneidy et al. 2018, *Directly Printable Flexible Strain Sensors for Bending and Contact Feedback of Soft Actuators* (see [[Literatur#Elgeneidy et al. 2018]]).
- Stakeholders: more lab capacity for students, demonstrator for teaching.
- Budget < 200 €, team of 2–3.

## Our project goal (from the Projektantrag)
- Develop and additively manufacture a DMS made of conductive PLA as a force sensor.
- Range **0–100 N**, resolution **≥ 2 N**.
- The assigned Kraft-Weg-Messplatz is **no longer working** → it may need to be rebuilt as a prototype (clamping or guided loading of the specimen, connection of the electronics).
- First question to answer: which **substrate/carrier material** suits the conductive PLA. Elgeneidy used NinjaFlex because it bonds well to PLA in multi-material printing. We want to make substrate and sensor **separately**, so the bonding method matters (see [[Kontaktierung und Kleben]]).
- The DMS has two terminals for an external Wheatstone bridge; resistance read e.g. with an STM32. The change in resistance should be (ideally) linear in the deformation and is plotted as a force-displacement curve to judge linearity and usefulness.

## Expected results (Projektantrag)
| No. | Deliverable | Success criterion |
|---|---|---|
| E1 | Functional model DMS (CAD files + printed prototype) | FEM results match the defined forces and deformations |
| E2 | Measurement and evaluation software | Real-time display of the curve; export as CSV |
| E3 | Pflichtenheft, Anforderungsliste, project plan | Submitted 10.12.2026 |
| E4 | Demo of the functional model | Shown 17.12.2026 |
| E5 | Technical report with drawings, circuit diagram, source code, operating manual | Submitted 28.01.2027; students can run a measurement without help |

## What the Lastenheft requires (deliverables)
- **Ablaufplanung:** at least two detailed work packages per team member, equal workload, none consisting only of trivial tasks (BOM, order form). Also enter the work packages in **OpenProject** (KoCAD lab login).
- **Schematic diagram:** own drawing made with visualisation software, black-and-white line drawing, max. DIN A4, caption and legend. No shaded CAD views, no modified pictures (plagiarism = fail).
- **Project planning** in MS Project, OpenProject or ProjectLibre:
  1. Product structure plan + process-oriented PSP as a task list (each task = noun + verb, hours per task, baseline)
  2. Linked bar chart with dependencies, phases as summary tasks, milestones (e.g. design reviews), project duration and end, free float, critical path in a separate view
  3. Resource plan as Gantt with resources on the bars, utilisation, cost per resource
  4. Total project cost incl. material
  5. Document the plans (Gantt without page-filling legend)
  6. Baseline, status update at the Pflichtenheft deadline with progress lines, updated end date at constant cost, options to still meet the deadline
  - Hourly rates: Musterbau 45 €, workshop staff 40 €, student worker 19 €. 8 h working day, no work on public holidays.
- **CAD:** model in **Creo Parametric**, drawing set derived from the models, sensible numbering system.
- **Circuit diagram** with standard symbols + pin assignment table, stored in the product database.
- **Software:** control program for the hardware.
- **Functional model:** parts manufacturable in the lab or a normal workshop; electrical parts are ordered through the lab (no refunds for private purchases); include delivery times in the plan.
- **Documentation:** incl. operating manual; software documented per the software-engineering module; everything (commented source code, circuit diagram) on the BHT Nextcloud project drive.
- **Cost:** must not exceed the approved budget.

## Projektaufgabe 2 (requirement list + Pflichtenheft)
Sub-tasks: (1) choose the system, (2) half-page abstract with existing products and sources, (3) research incl. **contacting a manufacturer by phone/e-mail and logging it**, (4) collect requirements with feature list and **Suchmatrix nach VDI 2222 Bl. 1** (at least three requirements in the matrix fields), (5) structured requirement list with **≥ 20 requirements**, F/Z/W category and source, (6) schematic diagram (landscape allowed on the slide), (7) Pflichtenheft with baseline, (8) schedule and performance control via Gantt.
Grading: completeness of the requirement list, correct citations, clarity, correct F/Z/W assignment, all sub-tasks done. Reference: Hering & Hering, *Technische und Naturwissenschaftliche Berichte*, 9th ed., 2024.
Also required: a short talk (Kurzreferat), several tests. Late submissions count as failed.

## Deadlines
| Item | Projektaufgabe 2 | Projektantrag | Note |
|---|---|---|---|
| Start | 29.10.2026 | M1 29.10.2026 | |
| Requirement list shown | 05.11.2026 | M2 BOM + order 05.11.2026 | |
| Work packages presented | "12.11.2025" | M3 12.11.2026 | year typo in the assignment |
| Jour fixe (finalise Lastenheft) | "19.11.2025" | – | |
| Presentation schematic (10 min free talk) | "03.12.2025" | M5 03.12.2026 | |
| Pflichtenheft upload (Moodle, PDF) | "10.12.2025" | M6 10.12.2026 | |
| Demo | "17.12.2025" | M7 17.12.2026 | Lastenheft table says **18.12.2025** → clarify |
| Calibration done | – | M8 14.01.2027 | own milestone |
| Report + handover | – | M9 28.01.2027 | |

> [!warning] Clarify with Prof. Pietsch
> The assignment PDFs still contain 2025 dates (copied from last year) and the demo date differs (17.12. vs 18.12.). The project tables in the Lastenheft (Tabelle 1, 2, 4) are empty in our PDF – the supplementary requirements and the definition of the demo sub-functions still have to be agreed at the jour fixe on 19.11.

## Pflichtenheft content (A4 with cover page)
Abstract · Anforderungsliste · research results · work packages per person · project planning with baseline and schedule/performance control via Gantt.

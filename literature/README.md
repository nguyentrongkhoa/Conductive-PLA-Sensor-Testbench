# Literatur: 3D-gedruckte Dehnungsmessstreifen (leitfähiges PLA)

Übersicht der Paper zum Thema eingebettete bzw. gedruckte Dehnungssensoren aus leitfähigem Filament (Stand: 12.11.2026).

**Download:** Die Dateien werden mit `download_papers.ps1` geladen und nach dem Titel benannt:

```
powershell -ExecutionPolicy Bypass -File .\download_papers.ps1
```

Bereits vorhandene Dateien werden übersprungen. Schlägt ein Download fehl (Paywall, Captcha), listet das Skript den Link zum manuellen Laden auf.

## Übersicht

| Datei (Titel) | Autoren, Jahr | Thema | Relevanz für das Projekt |
|---|---|---|---|
| Dynamic Measurements Using FDM 3D-Printed Embedded Strain Sensors | Maurizi et al., 2019 | Leitfähiges PLA (ProtoPasta, Carbon Black) wird per Dual-Extrusion in PLA-Balken mitgedruckt; dynamische Messungen, Temperatur, Nichtlinearität | Direktes Vorbild: eingebetteter Sensor, gleiche Materialkombination |
| Additive Manufacturing for Sensors - Piezoresistive Strain Gauge with Temperature Compensation | Lanzolla et al., 2022 | Kostengünstiger gedruckter DMS aus PLA mit Carbon Black, mit Temperaturkompensation | Temperaturdrift und Kompensation |
| 3D-Printed Strain Gauges Based on Conductive Filament for Experimental Stress Analysis | Chadda et al., 2023 | Mäander-Messgitter aus leitfähigem PLA auf PLA-Substrat, auf Stahl geklebt, Vergleich mit herkömmlichen DMS | Gitter-Geometrie, Aufbau wie ein Folien-DMS |
| Piezoresistive Properties of 3D-Printed Polylactic Acid (PLA) Nanocomposites | Hashemi Sanatgar et al., 2022 | PLA mit MWNT bzw. Ketjenblack, piezoresistives Verhalten unter zyklischer Druckbelastung | Druckbelastung (statt Zug), Füllstoffgehalt und Messfaktor |
| Research and development of 3D printed strain sensors for structural state and health monitoring | Jasper (KTU), 2026 | ProtoPasta-PLA und leitfähiges TPU; Zug, Dreipunktbiegung, Torsion; Wheatstone-Brücke; Messfaktor um 1 | Auslegung von Sensorlayouts, Brückenschaltung |
| Additive manufacturing of sensors - printing of conductor paths in loaded structures | Werkle et al., 2020 | Einfluss der Druckparameter (Temperatur, Füllmuster, Schichthöhe, Druckwinkel) auf den Widerstand; Biegung und Torsion | Druckparameter und hoher Grundwiderstand |
| Multidirectional strain sensor using multimaterial 3D printing | Chirila et al., 2022 | Piezoresistive Elastomerschicht in starrem PLA-Rahmen, fünf Sensorelemente, COMSOL-Simulation | Mehrachsige Kraftmessung, Anordnung mehrerer Sensoren |
| A preliminary study on multi-material fused filament fabrication of an embedded strain gauge for low-cost real-time monitoring of part strain | Minetola, Giubilini, 2024 | Graphen-PLA als DMS in PETG- und N-ASA-Zugproben, Auslesung per Arduino und Wheatstone-Brücke | Eingebetteter DMS, Grenzen: nur im elastischen Bereich zuverlässig, teils Ablösung |
| Effect of Process Parameters in Additively Manufactured Sensors prepared via Material Extrusion Processes: Correlation among Electrical, Mechanical and Microstructure Properties | Stano et al., 2024 | Versuchsplanung zu Ironing, Drucktemperatur und Überlappung bei Carbon-Black-PLA-DMS; etwa 48 % weniger Widerstand | Optimierung der Druckparameter |
| Three-Dimensional Printed Nanocomposites with Tunable Piezoresistive Response | Aliberti et al., 2024 | Einfluss von Rasterwinkel (0°/90°) und CNT-Gehalt auf die Empfindlichkeit (Material: ABS mit CNT, nicht PLA) | Einfluss der Druckrichtung, Kreuz-Sensor |
| Electromechanical Properties of 3D-Printed Smart Materials for Structural Health Monitoring | Saleh et al., 2022 | Gedruckte Verbunde mit Kupfer- bzw. NiCr-Draht in PLA und Kupfer in TPU, Zug- und Ermüdungsversuche | Alternative Sensorik, lineare Widerstandsänderung |
| Aerosol Jet Printed and Photonically Cured Sensors Embedded in 3D Printed Smart Orthoses - A Preliminary Study | Rossetti et al. | Aerosol-Jet-Sensoren, per Print-Pause-Print in PLA eingebettet, Biegeproben | Einbettung durch Druckpause statt Dual-Extrusion |
| Fabrication of a Soft Robotic Gripper With Integrated Strain Sensing Elements Using Multi-Material Additive Manufacturing | Georgopoulou, Vanderborght, Clemens, 2021 | Weicher Greifer mit integrierten TPU-Sensoren; Einfluss der Shore-Härte auf die Sensorempfindlichkeit | Multi-Material-Druck, Materialwahl |
| Fused Filament Fabrication of Piezoresistive Carbon Nanotubes Nanocomposites for Strain Monitoring | siehe PDF, 2020 | FFF-gedruckte CNT-Nanokomposite, Messfaktor bei Kriechen und Zyklen, zwei Druckmuster | Langzeitverhalten und Messfaktor |

## Hinweise

- Messfaktoren von leitfähigem PLA liegen in der Biegung meist nahe bei 1; Hysterese und Drift sind relevant. Eine Brückenschaltung mit Referenz-DMS hilft gegen Temperatureinfluss.
- Das Paper von Aliberti et al. untersucht ABS mit CNT und nicht PLA; die Aussage zum Rasterwinkel ist daher nur ein Hinweis.
- Die Titel wurden von den jeweiligen Seiten übernommen. Der vollständige Titel des Papers von Stano et al. ist hier lang und wurde im Dateinamen gekürzt (Windows-Pfadlänge).

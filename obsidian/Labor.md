---
topic: Lab equipment and test stand
date: 2026-11-17
tags:
  - forschungsprojekt
  - labor
---
# Labor B001 – available equipment
Back to [[Home]] · Photos in `pics/`, datasheets in `datasheets/`

## Equipment list
| Device | Purpose | Key data |
|---|---|---|
| **Raise3D Pro2** 3D printer | printing sensor, carrier, stand parts | dual extruder, filament 1.75 mm, nozzle 0.4 mm standard (0.2/0.6/0.8/1.0 available), nozzle ≤ 300 °C, bed ≤ 110 °C, build volume 305×305×300 mm (dual), slicer **ideaMaker**, STL/OBJ/3MF |
| **Protopasta conductive PLA** | sensor material | PLA + carbon black; resistivity ≈ 30 Ω·cm in the layer plane, ≈ 115 Ω·cm across layers (manufacturer values quoted by Maurizi et al.); details in [[Grundlagen]] |
| **GSV-3USB 2 mV/V** amplifier (ME-Meßsysteme) | bridge amplifier | 1 channel, 16 bit, sampling 10 kHz, data rate 1–1000 Hz, cut-off 1250 Hz, quarter/half/full bridge, internal bridge completion **350 Ω**, bridge supply **4.2 V**, input range **2 mV/V**, accuracy class 0.1 %, USB powered, 15-pin Sub-D |
| **Käfer MD12 T** digital dial gauge | displacement reference | range 12.5 mm, resolution 0.01 mm, max. error 10 µm ±1 digit, RS232/USB output |
| **Millimess** length gauge | displacement (analog to Käfer) | – |
| **Nema 17 stepper 17HS15-1504S-X1** | drive of the stand | – |
| **TB6600 driver (SBC-MD-TB6600)** | stepper driver | – |
| **Arduino Uno R3** | controller (alternative to STM32) | – |
| **Kraft-Weg-Messplatz** (old) | test stand | see below |

## The existing Kraft-Weg-Messplatz
Photo: `pics/Messplatz.jpeg`
- Aluminium base plate with a Nema 17 stepper driving a **lead screw**; the screw moves a carriage on a linear guide.
- Two 3D-printed clamps with screw-on clamping plates hold a **flat dog-bone specimen** in line with the screw → the stand loads the specimen axially (tension when the carriage moves away, compression when it moves towards the fixed clamp).
- A separate bracket on the plate probably holds the dial gauge.
- Labelled "Kraftsensor"; according to the Projektantrag it **no longer works** – to check: which part is broken (motor, driver, wiring, missing load cell?).
- There is **no reference load cell** on the stand → ordered a 10 kg load cell with HX711 (see [[Bestellung]]). 10 kg ≈ 98 N, i.e. just below the 100 N range → check overload capacity or use a 20 kg cell.

> [!todo] Measure on the stand
> Jaw width, clamping length, maximum free length between the jaws, screw positions and travel range. These values set the grip dimensions of the carrier in [[Implementation#3. Federkörper]].

## Lab rules
- Valid lab regulations apply; confirm in Moodle that you read them.
- Lab use only during exercise hours (Thursday 12:15–14:30).
- Electrical parts are ordered through the lab; no refunds for private purchases.

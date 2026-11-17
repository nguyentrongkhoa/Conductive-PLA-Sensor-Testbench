---
topic: Measuring circuit and amplifier
date: 2026-11-17
tags:
  - forschungsprojekt
  - elektronik
---
# Messschaltung
Back to [[Home]] · Related: [[Grundlagen]], [[Implementation]], [[Labor]]

## Numbers to design for
From the proposed geometry ([[Implementation]]):
- R0 ≈ **30–60 kΩ** per DMS (depends on effective resistivity; measure!)
- Strain at 100 N with two bonded DMS: ≈ **630 µm/m**
- ΔR/R0 at 100 N: 0.11 % (k = 1.7) … 0.52 % (k = 8.3) → ΔR ≈ 32–157 Ω on 30 kΩ
- Resolution 2 N = 2 % FS → **0.6–3 Ω** must be resolved, i.e. about 2·10⁻⁵ … 1·10⁻⁴ of R0.

## Options
| Circuit | Pro | Con | Used by |
|---|---|---|---|
| Voltage divider | simple, fine when ΔR is large, no offset problem | no temperature compensation, signal sits on a large DC level | Maurizi, Gooding |
| Quarter bridge (1 active + 3 fixed R) | zero output at rest | needs fixed R ≈ R0; no temp. compensation | Minetola |
| Half bridge active + dummy | **temperature compensation** | dummy must be identical | Lanzolla (dummy method) |
| **Full bridge, 2 active + 2 dummy** | temp. compensation **and** bending compensation, 2× signal | 4 printed DMS per sensor | recommended |
| Full bridge, all printed on one part | compact | layout effort | Jasper, Werkle |

## Recommended setup
```
          +Us (bridge supply)
           │
     ┌─────┴─────┐
   R1 active    R2 dummy
  (front face)  (unloaded coupon)
     │           │
  -Ud ●         ● +Ud   → amplifier
     │           │
   R4 dummy     R3 active
  (unloaded)    (back face)
     └─────┬─────┘
          -Us
```
- R1 and R3 = DMS on the front and back of the carrier (opposite bridge arms → their signals add; bending from eccentric clamping cancels).
- R2 and R4 = identical DMS glued on an **unloaded PLA coupon** next to the specimen (same temperature) → cancels temperature drift and creep that is not load-related.
- Output: $U_d/U_s \approx \frac{k}{4}(\varepsilon_1 + \varepsilon_3) = \frac{k\,\varepsilon}{2}$ → 0.54 mV/V (k = 1.7) … 2.6 mV/V (k = 8.3) at 100 N.

## Bridge design
- **Offset problem:** printed gauges scatter by about 5 % in R0 (Elgeneidy). 5 % mismatch in one arm gives ≈ **12.5 mV/V offset**, which is about 6× the GSV-3USB input range of 2 mV/V and larger than the useful signal. → Sort the printed DMS by measured R0 into matched sets, and add a **trimmer** (≈ 5–10 % of R0) between two arms for the zero balance.
- The ordered 261 Ω / 1.02 kΩ / 2 kΩ resistors and 1 k / 5 k trimmers do not match a 30–60 kΩ gauge (see [[Bestellung#Open points]]). For a quarter or half bridge you need fixed resistors ≈ R0 (0.1 %, low TC).
- **Self-heating:** with 4.2 V on a 30 kΩ half-arm, the current is ~70 µA and the power per gauge ~0.15 mW → negligible. Keep the supply ≤ 5 V (requirement 5.2).

## Amplifier / ADC options
**GSV-3USB (lab)**
- Input range 2 mV/V, bridge supply 4.2 V, 16 bit, internal bridge completion 350 Ω (only for 350 Ω quarter bridges, so not usable here).
- Use it in **full-bridge mode** with the external bridge above.
- Fits if k ≈ 2 (0.5–0.6 mV/V at 100 N); saturates if k ≈ 8 and the offset isn't trimmed. Check what the input does with a ~30 kΩ bridge source impedance.

**ADS1115 (ordered, 2 pcs)**
- 16 bit, I²C, PGA down to ±0.256 V FS → LSB ≈ 7.8 µV.
- Bridge with 3.3 V supply, k = 2: full scale ≈ 2 mV → only ~260 LSB → just enough for 2 % resolution, no margin. For a voltage divider the resolution is much worse, because the signal rides on a ~1.6 V level.
- Better: differential input on the bridge + averaging/oversampling (860 SPS max).

**HX711 (ordered with the 10 kg load cell)**
- 24 bit, gain 128 → made for load-cell bridges; with 5 V excitation the ±20 mV range is a good fit for our 2.7–13 mV signals.
- Option: use **one HX711 for the reference load cell and a second HX711 for the PLA bridge** (cheap, 10/80 Hz). Check settling time against t90 ≤ 500 ms (requirement 7.3).

**STM32 / Arduino Uno**
- Reads the ADC, drives the stepper (TB6600), logs the dial gauge (RS232/USB), sends CSV to the PC GUI.

## Temperature
- Two DS18B20 ordered: one on the specimen, one in the air → log with every measurement, correct residual drift.

## Wiring
- Lead and cable resistance (< 1 Ω) is negligible against 30 kΩ; the **contact resistance at the pads** dominates (requirement 6.2: ≤ 5 % of R0).
- Measure each DMS in **4-wire** mode (two wires per pad) when characterising R0 and the contact, to separate the contact resistance from the gauge.
- For the bridge, a 6-wire connection (sense lines) is only needed with long cables; Kreuzer circuit = amplifier-side solution (see [[Grundlagen#Lead resistance and wiring]]).

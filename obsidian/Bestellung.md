---
topic: Orders and costs
date: 2026-11-17
tags:
  - forschungsprojekt
  - bestellung
---
# Bestellung
Back to [[Home]] · Source: `project_management/Bestellscheine_Kraftsensor_PLA.xlsx` (all sheets status "in Arbeit"), prices as of 03.11.2026

## Roboter-Bausatz (anzado GmbH) – prices incl. 19 % VAT
| Item | Qty | Unit | Total | Purpose |
|---|---|---|---|---|
| ADS1115 4-channel ADC, 16 bit, I²C (RBS16519) | 2 | 3.89 € | 7.78 € | read the bridge / divider ([[Messschaltung]]) |
| HX711 + load cell 10 kg (RBS15858) | 1 | 3.39 € | 3.39 € | reference force for calibration |
| DS18B20 temperature sensor, waterproof, 1 m (RBS10137) | 2 | 1.94 € | 3.88 € | log temperature for drift correction |
| **Sum** | | | **15.05 €** (shipping still to add) | |

## RS Components – net prices
| Item | Qty | Total net | Purpose |
|---|---|---|---|
| Loctite EA 3430, 2K epoxy, 5 min, 24 ml (244-2021) | 1 | 21.70 € | main adhesive DMS → carrier |
| Loctite 401 cyanoacrylate, 5 g (258-5569) | 1 | 8.50 € | quick pre-tests |
| TE YR1B 261 Ω ±0.1 % 15 ppm/K, pack of 5 (754-8931) | 1 | 3.70 € (sheet; unit price 3.82 €) | bridge completion |
| TE YR1B 1.02 kΩ ±0.1 %, pack of 5 (755-1085) | 1 | 4.64 € | bridge completion |
| TE YR1B 2 kΩ ±0.1 %, pack of 10 (125-1200) | 1 | 4.02 € | bridge completion |
| Bourns 3296W 1 kΩ trimmer (521-9631) | 1 | 1.84 € | zero balance |
| Bourns 3296W 5 kΩ trimmer (521-9798) | 1 | 1.84 € | zero balance |
| Net 46.24 € + shipping 5 € + VAT 9.74 € | | **60.98 € gross** | |

## Totals
- Ordered/planned: 15.05 € + 60.98 € = **≈ 76 €** (+ shipping Roboter-Bausatz) of 200 €.
- Reichelt sheet: empty. Conrad sheet: contains only template leftovers (FilaExtruder, Robi, Digitalservo, Laborofen) with quantity 0 → clean up before submitting.
- Conductive PLA: available in the lab (Protopasta), so not ordered.

## Open points
> [!warning] Bridge resistors don't fit the sensor
> The printed DMS will have R0 ≈ 30–60 kΩ (see [[Implementation#Resistance estimate]], literature 4.5–275 kΩ). The ordered 261 Ω / 1.02 kΩ / 2 kΩ resistors and 1 k / 5 k trimmers are far too small to complete such a bridge. As the RS sheet already notes: **measure R0 of the first prints, then order matching 0.1 % resistors** (e.g. 33 kΩ or 47 kΩ, low TC) and a trimmer of about 5–10 % of R0. See [[Messschaltung#Bridge design]].
- **Conductive copper tape** was on the old wish list but is not in any order sheet. Decide after the contact tests in [[Kontaktierung und Kleben]].
- The fast cyanoacrylate the TU Darmstadt paper used is HBK Z70 (a strain gauge adhesive). Loctite 401 is the cheap substitute.
- Copper wire / thin stranded wire for the pads (probably in the lab).

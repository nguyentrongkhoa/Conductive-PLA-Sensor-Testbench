---
topic: Bonding the DMS and electrical contacting
date: 2026-11-17
tags:
  - forschungsprojekt
  - fertigung
---
# Kontaktierung und Kleben
Back to [[Home]] · Related: [[Implementation]], [[Bestellung]], risk R1 in [[Projektplanung]]

## Bonding the DMS to the carrier
**Use**
- **Loctite EA 3430 (2K epoxy, 5 min)** – main adhesive. Stiff, little creep, electrically insulating. Apply a **thin** layer and let it cure at room temperature.
- **Loctite 401 (cyanoacrylate)** – quick pre-tests. Closest to the HBK Z70 strain-gauge glue used by Chadda et al. (cures in ~1 min under thumb pressure).

**Avoid**
- Solvent-based glues (e.g. UHU Alleskleber): they dissolve PLA and change the resistance.
- Hot glue and double-sided tape: they **creep**, so the gauge doesn't follow the strain.

**Procedure (after Chadda et al.)**
1. Sand the bonding area on the carrier lightly (and the underside of the DMS substrate).
2. Clean with a solvent that doesn't attack PLA; Chadda used acetone, but **test on a scrap part first**, since acetone can soften some PLA blends. Isopropanol is the safe alternative.
3. Position the DMS with a printed **alignment jig** or alignment marks on the carrier (requirement 12.5: reproducible positioning). A clip-on jig is described in [[Implementation#5. Bonding jig]].
4. Thin adhesive layer, press with a flat silicone pad / thumb pressure, no adhesive on the pads.
5. Cure fully (EA 3430: handling time a few minutes, full strength much later – check datasheet) before loading.

## Electrical contacting – options to test (risk R1)
| Method | Source | Notes |
|---|---|---|
| **Copper wire melted into the pad** with a soldering iron | Chadda; Gooding (24 AWG, heated wire ends pushed into the tabs) | simple, low resistance; heat can deform a thin pad → use the thicker pad zone |
| **Thermal bonding with conductive PLA** (iron ≈ 350 °C, wire fused into pad with extra Protopasta) | Jasper | most stable and repeatable in that thesis |
| Conductive thread wound around the terminal + hot glue | Elgeneidy; planned in AP 3 | flexible; hot glue only for strain relief, not on the gauge |
| Metal pins pressed/melted into the pad | AP 3; Minetola | pins can tear out pieces of the pad when removed |
| Copper tape on the pad | old idea | **unstable** in Jasper (micro-movements between wire and tape) |
| Spring contacts / clamp in the stand | idea for requirement 12.3 (no soldering) | needs a defined contact force; check contact resistance drift |

**Acceptance:** contact resistance ≤ 5 % of R0 (requirement 6.2) and stable within ±0.1 % over 30 min → measure in **4-wire** mode (separate current and sense wires on each pad).

## Strain relief
- Fix the wires on the **grip zone** of the carrier (glue or cable tie), so cable forces don't pull on the pads.
- Route both wires to the same side; in the proposed DMS both pads sit at one end for that reason.

## Test plan for contacts
Do this before M4 (26.11.2026).
1. Print 3 contact coupons per method: a strip of Protopasta 30 × 4 × 0.3 mm with a pad at each end.
2. Make the contacts, measure 4-wire resistance (R_total) and 2-wire resistance → difference = contact + wire.
3. Repeat after 1 h, after 10 bending cycles by hand and the next day.
4. Pick the method with the lowest and most stable contact resistance.

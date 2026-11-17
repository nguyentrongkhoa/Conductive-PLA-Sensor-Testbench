---
topic: Theory – strain gauges and conductive PLA
date: 2026-11-17
tags:
  - forschungsprojekt
  - theorie
---
# Grundlagen
Back to [[Home]] · Books: Hoffmann, *An Introduction to Measurement using Strain Gauges* (HBM 1989); Keil, *Dehnungsmessstreifen* (Springer 2017)

## Resistance vs. resistivity
- **Resistivity ρ** (Ω·m) is a material property: how strongly the material itself opposes current. Independent of shape.
- **Resistance R** (Ω) belongs to a specific part and depends on material *and* geometry:
$$R = \rho \frac{L}{A}$$
  L = length of the current path, A = cross-section.
- In ANSYS ρ is the material input; R is the result from the geometry.

## Gauge factor
$$\frac{\Delta R}{R_0} = k \cdot \varepsilon$$
- Geometric part: length grows, cross-section shrinks → for metals k ≈ 2 (1 + 2ν).
- Material part: change of ρ under strain (piezoresistivity). In carbon-black PLA the conductive particle network is pulled apart/reorganised (percolation, tunnelling) → k can be larger than 2.
- Maurizi et al. write it as $GF = 2 - \Pi$, with Π the relative change of the number of conducting paths per strain; Π = 0 is metal-like behaviour.
- Values for Protopasta in the literature: k = 8.3 (Chadda, glued on steel), 1.7–3.2 (Maurizi, embedded in PLA beams), 0.4–1.3 (Jasper, PLA tensile/bending), 0.87 for an aerosol-jet silver sensor. **k depends strongly on geometry, printing and loading → must be measured.**

## Temperature
$$dR = k R_0 \left[\frac{dl}{l_0} + (\alpha - \beta)dT\right] + \gamma\,dT$$
(Maurizi et al.) α, β = thermal expansion of specimen and sensor, γ = temperature coefficient of resistance.
- If carrier and sensor have the same CTE (α = β), only γ remains → plain **PLA carrier** under Protopasta (requirement 6.1).
- γ is compensated with a **dummy gauge** (unloaded, same temperature) in the bridge (Lanzolla et al.) or corrected with the DS18B20 temperature reading.
- Maurizi found temperature effects negligible for dynamic measurements; for slow static loading they matter.

## Anisotropy from FDM printing
- Resistivity in the layer plane is lower than across the layers (≈ 30 vs. 115 Ω·cm for Protopasta) → print the grid **flat, in one plane**, with raster lines along the legs.
- Printing through several layers (steep build orientation) can make conductive paths separate under strain (Gooding et al.).
- Mechanical stiffness is also anisotropic (layer interfaces).

## Behaviour of conductive PLA under load
- **Creep/drift:** resistance keeps changing at constant load (Chadda: almost linear drift; cause: reorganisation of the particle network + viscoelastic PLA matrix).
- **Hysteresis:** loading and unloading curves differ; Gooding et al. measured 17–26 % on embedded graphene-PLA gauges. More end loops reduce it, thicker gauges increase it.
- **Repeated loading:** run a few full load cycles first to "settle" the sensor (Chadda: 3 cycles).
- **Elastic range only:** beyond the elastic limit of the carrier the gauge stops following the strain (Minetola & Giubilini).
- Compression vs. tension: under compression the particle network is pushed together → resistance drops (negative pressure coefficient in Hashemi Sanatgar et al.). The sign and size of k can differ between tension and compression → calibrate both if requirement 1.7 is pursued.

## Design rules taken from conventional strain gauges
- Meander grid with several legs parallel to the strain → long current path in a short gauge length.
- **End loops wider than the legs** → low resistance there → low transverse sensitivity (Hoffmann; Chadda).
- Gauge far from clamps and load introduction (St.-Venant), where strain is uniform (Chadda: 10 mm from the clamp).
- Thin carrier and thin adhesive layer → good strain transfer.
- Supply voltage as low as possible to avoid self-heating (requirement 5.2).

## Lead resistance and wiring
- Lead resistance in series with the gauge adds an error and its own temperature drift.
- Three-wire quarter bridge: lead resistances land in neighbouring bridge arms and cancel.
- **Kreuzer circuit / extended Kreuzer circuit** (HBM): the amplifier measures the voltage directly at the bridge, so cable resistance needs no correction; works for quarter, half and full bridges (Hoffmann 7.3).
- **Six-wire circuit:** sense lines measure the actual bridge supply; only for full bridges (Hoffmann 7.3.2, Keil 6.5).
- For a 30 kΩ PLA gauge, lead resistance (< 1 Ω) is negligible compared with the contact resistance at the pads → the critical point is the **contact**, not the cable. See [[Kontaktierung und Kleben]].

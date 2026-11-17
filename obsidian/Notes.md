---
topic:
date: 2026-10-15
tags:
---
- Sensor soll bei Raumteperatur funktionieren (20-30 Grad)
- Kraft-Weg-Messung
- Bis 100N an Kraft
- Ansys kann piezoresistive Simulationen durchführen
- [Ansys guide](https://ansyshelp.ansys.com/public/account/secured?returnurl=/views/secured/corp/v251/en/ans_thry/thy_coup3.html)
- FDM printing makes conductive PLA anisotropic—electrical conductivity and mechanical stiffness are different along the $Z$-axis (layer interface) compared to the $X/Y$ print plane
- What happens to conductive PLA under repeated loads?
- Conductive PLA and carrying material should have same thermal expansion coeff
- Kreuzer bridge better than Wheatstone
- Look at 3 4 6 wire measurements
- **Zweites leitfähiges Filament** (anderer Typ oder TPU) für einen Variantenvergleich mit t-Test???
- **Vermeide** lösungsmittelhaltige Kleber (z. B. UHU Alleskleber), die PLA anlösen und den Widerstand verändern können. Meide auch Heißkleber und doppelseitiges Klebeband, die kriechen
- **EA 3430 (Epoxid)** als Hauptkleber. Er ist steif, kriecht wenig und isoliert elektrisch. Tipp: Trage die Schicht dünn auf und lass sie bei Raumtemperatur aushärten.
- **Loctite 401 (Cyanacrylat)** für schnelle Vorversuche.
- Für **3D-Drucker**: prime tower im Setting aktivieren, sodass der 2. Nozzle nicht leakt
- **Dual extrusion**: Teile einzeln in CAD modellieren mit einem geteilten Ursprung (in Creo beide Teile auf einmal als .3mf exportieren im Assembly)
**Paper Dynamic Measurement using ...**
- 0,1mm Druckschicht, 220 und 225 Grad für PLA und Protopasta
- M-förmig, 0,8mm breit und 0,5mm dick (5 Schichten)
- E=3300 MPa, rho=1240kg/m3, 
- Voltage divider instead of Wheatstone, since strain is large
**Paper 3D-Printed Strain Gauge ...** (most useful paper so far)
- Linearitätsfehler 4%
- Empfindlichkeit 4-mal so hoch wie metal foil DMS
- Protopasta auf PLA und nochmal mit cold curing superglue mit Stahlplatte verbunden
- SG should be far from clamping edge (in this case 30mm from clamp, i.e 10mm from force application)
- Before glueing: sanding and acetone treatment
- Copper wires are melted into contact pads using soldering iron
- Has formulas for analytical calc
- Steel plate is loaded using universal testing machine
- DMM used to measure change in R
- Bass resistance of SG 18000 Ohm
- k=8,3 (Gauge Factor)
**3D Printed Strain Gauge Geometry and Orientation ...**
- Simulated change in resistance 44% higher than calculated, since poisson was neglected
- Average resistance 4.5K
- Inconsistent extrusion causes deviation between simulation and reality
- Adding end loops can decrease hysteresis errors
- Only 1 layer of SG (0.2mm)
- **0.6mm nozzle!!!** (maybe that's why they had inconsistent extrusion)
- FEM: coupled thermal-electrical-mechanical simulation: change in strain will be translated to change in resistance
- 3^3 factorial design
- use load frame to measure
- also use voltage divider and not wheatstone
- avg linearity error 5-6%, hysteresis 20%
**Paper Effect of Process Parameters ...**
- 2^3 factorial experiment with temp, ironing and infill
**Design of Experiments**
- Factors: strand width, no. of end loops, gauge length, distance to clamp spot, 
- Print factor: nozzle size & temp, bed temp, ironing
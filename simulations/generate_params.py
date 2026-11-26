"""

Constraints:
1. B_S <= ANS_W_FK <= B_S + 30        : Carrier at least as wide as substrate
2. B_S = L_A + L_E + L_START_LOOP + 5: substrate wider than strain gauge height by at least 5mm
3. L_S >= ((G_LEGS + B_GAUGE) * N_LEG) / 2 + 5         : subtrate longer than strain_gauge by at least 5mm
4. (N_LAYER+1)*H_LAYER <= T_S <= (N_LAYER+5)*H_LAYER         : substrate thicker than strain gauge by at least 1 print layer
5. 10 <= L_S + ANS_SUBSTRATE_OFFSET <= L_FK : substrate has to lie entirely in steel plate carrier and leave place for loading area (10mm)

Params:
1. N_LEG: even numbers between 4 and 20
2. B_GAUGE: real numbers between 2 and 10
3. G_LEGS: real numbers between 0.8 and 2
4. H_LAYER: real number and can be 0.15, 0.2, 0.3 or 0.4mm
5. N_LAYER: 2 3 4 5
6. L_A: real numbers between 10 and 50mm
7. L_E: real numbers between 1 and 10mm
8. L_START_LOOP: real number between 1 and 10mm
9. W: real number between 0.8 and 5
10. B_S: see constraints
11. L_S: see constraints
12: T_S: see constraints

"""
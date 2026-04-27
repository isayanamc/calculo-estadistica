"""
Módulo 3 - Optimización y Razones de Cambio Relacionadas
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

¿QUÉ ES LA OPTIMIZACIÓN?
──────────────────────────
Optimizar significa encontrar el valor MÁXIMO o MÍNIMO de una función
en un contexto real. Es una de las aplicaciones más importantes del
cálculo diferencial en ingeniería y ciencias.

En programación: minimizar tiempo de ejecución, maximizar rendimiento,
minimizar uso de memoria, etc.

PROCEDIMIENTO DE OPTIMIZACIÓN:
  1. Leer el problema e identificar QUÉ se quiere maximizar o minimizar
  2. Definir variables y escribir la función OBJETIVO f(x)
  3. Identificar la RESTRICCIÓN (si existe) y usarla para reducir variables
  4. Derivar f(x) e igualar a cero: f'(x) = 0  → puntos críticos
  5. Verificar con f''(x) si es máximo (f''<0) o mínimo (f''>0)
  6. Verificar los EXTREMOS del dominio (si hay un intervalo cerrado)
  7. Concluir con el valor óptimo y su interpretación

¿QUÉ SON LAS RAZONES DE CAMBIO RELACIONADAS?
──────────────────────────────────────────────
Cuando dos o más cantidades cambian con el tiempo y están relacionadas
por una ecuación, podemos derivar implícitamente respecto al tiempo t
para conectar sus tasas de cambio.

  Si A = f(r)  →  dA/dt = f'(r) · dr/dt

Ejemplo clásico: un globo esférico se infla. El radio r crece a 2 cm/s.
¿A qué velocidad crece el VOLUMEN cuando r = 5 cm?
  V = (4/3)πr³  →  dV/dt = 4πr² · dr/dt = 4π(25)(2) = 200π cm³/s
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x, t, r, h_var, b, l = symbols('x t r h b l', positive=True)

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Problemas de optimización
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  PROBLEMAS DE OPTIMIZACIÓN")
print("=" * 60)

# ── Problema 1: Área máxima con perímetro fijo ──
print("""
  PROBLEMA 1: Área máxima con perímetro fijo
  ───────────────────────────────────────────
  Se quiere cercar un terreno rectangular con 120 m de cerca.
  ¿Cuáles deben ser las dimensiones para maximizar el área?

  Variables:
    x = ancho,   y = largo
  Restricción (perímetro):
    2x + 2y = 120  →  y = 60 − x
  Función objetivo (área):
    A(x) = x · y = x(60 − x) = 60x − x²
""")

A = x * (60 - x)
Ap  = diff(A, x)
App = diff(Ap, x)
critico = solve(Ap, x)[0]
area_max = A.subs(x, critico)

print(f"  A(x)   = {A}")
print(f"  A'(x)  = {Ap}  →  igualando a 0: x = {critico}")
print(f"  A''(x) = {App}  < 0  →  es MÁXIMO")
print(f"  Ancho óptimo: x = {critico} m")
print(f"  Largo óptimo: y = {60 - critico} m")
print(f"  Área máxima:  A = {area_max} m²")
print(f"  Conclusión: el rectángulo óptimo es un CUADRADO de {critico}×{critico}")

# ── Problema 2: Caja de volumen máximo ──
print("""
  PROBLEMA 2: Caja de volumen máximo
  ────────────────────────────────────
  De una lámina cuadrada de 12 cm de lado se cortan cuadrados iguales
  en las esquinas y se dobla para formar una caja sin tapa.
  ¿Qué tamaño deben tener los cuadrados cortados para maximizar el volumen?

  Si cortamos cuadrados de lado x:
    Base de la caja: (12 − 2x) × (12 − 2x)
    Altura de la caja: x
  Función objetivo (volumen):
    V(x) = x(12 − 2x)²     con dominio: 0 < x < 6
""")

V = x * (12 - 2*x)**2
Vp  = diff(V, x)
Vpp = diff(Vp, x)
criticos_V = solve(Vp, x)
criticos_V_validos = [c for c in criticos_V if 0 < c < 6]

print(f"  V(x)  = {expand(V)}")
print(f"  V'(x) = {Vp}  →  factorizado: {factor(Vp)}")
print(f"  V'(x) = 0  →  x = {criticos_V}  (válido en (0,6): x = {criticos_V_validos})")

for c in criticos_V_validos:
    vol = V.subs(x, c)
    vpp_val = Vpp.subs(x, c)
    tipo = "MÁXIMO" if vpp_val < 0 else "MÍNIMO"
    print(f"  x = {c}:  V = {vol} cm³,  V''={vpp_val}  →  {tipo}")

# ── Problema 3: Distancia mínima a una curva ──
print("""
  PROBLEMA 3: Punto más cercano en una parábola
  ───────────────────────────────────────────────
  ¿Cuál es el punto de la parábola y = x² más cercano al punto (3, 0)?

  Distancia al cuadrado (se minimiza D² para simplificar):
    D²(x) = (x − 3)² + (x² − 0)² = (x−3)² + x⁴
""")

D2 = (x - 3)**2 + x**4
D2p = diff(D2, x)
print(f"  D²(x) = {D2}")
print(f"  (D²)'(x) = {D2p}")
sol_D = solve(D2p, x)
sol_real = [s for s in sol_D if im(s) == 0]
print(f"  Solución real: x ≈ {[round(float(s), 4) for s in sol_real]}")
for s in sol_real:
    xv = float(s)
    print(f"  Punto más cercano: ({round(xv,4)}, {round(xv**2,4)})")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Razones de cambio relacionadas
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  RAZONES DE CAMBIO RELACIONADAS")
print("=" * 60)
print("""
  Técnica: derivación implícita respecto al tiempo t.
  Si una ecuación relaciona dos variables que dependen de t,
  derivamos ambos lados respecto a t usando la regla de la cadena.

  Notación: dx/dt = tasa de cambio de x respecto al tiempo
""")

# ── Razón de cambio 1: Globo esférico ──
print("  EJEMPLO 1: Globo esférico que se infla")
print("  ─────────────────────────────────────────")
print("""
  V = (4/3)πr³

  Derivando respecto a t:
    dV/dt = 4πr² · dr/dt

  Dato: dr/dt = 2 cm/s   (el radio crece 2 cm por segundo)
  ¿Cuánto crece el volumen cuando r = 5 cm?
""")
r_val = 5
drdt  = 2
dVdt  = 4 * np.pi * r_val**2 * drdt
print(f"  dV/dt = 4π({r_val})²({drdt}) = 4π({r_val**2})({drdt}) = {round(dVdt, 4)} cm³/s")
print(f"  ≈ {round(dVdt, 2)} cm³/s  cuando r = {r_val} cm\n")

# ── Razón de cambio 2: Escalera deslizante ──
print("  EJEMPLO 2: Escalera deslizante")
print("  ─────────────────────────────────────────")
print("""
  Una escalera de 10 m apoyada en una pared.
  La base se aleja de la pared a 0.5 m/s.
  ¿Qué tan rápido baja el extremo superior cuando la base está a 6 m?

  Relación (Pitágoras):  x² + y² = 100
  Derivando respecto a t:
    2x(dx/dt) + 2y(dy/dt) = 0
    dy/dt = −(x/y) · dx/dt
""")
xv_val = 6
yv_val = np.sqrt(100 - xv_val**2)
dxdt   = 0.5
dydt   = -(xv_val / yv_val) * dxdt
print(f"  x = {xv_val} m  →  y = √(100−36) = √64 = {round(yv_val, 4)} m")
print(f"  dy/dt = −({xv_val}/{round(yv_val,4)}) · {dxdt} = {round(dydt, 4)} m/s")
print(f"  El extremo superior BAJA a {abs(round(dydt,4))} m/s\n")

# ── Razón de cambio 3: Sombra en movimiento ──
print("  EJEMPLO 3: Sombra de una persona caminando")
print("  ─────────────────────────────────────────")
print("""
  Un poste de luz de 6 m de alto. Una persona de 1.8 m
  camina alejándose a 1.5 m/s.
  ¿Con qué velocidad crece la longitud de su sombra?

  Por semejanza de triángulos:
    6 / (x + s) = 1.8 / s
    6s = 1.8(x + s)
    4.2s = 1.8x  →  s = (3/7)x

  Derivando: ds/dt = (3/7) · dx/dt
""")
dxdt_sombra = 1.5
dsdt = (3/7) * dxdt_sombra
print(f"  ds/dt = (3/7) · {dxdt_sombra} = {round(dsdt, 4)} m/s")
print(f"  La sombra crece a {round(dsdt, 4)} m/s\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Visualización
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Módulo 3 — Optimización y Razones de Cambio Relacionadas",
             fontsize=14, fontweight='bold')

# ── Área del rectángulo ──
ax = axes[0, 0]
xv = np.linspace(0, 60, 400)
Av = xv * (60 - xv)
ax.plot(xv, Av, color='#1565C0', lw=2.5)
ax.scatter([30], [900], color='red', zorder=5, s=100,
           label="Máximo: x=30, A=900 m²")
ax.axvline(30, color='red', ls='--', lw=1.5, alpha=0.7)
ax.set_title("Área del rectángulo\n2x+2y=120, maximizar A=xy", fontsize=9)
ax.set_xlabel("Ancho x (m)"); ax.set_ylabel("Área A (m²)")
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

# ── Volumen de la caja ──
ax = axes[0, 1]
xv2 = np.linspace(0.01, 5.99, 300)
Vv  = xv2 * (12 - 2*xv2)**2
ax.plot(xv2, Vv, color='#C62828', lw=2.5)
x_opt = float(criticos_V_validos[0])
v_opt = float(V.subs(x, x_opt))
ax.scatter([x_opt], [v_opt], color='red', zorder=5, s=100,
           label=f"Máximo: x={round(x_opt,2)}, V={round(v_opt,2)}")
ax.axvline(x_opt, color='red', ls='--', lw=1.5, alpha=0.7)
ax.set_title("Volumen de la caja\nV(x) = x(12−2x)²", fontsize=9)
ax.set_xlabel("Lado cortado x (cm)"); ax.set_ylabel("Volumen V (cm³)")
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

# ── Caja 3D (esquemática) ──
ax = axes[0, 2]
ax.set_aspect('equal')
lado = 12
xc = float(criticos_V_validos[0])
# Lámina original
cuadrado = plt.Polygon([[0,0],[lado,0],[lado,lado],[0,lado]],
                        fill=False, edgecolor='gray', lw=1.5, ls='--')
ax.add_patch(cuadrado)
# Esquinas cortadas
esquinas = [(0,0),(xc,0),(xc,xc),(0,xc)]
for ex, ey in [(0,0),(lado-xc,0),(lado-xc,lado-xc),(0,lado-xc)]:
    sq = plt.Polygon([[ex,ey],[ex+xc,ey],[ex+xc,ey+xc],[ex,ey+xc]],
                      facecolor='#FFCDD2', edgecolor='red', lw=1.5)
    ax.add_patch(sq)
# Base de la caja
base = plt.Polygon([[xc,xc],[lado-xc,xc],[lado-xc,lado-xc],[xc,lado-xc]],
                    facecolor='#BBDEFB', edgecolor='blue', lw=2)
ax.add_patch(base)
ax.annotate(f"x={round(xc,2)}", (xc/2, xc/2), ha='center', va='center',
            fontsize=8, color='red')
ax.annotate(f"Base\n{round(12-2*xc,2)}×{round(12-2*xc,2)}", (6,6),
            ha='center', va='center', fontsize=8, color='blue')
ax.set_xlim(-0.5, 12.5); ax.set_ylim(-0.5, 12.5)
ax.set_title("Lámina con esquinas cortadas\n(azul = base de la caja)", fontsize=9)
ax.axis('off')

# ── Globo esférico: dV/dt vs r ──
ax = axes[1, 0]
rv = np.linspace(0, 10, 200)
dVdt_v = 4 * np.pi * rv**2 * 2   # dr/dt = 2
ax.plot(rv, dVdt_v, color='#2E7D32', lw=2.5)
ax.scatter([5], [4*np.pi*25*2], color='red', zorder=5, s=100,
           label=f"r=5: dV/dt≈{round(4*np.pi*25*2,2)}")
ax.set_title("Globo esférico\ndV/dt = 4πr² · dr/dt  (dr/dt=2 cm/s)", fontsize=9)
ax.set_xlabel("Radio r (cm)"); ax.set_ylabel("dV/dt (cm³/s)")
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

# ── Escalera deslizante ──
ax = axes[1, 1]
xv3 = np.linspace(0.1, 9.9, 300)
yv3 = np.sqrt(100 - xv3**2)
dydt_v = -(xv3 / yv3) * 0.5
ax.plot(xv3, dydt_v, color='#6A1B9A', lw=2.5)
ax.scatter([6], [dydt], color='red', zorder=5, s=100,
           label=f"x=6: dy/dt={round(dydt,4)} m/s")
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Escalera deslizante\ndy/dt = −(x/y)·dx/dt", fontsize=9)
ax.set_xlabel("Base x (m)"); ax.set_ylabel("dy/dt (m/s)")
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

# ── Diagrama escalera ──
ax = axes[1, 2]
ax.set_aspect('equal')
xpos, ypos = 6, 8   # posición actual
ax.plot([0, 0], [0, 10], color='gray', lw=4, label="Pared")
ax.plot([0, 10], [0, 0], color='brown', lw=3, label="Suelo")
ax.plot([xpos, 0], [0, ypos], color='#1565C0', lw=3, label="Escalera (10m)")
ax.annotate("", (xpos+0.5,0), (xpos,0),
            arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax.text(xpos+0.6, 0.3, "dx/dt=0.5 m/s", fontsize=8, color='red')
ax.annotate("", (0,ypos-0.5), (0,ypos),
            arrowprops=dict(arrowstyle='->', color='purple', lw=2))
ax.text(0.2, ypos-0.8, f"dy/dt={round(dydt,3)} m/s", fontsize=8, color='purple')
ax.text(xpos/2+0.3, ypos/2, "10 m", fontsize=9, color='#1565C0')
ax.text(xpos/2, -0.5, f"x={xpos} m", fontsize=9, ha='center')
ax.text(-0.6, ypos/2, f"y={round(ypos,2)}m", fontsize=9, ha='center')
ax.set_xlim(-1.5, 11); ax.set_ylim(-1, 11)
ax.set_title("Diagrama — Escalera deslizante", fontsize=9)
ax.legend(fontsize=7, loc='upper right'); ax.axis('off')

plt.tight_layout()
plt.savefig("optimizacion_razones_cambio.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: optimizacion_razones_cambio.png")

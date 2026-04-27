"""
Módulo 2 - Definición de Derivada en un Punto
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

¿QUÉ ES LA DERIVADA?
─────────────────────
La derivada mide la TASA DE CAMBIO INSTANTÁNEA de una función.
Intuitivamente: ¿qué tan rápido está cambiando f(x) exactamente en x = a?

Para entenderlo, partimos de la tasa de cambio PROMEDIO entre dos puntos:
    tasa promedio = [f(a+h) - f(a)] / h      (pendiente de la secante)

Cuando hacemos h → 0, los dos puntos se acercan hasta coincidir,
y la secante se convierte en la RECTA TANGENTE.
Ese límite es la derivada:

    f'(a) = lim h→0  [f(a+h) - f(a)] / h

Si ese límite existe, decimos que f es DERIVABLE en x = a.

INTERPRETACIONES:
  • Geométrica:  f'(a) es la pendiente de la recta tangente en (a, f(a))
  • Física:      si f(t) es posición, entonces f'(t) es velocidad instantánea
  • General:     f'(a) indica cuánto cambia f por cada unidad que cambia x
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x, h = symbols('x h')

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Derivada por definición (límite del cociente)
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  DERIVADA POR DEFINICIÓN")
print("=" * 60)
print("""
  Fórmula:  f'(a) = lim h→0  [f(a+h) - f(a)] / h

  Procedimiento:
    1) Calcular f(x+h) sustituyendo x por (x+h) en f
    2) Restar f(x) y dividir entre h
    3) Simplificar la expresión algebraicamente
    4) Tomar el límite cuando h → 0
""")

def derivada_por_definicion(f_expr, punto, nombre):
    f_mas_h = f_expr.subs(x, x + h)
    cociente = (f_mas_h - f_expr) / h
    cociente_simplificado = simplify(cociente)
    derivada = limit(cociente_simplificado, h, 0)

    print(f"  ┌─ f(x) = {nombre}")
    print(f"  │  Paso 1 — f(x+h) = {expand(f_mas_h)}")
    print(f"  │  Paso 2 — [f(x+h)-f(x)]/h = {cociente_simplificado}")
    print(f"  │  Paso 3 — lim h→0 = {derivada}   ← esta es f'(x)")
    if punto is not None:
        val = derivada.subs(x, punto)
        print(f"  └  f'({punto}) = {val}   ← pendiente de la tangente en x={punto}")
    print()
    return derivada

funciones = [
    (x**2,     2, "x²      → esperamos f'(x) = 2x"),
    (x**3,     1, "x³      → esperamos f'(x) = 3x²"),
    (sqrt(x),  4, "√x      → esperamos f'(x) = 1/(2√x)"),
    (1/x,      3, "1/x     → esperamos f'(x) = -1/x²"),
]

for f_expr, punto, nombre in funciones:
    derivada_por_definicion(f_expr, punto, nombre)

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Recta tangente
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  RECTA TANGENTE EN UN PUNTO")
print("=" * 60)
print("""
  Una vez que tenemos f'(a), la ecuación de la recta tangente
  en el punto (a, f(a)) se construye con la fórmula punto-pendiente:

      y - f(a) = f'(a) · (x - a)
      y = f'(a)·x + [f(a) - f'(a)·a]

  La pendiente m = f'(a) nos dice:
    • m > 0 → la función SUBE en ese punto
    • m < 0 → la función BAJA en ese punto
    • m = 0 → posible máximo, mínimo o punto de inflexión
""")

def recta_tangente(f_expr, punto, nombre):
    fp = diff(f_expr, x)
    m  = fp.subs(x, punto)
    y0 = f_expr.subs(x, punto)
    tangente = m * (x - punto) + y0

    print(f"  f(x) = {nombre}  en  x = {punto}")
    print(f"    f'(x) = {fp}")
    print(f"    Pendiente:  m = f'({punto}) = {m}")
    print(f"    Punto:      ({punto}, {y0})")
    print(f"    Recta tangente: y = {expand(tangente)}")
    print()

recta_tangente(x**2,   2,    "x²")
recta_tangente(sin(x), pi/4, "sin(x)")
recta_tangente(exp(x), 0,    "eˣ")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Continuidad y derivabilidad
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  CONTINUIDAD Y DERIVABILIDAD")
print("=" * 60)
print("""
  Teorema: Si f es derivable en x=a  →  f es continua en x=a
  El RECÍPROCO ES FALSO: hay funciones continuas NO derivables.

  Esto ocurre cuando la gráfica tiene:
    • Esquina o pico:     las pendientes laterales son distintas
    • Tangente vertical:  la pendiente tiende a infinito

  Cómo verificarlo — calculamos las derivadas LATERALES:
    f'⁻(a) = lim h→0⁻  [f(a+h)-f(a)]/h
    f'⁺(a) = lim h→0⁺  [f(a+h)-f(a)]/h
  Si f'⁻(a) ≠ f'⁺(a)  →  NO derivable en x=a
""")

f_abs = Abs(x)
lim_izq = limit((f_abs.subs(x, 0+h) - 0)/h, h, 0, '-')
lim_der = limit((f_abs.subs(x, 0+h) - 0)/h, h, 0, '+')
print(f"  Ejemplo 1: f(x) = |x|  en x = 0")
print(f"    Derivada izquierda: lim h→0⁻  |h|/h = {lim_izq}")
print(f"    Derivada derecha:   lim h→0⁺  |h|/h = {lim_der}")
print(f"    {lim_izq} ≠ {lim_der}  →  NO derivable  (esquina)\n")

print(f"  Ejemplo 2: f(x) = x^(1/3)  en x = 0")
lim_cbrt = limit(x**Rational(1,3) / x, x, 0)
print(f"    lim h→0  h^(1/3)/h = lim h→0  h^(-2/3) = {lim_cbrt}")
print(f"    El límite es ∞  →  NO derivable  (tangente vertical)\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 4: Visualización
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Módulo 2 — Definición de Derivada y Recta Tangente",
             fontsize=14, fontweight='bold')

colores = ['#1565C0', '#C62828', '#2E7D32']

datos_plot = [
    (lambda xv: xv**2,
     lambda xv: 4*xv - 4,
     2, "f(x) = x²", "y=4x-4 (tangente)", (-1, 4)),
    (lambda xv: np.sin(xv),
     lambda xv: (np.sqrt(2)/2)*(xv - np.pi/4) + np.sqrt(2)/2,
     np.pi/4, "f(x) = sin(x)", "tangente en x=π/4", (-1, 4)),
    (lambda xv: np.exp(xv),
     lambda xv: xv + 1,
     0, "f(x) = eˣ", "y=x+1 (tangente)", (-2, 2)),
]

for i, (f_num, tang_num, pto, nombre_f, nombre_t, xlim) in enumerate(datos_plot):
    ax = axes[0, i]
    xv = np.linspace(xlim[0], xlim[1], 300)
    ax.plot(xv, f_num(xv), color=colores[i], lw=2.5, label=nombre_f)
    ax.plot(xv, tang_num(xv), color='orange', lw=2, ls='--', label=nombre_t)
    ax.scatter([pto], [f_num(pto)], color='black', zorder=5, s=80,
               label=f"Punto ({round(pto,2)}, {round(f_num(pto),2)})")
    ax.set_title(f"Tangente en x = {round(pto, 3)}", fontsize=9)
    ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_ylim(-2, min(10, max(f_num(xv)) + 1))

# Secantes → Tangente
ax = axes[1, 0]
xv4 = np.linspace(0, 4, 300)
ax.plot(xv4, xv4**2, color=colores[0], lw=2.5, zorder=5, label="f(x) = x²")
for hv, color in zip([1.5, 0.8, 0.3, 0.05],
                      ['#E53935', '#FB8C00', '#FDD835', '#1B5E20']):
    m_sec = ((2 + hv)**2 - 4) / hv
    xs = np.linspace(1.2, 2 + hv + 0.3, 100)
    ax.plot(xs, m_sec*(xs-2)+4, color=color, lw=1.8, alpha=0.85, label=f"secante h={hv}")
xt = np.linspace(1, 3.5, 100)
ax.plot(xt, 4*(xt-2)+4, color='black', lw=2, ls='--', label="tangente (h→0)")
ax.scatter([2], [4], color='black', zorder=6, s=80)
ax.set_title("Secantes → Tangente\n(visualización del límite)", fontsize=9)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_ylim(-1, 12); ax.set_xlim(0, 4)

# |x| no derivable
ax = axes[1, 1]
xv5 = np.linspace(-2, 2, 300)
ax.plot(xv5, np.abs(xv5), color=colores[0], lw=2.5, label="|x|  (continua)")
ax.scatter([0], [0], color='red', zorder=5, s=100)
ax.annotate("Esquina:\nf'⁻ = −1, f'⁺ = +1",
            (0, 0), textcoords="offset points", xytext=(25, 20),
            fontsize=8, color='red',
            arrowprops=dict(arrowstyle='->', color='red'))
ax.set_title("|x| — Continua pero NO derivable en x=0", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")

# x^(1/3) tangente vertical
ax = axes[1, 2]
xv6 = np.linspace(-2, 2, 500)
ax.plot(xv6, np.cbrt(xv6), color=colores[2], lw=2.5, label="x^(1/3)  (continua)")
ax.axvline(0, color='red', ls='--', lw=1.8, label="Tangente vertical (pendiente=∞)")
ax.scatter([0], [0], color='red', zorder=5, s=100)
ax.annotate("Pendiente → ∞",
            (0, 0), textcoords="offset points", xytext=(20, -35),
            fontsize=8, color='red',
            arrowprops=dict(arrowstyle='->', color='red'))
ax.set_title("x^(1/3) — Continua pero NO derivable en x=0", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")

plt.tight_layout()
plt.savefig("definicion_derivada.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: definicion_derivada.png")

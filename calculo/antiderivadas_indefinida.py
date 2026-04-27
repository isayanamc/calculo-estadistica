"""
Módulo 4 - Antiderivadas e Integración Indefinida
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

¿QUÉ ES UNA ANTIDERIVADA?
──────────────────────────
Si la derivada es el proceso de "descomponer" una función para ver
cómo cambia, la ANTIDERIVADA es el proceso INVERSO: dado f'(x),
¿cuál es la función f(x) original?

Formalmente: F(x) es antiderivada de f(x) si  F'(x) = f(x)

Ejemplo:
  f(x) = 2x   →   F(x) = x²   porque  d/dx[x²] = 2x ✓

IMPORTANTE — La constante de integración C:
  La antiderivada NO es única. Si F'(x) = f(x), entonces
  también [F(x) + C]' = f(x) para cualquier constante C.
  Esto es porque la derivada de una constante es 0.

  Por eso escribimos:  ∫ f(x) dx = F(x) + C

  La C representa TODA la familia de antiderivadas posibles.
  Es como decir: "no sabemos cuánto vale la función en x=0,
  solo sabemos cómo cambia".

NOTACIÓN DE LA INTEGRAL INDEFINIDA:
  ∫ f(x) dx = F(x) + C

  Donde:
    ∫       = símbolo de integral (S alargada, de "Summa")
    f(x)    = integrando (la función que integramos)
    dx      = diferencial (respecto a qué variable)
    F(x)+C  = familia de antiderivadas

TABLA DE INTEGRALES FUNDAMENTALES:
  ∫ xⁿ dx       = xⁿ⁺¹/(n+1) + C    (n ≠ −1)
  ∫ 1/x dx      = ln|x| + C
  ∫ eˣ dx       = eˣ + C
  ∫ aˣ dx       = aˣ/ln(a) + C
  ∫ sin(x) dx   = −cos(x) + C
  ∫ cos(x) dx   = sin(x) + C
  ∫ sec²(x) dx  = tan(x) + C
  ∫ 1/(1+x²) dx = arctan(x) + C
  ∫ 1/√(1−x²) dx = arcsin(x) + C
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = symbols('x')

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Verificación de antiderivadas
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  VERIFICACIÓN DE ANTIDERIVADAS")
print("=" * 60)
print("""
  Para verificar que F(x) es antiderivada de f(x):
  simplemente derivamos F(x) y comprobamos que da f(x).
""")

pares = [
    (2*x,           x**2,            "2x",       "x²"),
    (x**3,          x**4/4,          "x³",       "x⁴/4"),
    (cos(x),        sin(x),          "cos(x)",   "sin(x)"),
    (exp(x),        exp(x),          "eˣ",       "eˣ"),
    (1/x,           log(x),          "1/x",      "ln|x|"),
    (1/(1+x**2),    atan(x),         "1/(1+x²)", "arctan(x)"),
]

print(f"  {'f(x)':<16} {'F(x)':<16} {'F′(x)':<16} {'¿F′=f?'}")
print(f"  {'─'*58}")
for f_expr, F_expr, nombre_f, nombre_F in pares:
    Fp = diff(F_expr, x)
    ok = simplify(Fp - f_expr) == 0
    print(f"  {nombre_f:<16} {nombre_F:<16} {str(simplify(Fp)):<16} "
          f"{'✅' if ok else '❌'}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Tabla de integrales fundamentales
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  INTEGRALES INDEFINIDAS FUNDAMENTALES")
print("=" * 60)
print("""
  Calculadas con SymPy. Recuerda siempre agregar + C al resultado.
  La regla de la potencia ∫xⁿdx = xⁿ⁺¹/(n+1)+C NO aplica para n=-1.
""")

integrales = [
    (x**4,              "x⁴"),
    (x**Rational(3,2),  "x^(3/2)"),
    (1/x**2,            "x⁻²"),
    (sqrt(x),           "√x"),
    (exp(x),            "eˣ"),
    (exp(3*x),          "e^(3x)"),
    (2**x,              "2ˣ"),
    (1/x,               "1/x"),
    (log(x),            "ln(x)"),
    (sin(x),            "sin(x)"),
    (cos(x),            "cos(x)"),
    (tan(x),            "tan(x)"),
    (sec(x)**2,         "sec²(x)"),
    (1/(1 + x**2),      "1/(1+x²)"),
    (1/sqrt(1 - x**2),  "1/√(1−x²)"),
]

print(f"  {'∫ f(x) dx':<22} {'= F(x) + C'}")
print(f"  {'─'*50}")
for f_expr, nombre in integrales:
    try:
        F = integrate(f_expr, x)
        print(f"  ∫ {nombre:<20} = {F} + C")
    except Exception:
        print(f"  ∫ {nombre:<20} = (no elemental)")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Propiedades de linealidad
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  PROPIEDADES DE LINEALIDAD")
print("=" * 60)
print("""
  La integral es un operador LINEAL, lo que significa:

  1) Constante multiplicativa:
       ∫ k·f(x) dx = k · ∫ f(x) dx

  2) Suma/resta de funciones:
       ∫ [f(x) ± g(x)] dx = ∫ f(x) dx ± ∫ g(x) dx

  Esto nos permite integrar polinomios término por término.
""")

polinomios = [
    (3*x**2 + 2*x - 5,         "3x² + 2x − 5"),
    (4*x**3 - 6*x**2 + 1,      "4x³ − 6x² + 1"),
    (2*sin(x) + 3*cos(x),      "2·sin(x) + 3·cos(x)"),
    (exp(x) - 1/x,             "eˣ − 1/x"),
]

for f_expr, nombre in polinomios:
    F = integrate(f_expr, x)
    print(f"  ∫ ({nombre}) dx")
    print(f"       = {F} + C")
    # Verificación
    verif = simplify(diff(F, x) - f_expr) == 0
    print(f"       Verificación: F'(x) = f(x)? {'✅' if verif else '❌'}\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 4: Visualización — familia de antiderivadas
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Módulo 4 — Antiderivadas e Integración Indefinida",
             fontsize=14, fontweight='bold')

xv = np.linspace(-3, 3, 300)

# ── Familia de antiderivadas de 2x ──
ax = axes[0]
ax.plot(xv, 2*xv, color='black', lw=3, label="f(x) = 2x  (integrando)", zorder=5)
colores_c = ['#E53935', '#1565C0', '#2E7D32', '#6A1B9A', '#E65100']
for i, C_val in enumerate([-4, -2, 0, 2, 4]):
    F_vals = xv**2 + C_val
    ax.plot(xv, F_vals, color=colores_c[i], lw=1.8, ls='--',
            label=f"F(x) = x² + ({C_val})")
ax.axhline(0, color='gray', lw=0.8)
ax.set_title("Familia de antiderivadas de 2x\n∫2x dx = x² + C", fontsize=10)
ax.legend(fontsize=7, loc='upper left')
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_ylim(-8, 12); ax.grid(True, alpha=0.3)

# ── La constante C desplaza verticalmente ──
ax = axes[1]
for i, C_val in enumerate([-3, -1, 0, 1, 3]):
    F_vals = np.sin(xv) + C_val
    ax.plot(xv, F_vals, color=colores_c[i], lw=2,
            label=f"−cos(x) + {C_val}")
ax.set_title("Familia de antiderivadas de sin(x)\n∫sin(x) dx = −cos(x) + C",
             fontsize=10)
ax.legend(fontsize=7)
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.grid(True, alpha=0.3)

# ── Verificación gráfica: F'(x) = f(x) ──
ax = axes[2]
F_vals = xv**3/3 - xv
f_vals = xv**2 - 1    # derivada de x³/3 − x
ax.plot(xv, F_vals, color='#1565C0', lw=2.5, label="F(x) = x³/3 − x  (antiderivada)")
ax.plot(xv, f_vals, color='#C62828', lw=2, ls='--',
        label="f(x) = x² − 1  (integrando)")
ax.axhline(0, color='gray', lw=0.8)
# Marcar donde f=0 (extremos de F)
ax.scatter([-1, 1], [F_vals[np.argmin(np.abs(xv+1))],
                     F_vals[np.argmin(np.abs(xv-1))]],
           color='green', zorder=5, s=80,
           label="f=0 → extremos de F")
ax.set_title("Verificación gráfica: F'(x)=f(x)\nDonde f=0 → extremos de F",
             fontsize=10)
ax.legend(fontsize=7)
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_ylim(-3, 3); ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("antiderivadas_indefinida.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: antiderivadas_indefinida.png")

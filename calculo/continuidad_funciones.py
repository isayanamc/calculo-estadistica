"""
Módulo 1 - Continuidad de Funciones
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

Temas cubiertos:
  - Definición de continuidad (3 condiciones)
  - Discontinuidades: removible, de salto, esencial
  - Teorema del Valor Intermedio (TVI)
  - Verificación algebraica con SymPy
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sympy import *

x = symbols('x')

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Verificación de continuidad (3 condiciones)
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  VERIFICACIÓN DE CONTINUIDAD EN UN PUNTO")
print("=" * 60)
print("""
  Una función f es CONTINUA en x = a si:
    1) f(a) está definida
    2) lim x→a  f(x) existe
    3) lim x→a  f(x) = f(a)
""")

def verificar_continuidad(f_expr, punto, nombre_f="f"):
    """Verifica las 3 condiciones de continuidad en x = punto."""
    print(f"  f(x) = {nombre_f}  en x = {punto}")
    print(f"  {'─'*45}")

    # Condición 1
    try:
        val = f_expr.subs(x, punto)
        val_simplificado = simplify(val)
        c1 = val_simplificado.is_finite
        print(f"    1) f({punto}) = {val_simplificado}  →  {'✓ definida' if c1 else '✗ no definida'}")
    except Exception:
        c1 = False
        print(f"    1) f({punto}) no definida  →  ✗")

    # Condición 2
    lim_val = limit(f_expr, x, punto)
    c2 = lim_val.is_finite
    print(f"    2) lim x→{punto} f(x) = {lim_val}  →  {'✓ existe' if c2 else '✗ no existe'}")

    # Condición 3
    if c1 and c2:
        c3 = simplify(val_simplificado - lim_val) == 0
        print(f"    3) f({punto}) = lim?  →  {'✓ iguales' if c3 else '✗ distintos'}")
        es_continua = c3
    else:
        es_continua = False

    print(f"    → Conclusión: {'CONTINUA ✅' if es_continua else 'DISCONTINUA ❌'}")
    print()
    return es_continua

# Caso 1: continua en x=2
f1 = x**2 - 3*x + 2
verificar_continuidad(f1, 2, "x²-3x+2")

# Caso 2: discontinuidad removible en x=1
f2 = (x**2 - 1)/(x - 1)
verificar_continuidad(f2, 1, "(x²-1)/(x-1)")

# Caso 3: continua por partes — definida manualmente
print("  f(x) = (x²-1)/(x-1)  si x≠1,  f(1)=2  →  CORREGIDA")
f2_corregida = Piecewise(((x**2-1)/(x-1), Ne(x, 1)), (2, True))
lim_c = limit(f2_corregida, x, 1)
val_c = f2_corregida.subs(x, 1)
print(f"    lim x→1 = {lim_c},  f(1) = {val_c}  →  CONTINUA ✅\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Tipos de discontinuidades
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  TIPOS DE DISCONTINUIDADES")
print("=" * 60)

discontinuidades = [
    ((x**2-1)/(x-1),      1,  "Removible",  "(x²-1)/(x-1)  en x=1"),
    (Piecewise((x+1, x < 2), (x-1, True)), 2,  "Salto",      "f(x) por partes  en x=2"),
    (1/(x-3),             3,  "Esencial",   "1/(x-3)  en x=3"),
]

for f_expr, punto, tipo, nombre in discontinuidades:
    lim_izq = limit(f_expr, x, punto, '-')
    lim_der = limit(f_expr, x, punto, '+')
    print(f"\n  {nombre}  →  Discontinuidad {tipo}")
    print(f"    lim⁻ = {lim_izq}   |   lim⁺ = {lim_der}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Teorema del Valor Intermedio
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  TEOREMA DEL VALOR INTERMEDIO (TVI)")
print("=" * 60)
print("""
  Si f es continua en [a, b] y k está entre f(a) y f(b),
  entonces ∃ c ∈ (a, b) tal que f(c) = k.
""")

f_tvi = x**3 - x - 2
a_tvi, b_tvi = 1, 2
fa = f_tvi.subs(x, a_tvi)
fb = f_tvi.subs(x, b_tvi)
raiz = solve(f_tvi, x)
raiz_real = [r for r in raiz if im(r) == 0]

print(f"  f(x) = x³ - x - 2  en  [{a_tvi}, {b_tvi}]")
print(f"  f({a_tvi}) = {fa}  (negativo)")
print(f"  f({b_tvi}) = {fb}  (positivo)")
print(f"  Como los signos son opuestos, ∃ raíz en ({a_tvi}, {b_tvi})")
print(f"  Raíz exacta: x = {[simplify(r) for r in raiz_real]}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 4: Visualización
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Módulo 1 — Continuidad de Funciones",
             fontsize=14, fontweight='bold')

colores = ['#1565C0', '#C62828', '#2E7D32', '#6A1B9A']

# ── Gráfica 1: discontinuidad removible ──
ax = axes[0, 0]
xv = np.linspace(-1, 3, 400)
mask = np.abs(xv - 1) > 0.01
yv = np.where(mask, (xv**2 - 1)/(xv - 1), np.nan)
ax.plot(xv, yv, color=colores[0], lw=2.5)
ax.scatter([1], [2], facecolors='none', edgecolors=colores[0],
           s=100, zorder=5, linewidths=2)
ax.set_title("Discontinuidad Removible\n(x²-1)/(x-1)", fontsize=10)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")
ax.grid(True, alpha=0.3)

# ── Gráfica 2: discontinuidad de salto ──
ax = axes[0, 1]
xv_izq = np.linspace(-1, 2, 200)
xv_der = np.linspace(2, 5, 200)
ax.plot(xv_izq, xv_izq + 1, color=colores[1], lw=2.5, label="x+1  (x<2)")
ax.plot(xv_der, xv_der - 1, color=colores[1], lw=2.5, ls='--', label="x-1  (x≥2)")
ax.scatter([2], [3], facecolors='none', edgecolors=colores[1], s=100, zorder=5, lw=2)
ax.scatter([2], [1], color=colores[1], s=80, zorder=5)
ax.set_title("Discontinuidad de Salto\nf(x) por partes  en x=2", fontsize=10)
ax.legend(fontsize=8)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")
ax.grid(True, alpha=0.3)

# ── Gráfica 3: discontinuidad esencial ──
ax = axes[1, 0]
xv_l = np.linspace(-3, 2.9, 300)
xv_r = np.linspace(3.1, 9, 300)
ax.plot(xv_l, 1/(xv_l - 3), color=colores[2], lw=2.5)
ax.plot(xv_r, 1/(xv_r - 3), color=colores[2], lw=2.5)
ax.axvline(3, color='gray', ls=':', lw=1.5, label='x=3 (asíntota vertical)')
ax.set_ylim(-10, 10)
ax.set_title("Discontinuidad Esencial\n1/(x-3)  en x=3", fontsize=10)
ax.legend(fontsize=8)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")
ax.grid(True, alpha=0.3)

# ── Gráfica 4: TVI ──
ax = axes[1, 1]
xv4 = np.linspace(0.5, 2.5, 300)
yv4 = xv4**3 - xv4 - 2
ax.plot(xv4, yv4, color=colores[3], lw=2.5)
ax.axhline(0, color='black', lw=0.8)
raiz_num = float(raiz_real[0])
ax.scatter([raiz_num], [0], color='red', zorder=5, s=100,
           label=f'Raíz ≈ {raiz_num:.4f}')
ax.scatter([1, 2], [float(fa), float(fb)], color=colores[3],
           marker='D', s=70, zorder=5)
ax.annotate(f'f(1)={fa}', (1, float(fa)), textcoords="offset points",
            xytext=(10, -15), fontsize=8)
ax.annotate(f'f(2)={fb}', (2, float(fb)), textcoords="offset points",
            xytext=(-30, 5), fontsize=8)
ax.fill_between([1, 2], [float(fa), float(fb)], alpha=0.1, color=colores[3])
ax.set_title("Teorema del Valor Intermedio\nx³-x-2  en [1,2]", fontsize=10)
ax.legend(fontsize=8)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("continuidad_funciones.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: continuidad_funciones.png")

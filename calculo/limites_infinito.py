"""
Módulo 1 - Límites al Infinito y Formas Indeterminadas
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

Temas cubiertos:
  - Límites cuando x → ±∞
  - Formas indeterminadas: 0/0, ∞/∞, 0·∞
  - Regla de L'Hôpital (introducción)
  - Asíntotas horizontales y verticales
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sympy import *

x = symbols('x')

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Límites al infinito
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  LÍMITES AL INFINITO")
print("=" * 60)

funciones_infinito = [
    (1/x,                   "1/x",                  "oo"),
    ((2*x**2 + 3) / (x**2 - 1), "(2x²+3)/(x²-1)", "oo"),
    (sin(x)/x,              "sin(x)/x",             "oo"),
    ((x**3) / exp(x),       "x³/eˣ",                "oo"),
]

for f, nombre, punto in funciones_infinito:
    lim = limit(f, x, oo)
    lim_neg = limit(f, x, -oo)
    print(f"\n  f(x) = {nombre}")
    print(f"    lim x→+∞  f(x) = {lim}")
    print(f"    lim x→-∞  f(x) = {lim_neg}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Formas indeterminadas — Regla de L'Hôpital
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  FORMAS INDETERMINADAS — REGLA DE L'HÔPITAL")
print("=" * 60)

casos_lhopital = [
    # (función,        punto,  forma,  nombre)
    (sin(x)/x,        0,      "0/0",  "sin(x)/x  en x→0"),
    ((x**2-1)/(x-1),  1,      "0/0",  "(x²-1)/(x-1)  en x→1"),
    ((exp(x)-1)/x,    0,      "0/0",  "(eˣ-1)/x  en x→0"),
    (x*exp(-x),       oo,     "0·∞",  "x·e⁻ˣ  en x→∞"),
    ((1 + 1/x)**x,    oo,     "1^∞",  "(1+1/x)ˣ  en x→∞"),
]

for f, punto, forma, nombre in casos_lhopital:
    lim = limit(f, x, punto)
    # Detectar si L'Hôpital aplica (numerador/denominador → 0)
    if '/' in str(f):
        num, den = fraction(f)
        val_num = limit(num, x, punto)
        val_den = limit(den, x, punto)
        aplicar = (val_num == 0 and val_den == 0) or \
                  (val_num in [oo, -oo] and val_den in [oo, -oo])
    else:
        aplicar = False

    print(f"\n  Forma {forma}:  f(x) = {nombre}")
    if aplicar:
        num, den = fraction(f)
        dnum = diff(num, x)
        dden = diff(den, x)
        lim2 = limit(dnum/dden, x, punto)
        print(f"    L'Hôpital → f'(x)/g'(x) = {dnum}/{dden}")
        print(f"    lim = {lim2}")
    else:
        print(f"    lim = {lim}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Visualización
# ─────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 10))
fig.suptitle("Módulo 1 — Límites al Infinito y Formas Indeterminadas",
             fontsize=14, fontweight='bold', y=0.98)

gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

colores = ['#2196F3', '#E91E63', '#4CAF50', '#FF9800', '#9C27B0', '#00BCD4']

# ── Gráfica 1: (2x²+3)/(x²-1) → asíntota horizontal y=2 ──
ax1 = fig.add_subplot(gs[0, 0])
xv = np.linspace(-10, 10, 500)
mask = np.abs(xv**2 - 1) > 0.05
yv = np.where(mask, (2*xv**2 + 3) / (xv**2 - 1), np.nan)
ax1.plot(xv, yv, color=colores[0], lw=2)
ax1.axhline(2, color='red', ls='--', lw=1.2, label='y = 2  (asíntota)')
ax1.axvline(1,  color='gray', ls=':', lw=1)
ax1.axvline(-1, color='gray', ls=':', lw=1)
ax1.set_ylim(-10, 10)
ax1.set_title("(2x²+3)/(x²-1)", fontsize=10)
ax1.legend(fontsize=8)
ax1.set_xlabel("x"); ax1.set_ylabel("f(x)")
ax1.grid(True, alpha=0.3)

# ── Gráfica 2: sin(x)/x → límite en 0 y en ∞ ──
ax2 = fig.add_subplot(gs[0, 1])
xv2 = np.linspace(-20, 20, 1000)
xv2_safe = np.where(xv2 == 0, 1e-10, xv2)
yv2 = np.sin(xv2_safe) / xv2_safe
ax2.plot(xv2, yv2, color=colores[1], lw=2)
ax2.axhline(0, color='red', ls='--', lw=1.2, label='y = 0  (lim x→∞)')
ax2.scatter([0], [1], color='green', zorder=5, s=60, label='lim x→0 = 1')
ax2.set_title("sin(x)/x", fontsize=10)
ax2.legend(fontsize=8)
ax2.set_xlabel("x"); ax2.set_ylabel("f(x)")
ax2.grid(True, alpha=0.3)

# ── Gráfica 3: x³/eˣ → 0 cuando x→∞ ──
ax3 = fig.add_subplot(gs[0, 2])
xv3 = np.linspace(0, 15, 300)
yv3 = xv3**3 / np.exp(xv3)
ax3.plot(xv3, yv3, color=colores[2], lw=2)
ax3.axhline(0, color='red', ls='--', lw=1.2, label='y = 0  (lim x→∞)')
ax3.set_title("x³/eˣ", fontsize=10)
ax3.legend(fontsize=8)
ax3.set_xlabel("x"); ax3.set_ylabel("f(x)")
ax3.grid(True, alpha=0.3)

# ── Gráfica 4: (x²-1)/(x-1) y su límite en x=1 ──
ax4 = fig.add_subplot(gs[1, 0])
xv4 = np.linspace(-1, 3, 300)
mask4 = np.abs(xv4 - 1) > 0.02
yv4 = np.where(mask4, (xv4**2 - 1)/(xv4 - 1), np.nan)
ax4.plot(xv4, yv4, color=colores[3], lw=2)
ax4.scatter([1], [2], facecolors='none', edgecolors='black',
            s=80, zorder=5, label='lim x→1 = 2')
ax4.set_title("(x²-1)/(x-1)  [forma 0/0]", fontsize=10)
ax4.legend(fontsize=8)
ax4.set_xlabel("x"); ax4.set_ylabel("f(x)")
ax4.grid(True, alpha=0.3)

# ── Gráfica 5: (eˣ-1)/x → 1 en x=0 ──
ax5 = fig.add_subplot(gs[1, 1])
xv5 = np.linspace(-3, 3, 300)
xv5_safe = np.where(xv5 == 0, 1e-10, xv5)
yv5 = (np.exp(xv5_safe) - 1) / xv5_safe
ax5.plot(xv5, yv5, color=colores[4], lw=2)
ax5.scatter([0], [1], color='green', zorder=5, s=60, label='lim x→0 = 1')
ax5.set_title("(eˣ-1)/x  [L'Hôpital]", fontsize=10)
ax5.legend(fontsize=8)
ax5.set_xlabel("x"); ax5.set_ylabel("f(x)")
ax5.grid(True, alpha=0.3)

# ── Gráfica 6: (1+1/x)ˣ → e ──
ax6 = fig.add_subplot(gs[1, 2])
xv6 = np.linspace(1, 100, 300)
yv6 = (1 + 1/xv6)**xv6
ax6.plot(xv6, yv6, color=colores[5], lw=2)
ax6.axhline(np.e, color='red', ls='--', lw=1.2, label=f'y = e ≈ {np.e:.4f}')
ax6.set_title("(1+1/x)ˣ → e", fontsize=10)
ax6.legend(fontsize=8)
ax6.set_xlabel("x"); ax6.set_ylabel("f(x)")
ax6.grid(True, alpha=0.3)

plt.savefig("limites_infinito.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: limites_infinito.png")

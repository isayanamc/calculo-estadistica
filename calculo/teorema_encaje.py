"""
Módulo 1 - Teorema del Encaje (Squeeze Theorem)
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

Temas cubiertos:
  - Enunciado formal del Teorema del Encaje
  - Aplicación para calcular límites oscilantes
  - Límite clásico: lim x→0  x·sin(1/x) = 0
  - Límite trigonométrico: lim x→0  sin(x)/x = 1
  - Visualización de las funciones "encajadoras"
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = symbols('x')

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Enunciado del Teorema
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  TEOREMA DEL ENCAJE (Squeeze / Sandwich Theorem)")
print("=" * 60)
print("""
  Si  g(x) ≤ f(x) ≤ h(x)  cerca de x = a  (excepto posiblemente en a)
  y   lim x→a  g(x) = lim x→a  h(x) = L
  entonces:
        lim x→a  f(x) = L
""")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Ejemplo 1 — x·sin(1/x) → 0 cuando x→0
# ─────────────────────────────────────────────────────────────
print("─" * 60)
print("  Ejemplo 1:  lim x→0  x·sin(1/x)")
print("─" * 60)
print("""
  Sabemos que  -1 ≤ sin(1/x) ≤ 1  para todo x ≠ 0
  Multiplicando por |x|:
      -|x| ≤ x·sin(1/x) ≤ |x|

  Como  lim x→0 (-|x|) = 0  y  lim x→0 (|x|) = 0
  Por el Teorema del Encaje:
      lim x→0  x·sin(1/x) = 0
""")
f_ej1 = x * sin(1/x)
lim_ej1 = limit(f_ej1, x, 0)
print(f"  Verificación con SymPy:  lim x→0  x·sin(1/x) = {lim_ej1}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Ejemplo 2 — sin(x)/x → 1 cuando x→0
# ─────────────────────────────────────────────────────────────
print("\n" + "─" * 60)
print("  Ejemplo 2:  lim x→0  sin(x)/x  (límite trigonométrico fundamental)")
print("─" * 60)
print("""
  Se puede demostrar geométricamente que para x ∈ (0, π/2):
      cos(x) ≤ sin(x)/x ≤ 1

  Como  lim x→0 cos(x) = 1  y  lim x→0 (1) = 1
  Por el Teorema del Encaje:
      lim x→0  sin(x)/x = 1
""")
f_ej2 = sin(x)/x
lim_ej2 = limit(f_ej2, x, 0)
print(f"  Verificación con SymPy:  lim x→0  sin(x)/x = {lim_ej2}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 4: Ejemplo 3 — x²·cos(1/x²) → 0
# ─────────────────────────────────────────────────────────────
print("\n" + "─" * 60)
print("  Ejemplo 3:  lim x→0  x²·cos(1/x²)")
print("─" * 60)
print("""
  Sabemos que  -1 ≤ cos(1/x²) ≤ 1
  Multiplicando por x² ≥ 0:
      -x² ≤ x²·cos(1/x²) ≤ x²

  Como  lim x→0 (-x²) = 0  y  lim x→0 (x²) = 0
  Por el Teorema del Encaje:
      lim x→0  x²·cos(1/x²) = 0
""")
f_ej3 = x**2 * cos(1/x**2)
lim_ej3 = limit(f_ej3, x, 0)
print(f"  Verificación con SymPy:  lim x→0  x²·cos(1/x²) = {lim_ej3}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 5: Visualización
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Módulo 1 — Teorema del Encaje (Squeeze Theorem)",
             fontsize=13, fontweight='bold')

# ── Gráfica 1: x·sin(1/x) encajada entre -|x| y |x| ──
ax = axes[0]
xv = np.linspace(-0.5, 0.5, 2000)
xv_safe = np.where(xv == 0, 1e-10, xv)
f_vals = xv_safe * np.sin(1/xv_safe)
ax.plot(xv, f_vals,    color='#1565C0', lw=1.5,  label="x·sin(1/x)", zorder=3)
ax.plot(xv, np.abs(xv), color='#E53935', lw=2, ls='--', label="|x|  (cota superior)")
ax.plot(xv, -np.abs(xv), color='#43A047', lw=2, ls='--', label="-|x|  (cota inferior)")
ax.scatter([0], [0], color='black', zorder=5, s=80, label="lim = 0")
ax.set_title("lim x→0  x·sin(1/x) = 0", fontsize=10)
ax.legend(fontsize=7, loc='upper right')
ax.set_xlabel("x"); ax.set_ylabel("f(x)")
ax.set_ylim(-0.6, 0.6)
ax.grid(True, alpha=0.3)

# ── Gráfica 2: sin(x)/x encajada entre cos(x) y 1 ──
ax = axes[1]
xv2 = np.linspace(-np.pi/2 + 0.01, np.pi/2 - 0.01, 400)
f_vals2 = np.sin(xv2) / xv2
ax.plot(xv2, f_vals2,          color='#1565C0', lw=2,   label="sin(x)/x", zorder=3)
ax.plot(xv2, np.cos(xv2),      color='#E53935', lw=2, ls='--', label="cos(x)  (cota inferior)")
ax.axhline(1,                   color='#43A047', lw=2, ls='--', label="1  (cota superior)")
ax.scatter([0], [1], color='black', zorder=5, s=80, label="lim = 1")
ax.fill_between(xv2, np.cos(xv2), f_vals2, alpha=0.08, color='#1565C0')
ax.fill_between(xv2, f_vals2, 1, alpha=0.08, color='#43A047')
ax.set_title("lim x→0  sin(x)/x = 1", fontsize=10)
ax.legend(fontsize=7)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")
ax.grid(True, alpha=0.3)

# ── Gráfica 3: x²·cos(1/x²) encajada entre -x² y x² ──
ax = axes[2]
xv3 = np.linspace(-0.6, 0.6, 2000)
xv3_safe = np.where(xv3 == 0, 1e-10, xv3)
f_vals3 = xv3_safe**2 * np.cos(1/xv3_safe**2)
ax.plot(xv3, f_vals3,   color='#1565C0', lw=1.5,  label="x²·cos(1/x²)", zorder=3)
ax.plot(xv3, xv3**2,    color='#E53935', lw=2, ls='--', label="x²  (cota superior)")
ax.plot(xv3, -xv3**2,   color='#43A047', lw=2, ls='--', label="-x²  (cota inferior)")
ax.scatter([0], [0], color='black', zorder=5, s=80, label="lim = 0")
ax.set_title("lim x→0  x²·cos(1/x²) = 0", fontsize=10)
ax.legend(fontsize=7)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")
ax.set_ylim(-0.4, 0.4)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("teorema_encaje.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: teorema_encaje.png")

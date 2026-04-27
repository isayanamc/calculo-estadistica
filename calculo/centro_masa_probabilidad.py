"""
Módulo 5 - Centro de Masa y Funciones de Densidad de Probabilidad
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

¿QUÉ ES EL CENTRO DE MASA?
────────────────────────────
El centro de masa es el punto donde se "equilibra" un objeto.
Si colgaras una figura plana de ese punto, quedaría horizontal.

Para un sistema de masas discretas m₁, m₂, ..., mₙ en posiciones x₁, x₂, ...:
    x̄ = (Σ mᵢ·xᵢ) / (Σ mᵢ)   ← promedio ponderado por masa

Para una región continua con densidad ρ(x) entre a y b:
    Masa total:  M = ∫[a,b] ρ(x) dx
    Momento:     Mx = ∫[a,b] x·ρ(x) dx
    Centro:      x̄ = Mx / M

Para una lámina delgada entre f(x) y g(x) con densidad uniforme ρ=1:
    M  = ∫[a,b] [f(x) − g(x)] dx         ← área de la región
    Mx = ∫[a,b] x·[f(x) − g(x)] dx       ← momento respecto al eje y
    My = ∫[a,b] ½·[f(x)² − g(x)²] dx     ← momento respecto al eje x
    x̄ = Mx / M ,   ȳ = My / M

FUNCIONES DE DENSIDAD DE PROBABILIDAD:
────────────────────────────────────────
En probabilidad, una función f(x) es una DENSIDAD DE PROBABILIDAD si:
    1) f(x) ≥ 0  para todo x         (no hay probabilidades negativas)
    2) ∫[−∞,∞] f(x) dx = 1           (la probabilidad total es 100%)

La probabilidad de que X esté entre a y b es:
    P(a ≤ X ≤ b) = ∫[a,b] f(x) dx

El VALOR ESPERADO (media) de la distribución es:
    μ = E[X] = ∫[−∞,∞] x·f(x) dx

La VARIANZA mide qué tan dispersos están los valores:
    σ² = Var[X] = ∫[−∞,∞] (x−μ)²·f(x) dx

DISTRIBUCIONES IMPORTANTES:
  • Uniforme en [a,b]:  f(x) = 1/(b−a)      μ = (a+b)/2
  • Exponencial:        f(x) = λ·e^(−λx)    μ = 1/λ
  • Normal (Gauss):     f(x) = (1/σ√(2π))·e^(−(x−μ)²/2σ²)
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = symbols('x', real=True)

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Centro de masa
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  CENTRO DE MASA")
print("=" * 60)

# ── Masas discretas ──
print("""
  CASO 1: Sistema de masas discretas
  ─────────────────────────────────────
  Fórmula: x̄ = (Σ mᵢ·xᵢ) / (Σ mᵢ)

  Ejemplo: 3 masas en una barra
""")
masas = [(2, 1), (5, 3), (3, 7)]   # (masa, posición)
M_total = sum(m for m, _ in masas)
momento = sum(m*pos for m, pos in masas)
x_barra = momento / M_total

for m, pos in masas:
    print(f"    m={m} kg  en  x={pos} m  →  contribuye {m*pos} kg·m")
print(f"  Masa total:  M = {M_total} kg")
print(f"  Momento:     Σmᵢxᵢ = {momento} kg·m")
print(f"  Centro de masa: x̄ = {momento}/{M_total} = {x_barra:.4f} m\n")

# ── Centro de masa continuo ──
print("  CASO 2: Barra con densidad variable ρ(x)")
print("  ────────────────────────────────────────────")

def centro_masa_1d(rho_expr, a, b, nombre_rho):
    M  = integrate(rho_expr, (x, a, b))
    Mx = integrate(x * rho_expr, (x, a, b))
    x_bar = simplify(Mx / M)
    print(f"  ρ(x) = {nombre_rho}  en  [{a}, {b}]")
    print(f"    Masa total:   M = ∫ρ dx = {M}")
    print(f"    Momento:      Mx = ∫x·ρ dx = {Mx}")
    print(f"    Centro:       x̄ = Mx/M = {x_bar} ≈ {float(x_bar):.4f}")
    print()

centro_masa_1d(1 + x,        0, 2, "1 + x       (densidad lineal creciente)")
centro_masa_1d(x**2,         0, 3, "x²          (densidad cuadrática)")
centro_masa_1d(exp(-x),      0, oo, "e⁻ˣ        (densidad exponencial)")

# ── Centro de masa de lámina plana ──
print("  CASO 3: Lámina plana entre dos curvas")
print("  ────────────────────────────────────────────")
print("""
  Para una lámina entre f(x) (arriba) y g(x) (abajo):
    M  = ∫ [f(x)−g(x)] dx
    x̄  = [∫ x·(f(x)−g(x)) dx] / M
    ȳ  = [∫ ½·(f(x)²−g(x)²) dx] / M
""")

laminas = [
    (x**2, x,     0, 1, "f(x)=x², g(x)=x  en [0,1]"),
    (x,    x**2,  0, 1, "f(x)=x,  g(x)=x²  en [0,1]"),
    (4-x**2, 0,   -2, 2, "f(x)=4−x², g(x)=0  en [−2,2]"),
]

for f_expr, g_expr, a, b, nombre in laminas:
    diff_fg = f_expr - g_expr
    M   = integrate(diff_fg, (x, a, b))
    Mx  = integrate(x * diff_fg, (x, a, b))
    My  = integrate(Rational(1,2) * (f_expr**2 - g_expr**2), (x, a, b))
    x_bar = simplify(Mx / M)
    y_bar = simplify(My / M)
    print(f"  {nombre}")
    print(f"    M = {M},   x̄ = {x_bar} ≈ {float(x_bar):.4f},   "
          f"ȳ = {y_bar} ≈ {float(y_bar):.4f}\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Funciones de densidad de probabilidad
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  FUNCIONES DE DENSIDAD DE PROBABILIDAD")
print("=" * 60)
print("""
  Una función f(x) es densidad de probabilidad si:
    1) f(x) ≥ 0 en todo su dominio
    2) ∫ f(x) dx = 1  (integral en todo el dominio)

  La probabilidad de que X caiga en [a,b] es:
    P(a ≤ X ≤ b) = ∫[a,b] f(x) dx
""")

lam = symbols('lambda', positive=True)
mu_s, sigma_s = symbols('mu sigma', real=True)

distribuciones = [
    # nombre, f(x), dominio, a_int, b_int
    ("Uniforme en [0,1]",
     S.One,
     "x ∈ [0,1]",
     0, 1),
    ("Exponencial λ=2  (f(x)=2e^{-2x})",
     2*exp(-2*x),
     "x ≥ 0",
     0, oo),
    ("Triangular en [0,2]  (f(x)=x para [0,1], 2-x para [1,2])",
     Piecewise((x, (x>=0) & (x<=1)), (2-x, (x>1) & (x<=2)), (0, True)),
     "x ∈ [0,2]",
     0, 2),
]

for nombre, f_expr, dominio, a_int, b_int in distribuciones:
    total = integrate(f_expr, (x, a_int, b_int))
    mu_val = integrate(x * f_expr, (x, a_int, b_int))
    print(f"  Distribución: {nombre}")
    print(f"  Dominio: {dominio}")
    print(f"  ∫ f(x) dx = {simplify(total)}  "
          f"{'[OK] es densidad' if simplify(total-1)==0 else '-'}")
    print(f"  Valor esperado μ = ∫ x·f(x)dx = {simplify(mu_val)} "
          f"≈ {float(mu_val.evalf()):.4f}")
    print()

# Probabilidades con la exponencial
print("  PROBABILIDADES — Distribución Exponencial (λ=2):")
f_exp = 2*exp(-2*x)
intervalos = [(0, 1), (0.5, 1.5), (1, oo)]
for a_p, b_p in intervalos:
    prob = integrate(f_exp, (x, a_p, b_p))
    print(f"    P({a_p} ≤ X ≤ {b_p}) = {simplify(prob)} "
          f"≈ {float(prob.evalf()):.4f}")

# Distribución Normal — verificación numérica
print("""
  Distribución Normal N(μ=0, σ=1):
    f(x) = (1/√(2π)) · e^(−x²/2)
""")
mu_v, sigma_v = 0, 1
f_normal = lambda xv: (1/(sigma_v*np.sqrt(2*np.pi))) * np.exp(-0.5*((xv-mu_v)/sigma_v)**2)
xv_norm = np.linspace(-5, 5, 10000)
total_norm = np.trapezoid(f_normal(xv_norm), xv_norm)
prob_1sigma = np.trapezoid(f_normal(xv_norm[(xv_norm>=-1)&(xv_norm<=1)]),
                       xv_norm[(xv_norm>=-1)&(xv_norm<=1)])
prob_2sigma = np.trapezoid(f_normal(xv_norm[(xv_norm>=-2)&(xv_norm<=2)]),
                       xv_norm[(xv_norm>=-2)&(xv_norm<=2)])
print(f"  ∫ f(x)dx ≈ {total_norm:.6f}  [OK]")
print(f"  P(−1 ≤ X ≤ 1) ≈ {prob_1sigma:.4f}  ({prob_1sigma*100:.2f}%  → regla 68%)")
print(f"  P(−2 ≤ X ≤ 2) ≈ {prob_2sigma:.4f}  ({prob_2sigma*100:.2f}%  → regla 95%)")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Visualización
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle("Módulo 5 — Centro de Masa y Densidad de Probabilidad",
             fontsize=14, fontweight='bold')

# ── Centro de masa discreto ──
ax = axes[0, 0]
posiciones = [m[1] for m in masas]
pesos      = [m[0] for m in masas]
ax.barh([0]*3, pesos, left=posiciones,
        color=['#1565C0','#C62828','#2E7D32'], alpha=0.7, height=0.3)
for m, pos in masas:
    ax.scatter([pos], [0], s=m*200, color='black', zorder=5)
    ax.text(pos, 0.2, f"m={m}\nx={pos}", ha='center', fontsize=8)
ax.axvline(x_barra, color='red', lw=2.5, ls='--',
           label=f"x̄ = {x_barra:.3f} m")
ax.set_title("Centro de masa — masas discretas", fontsize=9)
ax.legend(fontsize=8); ax.set_xlabel("Posición (m)")
ax.set_ylim(-0.5, 0.8); ax.grid(True, alpha=0.3, axis='x')
ax.set_yticks([])

# ── Centro de masa lámina ──
ax = axes[0, 1]
xv = np.linspace(0, 1, 300)
ax.fill_between(xv, xv**2, xv, alpha=0.35, color='#1565C0',
                label="Región entre x² y x")
ax.plot(xv, xv,    color='#C62828', lw=2)
ax.plot(xv, xv**2, color='#2E7D32', lw=2)
ax.scatter([0.5], [0.5], color='red', zorder=5, s=200,
           marker='*', label="Centro (½, ½)")
ax.set_title("Centro de masa de lámina\nentre f(x)=x y g(x)=x²", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# ── Densidad variable ──
ax = axes[0, 2]
xv2 = np.linspace(0, 2, 300)
rho = 1 + xv2
ax.fill_between(xv2, rho, alpha=0.3, color='#6A1B9A')
ax.plot(xv2, rho, color='#6A1B9A', lw=2.5, label="ρ(x) = 1+x")
x_cm = float(integrate(x*(1+x), (x,0,2)) / integrate(1+x, (x,0,2)))
ax.axvline(x_cm, color='red', lw=2.5, ls='--',
           label=f"x̄ = {x_cm:.4f}")
ax.set_title("Densidad lineal ρ(x)=1+x\nen [0,2]", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("ρ(x)")

# ── Distribución Uniforme ──
ax = axes[1, 0]
xv3 = np.linspace(-0.5, 1.5, 300)
yv3 = np.where((xv3 >= 0) & (xv3 <= 1), 1.0, 0.0)
ax.plot(xv3, yv3, color='#1565C0', lw=2.5, label="f(x)=1  en [0,1]")
ax.fill_between(xv3, yv3, alpha=0.25, color='#1565C0')
ax.fill_between(xv3[(xv3>=0.25)&(xv3<=0.75)],
                yv3[(xv3>=0.25)&(xv3<=0.75)],
                alpha=0.5, color='red', label="P(0.25≤X≤0.75)=0.5")
ax.set_title("Distribución Uniforme [0,1]\nμ=0.5, ∫f=1 [OK]", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")
ax.set_ylim(-0.1, 1.5)

# ── Distribución Exponencial ──
ax = axes[1, 1]
xv4 = np.linspace(0, 3, 300)
for lam_v, color in [(0.5,'#C62828'),(1,'#1565C0'),(2,'#2E7D32')]:
    yv4 = lam_v * np.exp(-lam_v * xv4)
    ax.plot(xv4, yv4, color=color, lw=2.5, label=f"λ={lam_v}, μ={1/lam_v}")
ax.set_title("Distribución Exponencial\nf(x)=λe^{-λx}", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")

# ── Distribución Normal ──
ax = axes[1, 2]
xv5 = np.linspace(-5, 5, 500)
for mu_v, sigma_v, color, label in [
    (0, 1, '#1565C0', "N(0,1)"),
    (0, 2, '#C62828', "N(0,2)"),
    (2, 1, '#2E7D32', "N(2,1)"),
]:
    yv5 = (1/(sigma_v*np.sqrt(2*np.pi))) * np.exp(-0.5*((xv5-mu_v)/sigma_v)**2)
    ax.plot(xv5, yv5, color=color, lw=2.5, label=label)

# Colorear ±1σ para N(0,1)
mask = (xv5 >= -1) & (xv5 <= 1)
yv5_01 = (1/np.sqrt(2*np.pi)) * np.exp(-0.5*xv5**2)
ax.fill_between(xv5[mask], yv5_01[mask], alpha=0.25, color='#1565C0',
                label="P(−1≤X≤1)≈68%")
ax.set_title("Distribución Normal N(μ,σ)\nRegla 68-95-99.7", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")

plt.tight_layout(pad=2.0)
plt.savefig("centro_masa_probabilidad.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n[OK]  Gráfica guardada: centro_masa_probabilidad.png")
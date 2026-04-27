"""
Módulo 4 - Técnicas de Integración e Integrales Impropias
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

¿POR QUÉ NECESITAMOS TÉCNICAS DE INTEGRACIÓN?
───────────────────────────────────────────────
La tabla de integrales fundamentales solo cubre funciones simples.
Para funciones más complejas necesitamos transformar el integrando
en una forma que sí podamos integrar directamente.

Las principales técnicas son:

  1. SUSTITUCIÓN (cambio de variable u):
     Usada cuando el integrando tiene una función compuesta.
     Se elige u = g(x), se calcula du = g'(x)dx,
     y se transforma toda la integral a variable u.
     Ejemplo: ∫ 2x·cos(x²) dx  →  u=x², du=2x dx  →  ∫ cos(u) du = sin(u)+C

  2. INTEGRACIÓN POR PARTES:
     Basada en la inversa de la regla del producto.
     Fórmula: ∫ u·dv = u·v − ∫ v·du
     Regla LIATE para elegir u: Logarítmica, Inversa trig,
     Algebraica, Trigonométrica, Exponencial.
     Ejemplo: ∫ x·eˣ dx  →  u=x, dv=eˣdx  →  x·eˣ − eˣ + C

  3. FRACCIONES PARCIALES:
     Para integrar funciones racionales P(x)/Q(x).
     Se descompone el denominador en factores y se separa
     en fracciones simples que se integran individualmente.
     Ejemplo: ∫ 1/(x²−1) dx = ∫ [1/(2(x−1)) − 1/(2(x+1))] dx

  4. SUSTITUCIÓN TRIGONOMÉTRICA:
     Para integrales con √(a²−x²), √(a²+x²) o √(x²−a²).
     Se sustituye x por una función trigonométrica para
     eliminar la raíz cuadrada usando identidades pitagóricas.
     • √(a²−x²): usar x = a·sin(θ)
     • √(a²+x²): usar x = a·tan(θ)
     • √(x²−a²): usar x = a·sec(θ)

INTEGRALES IMPROPIAS:
  Una integral es IMPROPIA cuando:
    a) Uno o ambos límites son ±∞
    b) El integrando tiene una discontinuidad en [a, b]

  Se definen como límites de integrales ordinarias:
    ∫[a,∞] f(x) dx = lim[b→∞] ∫[a,b] f(x) dx

  Si el límite existe → la integral CONVERGE
  Si el límite es ±∞ → la integral DIVERGE
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x, u, t = symbols('x u t')

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Sustitución (cambio de variable)
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  TÉCNICA 1: SUSTITUCIÓN (CAMBIO DE VARIABLE u)")
print("=" * 60)
print("""
  Pasos:
    1) Identificar una función interior g(x) y hacer u = g(x)
    2) Calcular du = g'(x) dx  →  dx = du / g'(x)
    3) Reescribir toda la integral en términos de u
    4) Integrar en u
    5) Sustituir de vuelta u = g(x)
""")

casos_sust = [
    (2*x*cos(x**2),     "2x·cos(x²)",    "u = x²,  du = 2x dx"),
    (x**2*exp(x**3),    "x²·eˣ³",        "u = x³,  du = 3x² dx"),
    (sin(x)*cos(x),     "sin(x)·cos(x)", "u = sin(x),  du = cos(x) dx"),
    ((2*x)/(x**2+1),    "2x/(x²+1)",     "u = x²+1,  du = 2x dx"),
    (exp(x)/(1+exp(x)), "eˣ/(1+eˣ)",     "u = 1+eˣ,  du = eˣ dx"),
    (x*sqrt(x**2+4),    "x·√(x²+4)",     "u = x²+4,  du = 2x dx"),
]

for f_expr, nombre, sustitucion in casos_sust:
    F = integrate(f_expr, x)
    verif = simplify(diff(F, x) - f_expr) == 0
    print(f"  ∫ {nombre} dx")
    print(f"    Sustitución: {sustitucion}")
    print(f"    Resultado:   {F} + C  {'✅' if verif else '❌'}\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Integración por partes
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  TÉCNICA 2: INTEGRACIÓN POR PARTES")
print("=" * 60)
print("""
  Fórmula: ∫ u·dv = u·v − ∫ v·du

  Regla LIATE para elegir u (la que aparece primero en la lista):
    L - Logarítmica:    ln(x), log(x)
    I - Inversa trig:   arcsin, arctan, ...
    A - Algebraica:     xⁿ, polinomios
    T - Trigonométrica: sin, cos, tan
    E - Exponencial:    eˣ, aˣ

  El objetivo es que ∫ v·du sea más fácil que la original.
""")

casos_partes = [
    (x*exp(x),      "x·eˣ",        "u=x,     dv=eˣdx  →  LIATE: A antes que E"),
    (x*sin(x),      "x·sin(x)",    "u=x,     dv=sin(x)dx"),
    (x**2*exp(x),   "x²·eˣ",       "u=x²,    dv=eˣdx  (necesita 2 pasos)"),
    (log(x),        "ln(x)",       "u=ln(x), dv=dx    →  L primero en LIATE"),
    (x*log(x),      "x·ln(x)",     "u=ln(x), dv=x·dx"),
    (exp(x)*sin(x), "eˣ·sin(x)",   "u=sin(x),dv=eˣdx  (circular → despejar)"),
    (asin(x),       "arcsin(x)",   "u=arcsin(x), dv=dx"),
]

for f_expr, nombre, nota in casos_partes:
    F = integrate(f_expr, x)
    verif = simplify(diff(F, x) - f_expr) == 0
    print(f"  ∫ {nombre} dx")
    print(f"    Elección: {nota}")
    print(f"    Resultado: {expand(F)} + C  {'✅' if verif else '❌'}\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Fracciones parciales
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  TÉCNICA 3: FRACCIONES PARCIALES")
print("=" * 60)
print("""
  Se usa para integrar funciones racionales P(x)/Q(x)
  donde el grado de P < grado de Q.

  Pasos:
    1) Factorizar el denominador Q(x)
    2) Escribir P(x)/Q(x) como suma de fracciones simples
    3) Determinar los coeficientes (A, B, C, ...)
    4) Integrar cada fracción simple
""")

casos_frac = [
    (1/(x**2 - 1),          "1/(x²−1)"),
    (x/(x**2 - 3*x + 2),    "x/(x²−3x+2)"),
    ((2*x+1)/(x**2+3*x+2),  "(2x+1)/(x²+3x+2)"),
    (1/(x*(x+1)**2),        "1/(x(x+1)²)"),
]

for f_expr, nombre in casos_frac:
    # Descomposición en fracciones parciales
    f_parcial = apart(f_expr, x)
    F = integrate(f_expr, x)
    verif = simplify(diff(F, x) - f_expr) == 0
    print(f"  ∫ {nombre} dx")
    print(f"    Descomposición: {f_parcial}")
    print(f"    Resultado: {F} + C  {'✅' if verif else '❌'}\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 4: Sustitución trigonométrica
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  TÉCNICA 4: SUSTITUCIÓN TRIGONOMÉTRICA")
print("=" * 60)
print("""
  Usada cuando aparecen raíces de la forma:
    √(a²−x²)  →  x = a·sin(θ),   identidad: 1−sin²θ = cos²θ
    √(a²+x²)  →  x = a·tan(θ),   identidad: 1+tan²θ = sec²θ
    √(x²−a²)  →  x = a·sec(θ),   identidad: sec²θ−1 = tan²θ
""")

casos_trig_sust = [
    (1/sqrt(1 - x**2),         "1/√(1−x²)  →  x=sin(θ)"),
    (sqrt(1 - x**2),           "√(1−x²)    →  x=sin(θ)"),
    (1/(1 + x**2),             "1/(1+x²)   →  x=tan(θ)"),
    (1/sqrt(4 - x**2),         "1/√(4−x²)  →  x=2sin(θ)"),
    (x**2/sqrt(4 - x**2),     "x²/√(4−x²) →  x=2sin(θ)"),
]

for f_expr, nombre in casos_trig_sust:
    try:
        F = integrate(f_expr, x)
        verif = simplify(diff(F, x) - f_expr) == 0
        print(f"  ∫ {nombre} dx")
        print(f"    Resultado: {simplify(F)} + C  {'✅' if verif else '❌'}\n")
    except Exception:
        print(f"  ∫ {nombre} dx → requiere cálculo manual\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 5: Integrales impropias
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  INTEGRALES IMPROPIAS")
print("=" * 60)
print("""
  Una integral es IMPROPIA cuando tiene límites infinitos o el
  integrando tiene discontinuidades en el intervalo de integración.

  Se evalúa como un límite:
    ∫[a,∞] f(x)dx = lim[b→∞] ∫[a,b] f(x)dx

  Si el límite existe y es finito → CONVERGE
  Si el límite es infinito         → DIVERGE
""")

casos_impropias = [
    (1/x**2,   1,  oo,    "∫[1,∞] 1/x²  dx",      "converge (p>1)"),
    (1/x,      1,  oo,    "∫[1,∞] 1/x   dx",       "diverge  (p=1)"),
    (exp(-x),  0,  oo,    "∫[0,∞] e⁻ˣ  dx",        "converge"),
    (1/sqrt(x),0,  1,     "∫[0,1] 1/√x  dx",       "converge (discontinua en 0)"),
    (1/x,      0,  1,     "∫[0,1] 1/x   dx",       "diverge  (discontinua en 0)"),
    (exp(-x**2), -oo, oo, "∫[−∞,∞] e^(−x²) dx",   "converge → √π"),
]

for f_expr, a, b, nombre, comportamiento in casos_impropias:
    resultado = integrate(f_expr, (x, a, b))
    converge  = resultado.is_finite
    print(f"  {nombre}")
    print(f"    Resultado: {resultado}  →  "
          f"{'CONVERGE ✅' if converge else 'DIVERGE ❌'}  ({comportamiento})\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 6: Visualización
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Módulo 4 — Técnicas de Integración e Integrales Impropias",
             fontsize=14, fontweight='bold')

# ── Sustitución: 2x·cos(x²) ──
ax = axes[0, 0]
xv = np.linspace(0, np.sqrt(2*np.pi), 300)
f_v = 2*xv*np.cos(xv**2)
F_v = np.sin(xv**2)
ax.plot(xv, f_v, color='#1565C0', lw=2.5, label="f(x) = 2x·cos(x²)")
ax.plot(xv, F_v, color='#C62828', lw=2, ls='--', label="F(x) = sin(x²) + C")
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Sustitución: u = x²\n∫ 2x·cos(x²)dx = sin(x²)+C", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# ── Por partes: x·eˣ ──
ax = axes[0, 1]
xv2 = np.linspace(-3, 2, 300)
f_v2 = xv2 * np.exp(xv2)
F_v2 = (xv2 - 1) * np.exp(xv2)
ax.plot(xv2, f_v2, color='#2E7D32', lw=2.5, label="f(x) = x·eˣ")
ax.plot(xv2, F_v2, color='#E65100', lw=2, ls='--',
        label="F(x) = (x−1)eˣ + C")
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Por Partes: u=x, dv=eˣdx\n∫ x·eˣ dx = (x−1)eˣ + C", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_ylim(-3, 5)

# ── Fracciones parciales: 1/(x²-1) ──
ax = axes[0, 2]
xv3 = np.linspace(-3, -1.05, 150)
xv3b = np.linspace(1.05, 3, 150)
f_v3a = 1/(xv3**2 - 1)
f_v3b = 1/(xv3b**2 - 1)
ax.plot(xv3,  f_v3a, color='#6A1B9A', lw=2.5, label="f(x) = 1/(x²−1)")
ax.plot(xv3b, f_v3b, color='#6A1B9A', lw=2.5)
ax.axvline(-1, color='gray', ls=':', lw=1.5, label="Asíntotas x=±1")
ax.axvline( 1, color='gray', ls=':', lw=1.5)
ax.set_ylim(-5, 5)
ax.set_title("Fracciones Parciales\n1/(x²−1) = 1/(2(x−1)) − 1/(2(x+1))",
             fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# ── Sustitución trig: √(1-x²) ──
ax = axes[1, 0]
xv4 = np.linspace(-1, 1, 300)
yv4 = np.sqrt(np.maximum(1 - xv4**2, 0))
ax.plot(xv4, yv4, color='#00838F', lw=2.5,
        label="f(x) = √(1−x²)")
ax.fill_between(xv4, yv4, alpha=0.2, color='#00838F',
                label="Área = π/2 (semicírculo)")
ax.set_aspect('equal')
ax.set_title("Sust. Trig: x=sin(θ)\n∫√(1−x²)dx → semicírculo", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# ── Integral impropia convergente vs divergente ──
ax = axes[1, 1]
xv5 = np.linspace(1, 8, 300)
ax.plot(xv5, 1/xv5**2, color='#1565C0', lw=2.5, label="1/x²  CONVERGE → 1")
ax.plot(xv5, 1/xv5,    color='#C62828', lw=2.5, label="1/x   DIVERGE → ∞")
ax.fill_between(xv5, 1/xv5**2, alpha=0.2, color='#1565C0')
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Integrales Impropias ∫[1,∞]\n1/x² converge,  1/x diverge",
             fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")
ax.set_ylim(-0.1, 1.5)

# ── Integral de Gauss: e^(-x²) ──
ax = axes[1, 2]
xv6 = np.linspace(-4, 4, 400)
yv6 = np.exp(-xv6**2)
ax.plot(xv6, yv6, color='#2E7D32', lw=2.5, label="e^(−x²)")
ax.fill_between(xv6, yv6, alpha=0.25, color='#2E7D32',
                label=f"∫[−∞,∞] = √π ≈ {np.sqrt(np.pi):.4f}")
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Integral de Gauss (impropia)\n∫[−∞,∞] e^(−x²) dx = √π",
             fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")

plt.tight_layout()
plt.savefig("tecnicas_integracion.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: tecnicas_integracion.png")

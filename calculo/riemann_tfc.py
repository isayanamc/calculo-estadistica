"""
Módulo 4 - Sumas de Riemann, Integrales Definidas
        y Teorema Fundamental del Cálculo
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

¿QUÉ ES LA INTEGRAL DEFINIDA?
───────────────────────────────
La integral definida mide el ÁREA NETA bajo la curva f(x)
entre dos valores x = a y x = b.

"Neta" significa que las áreas por ENCIMA del eje x cuentan positivo
y las áreas por DEBAJO cuentan negativo.

CONSTRUCCIÓN MEDIANTE SUMAS DE RIEMANN:
  Para aproximar el área bajo f(x) en [a, b]:
    1) Dividir [a, b] en n subintervalos iguales de ancho Δx = (b−a)/n
    2) En cada subintervalo elegir un punto representativo xᵢ*
    3) Construir rectángulos de altura f(xᵢ*) y base Δx
    4) Sumar todas las áreas: Σ f(xᵢ*) · Δx

  Tipos de suma de Riemann según dónde se elige xᵢ*:
    • Suma izquierda:   xᵢ* = extremo izquierdo del subintervalo
    • Suma derecha:     xᵢ* = extremo derecho del subintervalo
    • Suma central:     xᵢ* = punto medio del subintervalo

  La integral definida es el LÍMITE cuando n → ∞:
    ∫[a,b] f(x) dx = lim n→∞  Σᵢ f(xᵢ*) · Δx

NOTACIÓN:
    ∫[a a b] f(x) dx
    a = límite inferior,  b = límite superior

TEOREMA FUNDAMENTAL DEL CÁLCULO (TFC):
  Es el resultado más importante del cálculo. Conecta la derivada
  (proceso de diferenciación) con la integral (proceso de integración),
  mostrando que son operaciones INVERSAS.

  Parte 1 — Derivada de una integral con límite variable:
    Si G(x) = ∫[a a x] f(t) dt,  entonces  G'(x) = f(x)
    "Derivar una integral respecto a su límite superior devuelve el integrando"

  Parte 2 — Evaluación de integrales definidas:
    Si F es antiderivada de f, entonces:
    ∫[a a b] f(x) dx = F(b) − F(a)

    Esto transforma el problema de calcular infinitos rectángulos
    en simplemente evaluar la antiderivada en los dos extremos.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sympy import *

x, t = symbols('x t')

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Sumas de Riemann
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  SUMAS DE RIEMANN")
print("=" * 60)
print("""
  Aproximación del área bajo f(x) = x² en [0, 2]
  Valor exacto: ∫[0,2] x² dx = [x³/3]₀² = 8/3 ≈ 2.6667
""")

def suma_riemann(f_num, a, b, n, tipo='central'):
    """
    Calcula la suma de Riemann con n rectángulos.
    tipo: 'izquierda', 'derecha', 'central'
    """
    dx = (b - a) / n
    puntos = np.linspace(a, b, n+1)

    if tipo == 'izquierda':
        xi = puntos[:-1]
    elif tipo == 'derecha':
        xi = puntos[1:]
    else:  # central
        xi = (puntos[:-1] + puntos[1:]) / 2

    return np.sum(f_num(xi) * dx)

f_num = lambda xv: xv**2
exacto = 8/3

print(f"  {'n':>6} {'Izquierda':>12} {'Derecha':>12} "
      f"{'Central':>12} {'Error Central':>14}")
print(f"  {'─'*60}")
for n in [4, 10, 50, 100, 500, 1000]:
    izq = suma_riemann(f_num, 0, 2, n, 'izquierda')
    der = suma_riemann(f_num, 0, 2, n, 'derecha')
    cen = suma_riemann(f_num, 0, 2, n, 'central')
    err = abs(cen - exacto)
    print(f"  {n:>6} {izq:>12.6f} {der:>12.6f} {cen:>12.6f} {err:>14.2e}")
print(f"\n  Valor exacto: {exacto:.6f}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Integrales definidas
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  INTEGRALES DEFINIDAS")
print("=" * 60)
print("""
  Usando el TFC Parte 2: ∫[a,b] f(x)dx = F(b) − F(a)
  Mostramos el proceso completo de evaluación.
""")

casos = [
    (x**2,              0,  2,    "x²        en [0, 2]"),
    (sin(x),            0,  pi,   "sin(x)    en [0, π]"),
    (exp(x),            0,  1,    "eˣ         en [0, 1]"),
    (1/x,               1,  exp(1), "1/x      en [1, e]"),
    (x**3 - 3*x,       -2,  2,   "x³−3x     en [−2, 2]"),
    (sqrt(x),           0,  4,   "√x         en [0, 4]"),
    (cos(x),            0,  pi/2, "cos(x)    en [0, π/2]"),
]

for f_expr, a, b, nombre in casos:
    F   = integrate(f_expr, x)
    F_b = F.subs(x, b)
    F_a = F.subs(x, a)
    resultado = simplify(F_b - F_a)

    print(f"  ∫ {nombre}")
    print(f"    Antiderivada: F(x) = {F}")
    print(f"    F({b}) − F({a}) = {F_b} − {F_a} = {resultado}")
    print(f"    Resultado: {float(resultado):.6f}\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Teorema Fundamental del Cálculo
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  TEOREMA FUNDAMENTAL DEL CÁLCULO")
print("=" * 60)
print("""
  TFC Parte 1: Si G(x) = ∫[a,x] f(t) dt  →  G'(x) = f(x)

  Derivar una integral respecto a su límite superior
  simplemente "devuelve" la función integrando evaluada en x.
  Con regla de la cadena: d/dx[∫[a,g(x)] f(t)dt] = f(g(x))·g'(x)
""")

ejemplos_tfc1 = [
    (t**2,      "t²",       "x²"),
    (sin(t),    "sin(t)",   "sin(x)"),
    (exp(t**2), "e^(t²)",   "e^(x²)"),
    (sqrt(t),   "√t",       "√x"),
]

print("  TFC Parte 1 — Derivada de integral con límite variable:")
for f_t, nombre_t, resultado_esperado in ejemplos_tfc1:
    G = integrate(f_t, (t, 0, x))
    Gp = diff(G, x)
    print(f"    G(x) = ∫[0,x] {nombre_t} dt")
    print(f"    G'(x) = {simplify(Gp)}  "
          f"(esperado: {resultado_esperado}) ✅\n")

print("""
  TFC Parte 2: ∫[a,b] f(x) dx = F(b) − F(a)
  (ya aplicado en la sección anterior)

  El TFC muestra que integración y derivación son INVERSAS:
    d/dx [∫[a,x] f(t) dt] = f(x)     (derivar deshace la integral)
    ∫[a,b] F'(x) dx = F(b) − F(a)   (integrar deshace la derivada)
""")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 4: Visualización
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Módulo 4 — Sumas de Riemann, Integral Definida y TFC",
             fontsize=14, fontweight='bold')

# ── Suma izquierda con 6 rectángulos ──
def graficar_riemann(ax, f_num, a, b, n, tipo, titulo, color):
    xv = np.linspace(a - 0.2, b + 0.2, 300)
    ax.plot(xv, f_num(xv), color='black', lw=2.5, zorder=5)
    dx = (b - a) / n
    puntos = np.linspace(a, b, n+1)
    if tipo == 'izquierda':
        xi = puntos[:-1]
    elif tipo == 'derecha':
        xi = puntos[1:]
    else:
        xi = (puntos[:-1] + puntos[1:]) / 2
    for xi_k in xi:
        h = f_num(xi_k)
        rect = patches.Rectangle((xi_k - (dx if tipo=='derecha' else 0),
                                   min(h, 0)),
                                  dx, abs(h),
                                  linewidth=1, edgecolor='black',
                                  facecolor=color, alpha=0.5)
        if tipo == 'izquierda':
            rect = patches.Rectangle((xi_k, min(h,0)), dx, abs(h),
                                      lw=1, edgecolor='black',
                                      facecolor=color, alpha=0.5)
        elif tipo == 'central':
            rect = patches.Rectangle((xi_k - dx/2, min(h,0)), dx, abs(h),
                                      lw=1, edgecolor='black',
                                      facecolor=color, alpha=0.5)
        ax.add_patch(rect)
    aprox = suma_riemann(f_num, a, b, n, tipo)
    ax.set_title(f"{titulo}\nAprox = {aprox:.4f}", fontsize=9)
    ax.set_xlabel("x"); ax.set_ylabel("f(x)")
    ax.grid(True, alpha=0.3)

graficar_riemann(axes[0,0], lambda xv: xv**2, 0, 2, 6,
                 'izquierda', "Suma Izquierda n=6\nf(x)=x²", '#E53935')
graficar_riemann(axes[0,1], lambda xv: xv**2, 0, 2, 6,
                 'derecha', "Suma Derecha n=6\nf(x)=x²", '#1565C0')
graficar_riemann(axes[0,2], lambda xv: xv**2, 0, 2, 6,
                 'central', "Suma Central n=6\nf(x)=x²", '#2E7D32')

# ── Convergencia de la suma de Riemann ──
ax = axes[1, 0]
ns = np.arange(1, 101)
exacto_val = 8/3
izqs = [suma_riemann(lambda xv: xv**2, 0, 2, n, 'izquierda') for n in ns]
cens = [suma_riemann(lambda xv: xv**2, 0, 2, n, 'central')   for n in ns]
ax.plot(ns, izqs, color='#E53935', lw=2, label="Suma Izquierda")
ax.plot(ns, cens, color='#2E7D32', lw=2, label="Suma Central")
ax.axhline(exacto_val, color='black', lw=2, ls='--',
           label=f"Exacto = {exacto_val:.4f}")
ax.set_title("Convergencia al valor exacto\n∫₀² x² dx = 8/3", fontsize=9)
ax.set_xlabel("n (número de rectángulos)")
ax.set_ylabel("Aproximación")
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

# ── Área neta: positiva y negativa ──
ax = axes[1, 1]
xv = np.linspace(-np.pi, 2*np.pi, 400)
yv = np.sin(xv)
ax.plot(xv, yv, color='black', lw=2.5, label="sin(x)")
ax.fill_between(xv, yv, 0, where=(yv > 0), alpha=0.4,
                color='#1565C0', label="Área positiva")
ax.fill_between(xv, yv, 0, where=(yv < 0), alpha=0.4,
                color='#E53935', label="Área negativa")
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Área NETA: positiva y negativa\n∫₋π^{2π} sin(x) dx", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# ── TFC Parte 1: G(x) = ∫₀ˣ t² dt = x³/3 ──
ax = axes[1, 2]
xv2 = np.linspace(0, 3, 300)
G_vals  = xv2**3 / 3       # ∫₀ˣ t² dt
Gp_vals = xv2**2            # G'(x) = x²
ax.plot(xv2, G_vals,  color='#1565C0', lw=2.5,
        label="G(x) = ∫₀ˣ t² dt = x³/3")
ax.plot(xv2, Gp_vals, color='#C62828', lw=2, ls='--',
        label="G'(x) = x²  (TFC Parte 1)")
ax.set_title("TFC Parte 1\nG(x)=∫₀ˣ t²dt  →  G'(x)=x²", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

plt.tight_layout()
plt.savefig("riemann_tfc.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: riemann_tfc.png")

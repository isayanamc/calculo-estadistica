"""
Módulo 5 - Métodos Numéricos de Integración
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

¿POR QUÉ MÉTODOS NUMÉRICOS?
──────────────────────────────
Muchas integrales no tienen solución algebraica en forma cerrada.
Por ejemplo, ∫ e^(−x²) dx, ∫ sin(x)/x dx o ∫ √(1+x⁴) dx
no se pueden expresar con funciones elementales.

En estos casos usamos MÉTODOS NUMÉRICOS: algoritmos que aproximan
el valor de la integral con la precisión que necesitemos.

MÉTODOS PRINCIPALES:
─────────────────────

  1. REGLA DEL TRAPECIO:
     Aproxima el área bajo la curva con trapecios en lugar de rectángulos.
     Cada trapecio tiene como lados los valores f(xᵢ) y f(xᵢ₊₁).

     Para n subintervalos con ancho h = (b−a)/n:
       T = h/2 · [f(x₀) + 2f(x₁) + 2f(x₂) + ... + 2f(xₙ₋₁) + f(xₙ)]
       T = (h/2) · [f(a) + f(b) + 2·Σᵢ₌₁ⁿ⁻¹ f(xᵢ)]

     Error: O(h²) — el error se reduce al cuadrado al reducir h a la mitad.

  2. REGLA DE SIMPSON 1/3:
     En lugar de líneas rectas (trapecios), usa PARÁBOLAS para aproximar
     la función en cada par de subintervalos.

     Requiere n PAR. Con h = (b−a)/n:
       S = h/3 · [f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ... + 4f(xₙ₋₁) + f(xₙ)]
       Patrón de coeficientes: 1, 4, 2, 4, 2, ..., 4, 1

     Error: O(h⁴) — mucho más preciso que el trapecio para el mismo h.

  3. REGLA DE SIMPSON 3/8:
     Usa polinomios cúbicos. Requiere n múltiplo de 3.
       S = 3h/8 · [f(x₀) + 3f(x₁) + 3f(x₂) + 2f(x₃) + ... + f(xₙ)]
       Patrón: 1, 3, 3, 2, 3, 3, 2, ..., 3, 3, 1

  4. CUADRATURA DE GAUSS:
     Elige los MEJORES puntos de evaluación (no igualmente espaciados)
     para maximizar la precisión con el mínimo número de evaluaciones.
     Para n puntos, integra exactamente polinomios de grado 2n−1.

COMPARACIÓN DE PRECISIÓN:
  Para la misma función y el mismo número de evaluaciones n:
    Riemann   < Trapecio < Simpson 1/3 < Simpson 3/8 < Gauss
  (menos preciso)                                  (más preciso)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sympy import *

x = symbols('x')

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Implementación de los métodos
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  MÉTODOS NUMÉRICOS DE INTEGRACIÓN")
print("=" * 60)

def trapecio(f, a, b, n):
    """
    Regla del Trapecio con n subintervalos.
    Aproxima el área con trapecios en cada subintervalo.
    """
    h  = (b - a) / n
    xv = np.linspace(a, b, n + 1)
    yv = f(xv)
    return h/2 * (yv[0] + 2*np.sum(yv[1:-1]) + yv[-1])

def simpson13(f, a, b, n):
    """
    Regla de Simpson 1/3 con n subintervalos (n debe ser par).
    Aproxima con parábolas — mucho más preciso que el trapecio.
    """
    if n % 2 != 0:
        n += 1   # asegurar que n sea par
    h  = (b - a) / n
    xv = np.linspace(a, b, n + 1)
    yv = f(xv)
    # Coeficientes: 1, 4, 2, 4, 2, ..., 4, 1
    coefs = np.ones(n + 1)
    coefs[1:-1:2] = 4   # índices impares → coeficiente 4
    coefs[2:-2:2] = 2   # índices pares intermedios → coeficiente 2
    return h/3 * np.dot(coefs, yv)

def simpson38(f, a, b, n):
    """
    Regla de Simpson 3/8 con n subintervalos (n múltiplo de 3).
    Usa polinomios cúbicos.
    """
    while n % 3 != 0:
        n += 1
    h  = (b - a) / n
    xv = np.linspace(a, b, n + 1)
    yv = f(xv)
    # Coeficientes: 1, 3, 3, 2, 3, 3, 2, ..., 3, 3, 1
    coefs = np.ones(n + 1)
    for i in range(1, n):
        if i % 3 == 0:
            coefs[i] = 2
        else:
            coefs[i] = 3
    return 3*h/8 * np.dot(coefs, yv)

def gauss_legendre(f, a, b, n=5):
    """
    Cuadratura de Gauss-Legendre con n puntos.
    Los puntos y pesos se calculan sobre [−1,1] y se transforman a [a,b].
    """
    nodos, pesos = np.polynomial.legendre.leggauss(n)
    # Transformación: t ∈ [−1,1] → x ∈ [a,b]
    xv = 0.5*(b - a)*nodos + 0.5*(b + a)
    return 0.5*(b - a) * np.dot(pesos, f(xv))

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Comparación de métodos
# ─────────────────────────────────────────────────────────────
print("""
  Función de prueba: f(x) = x² en [0, 2]
  Valor exacto:  ∫₀² x² dx = 8/3 ≈ 2.666667
""")

f_test  = lambda xv: xv**2
exacto  = 8/3

print(f"  {'Método':<20} {'n=4':>10} {'n=10':>10} "
      f"{'n=100':>10} {'Error n=10':>12}")
print(f"  {'─'*58}")

metodos = [
    ("Trapecio",     trapecio),
    ("Simpson 1/3",  simpson13),
    ("Simpson 3/8",  simpson38),
]

resultados_metodos = {}
for nombre, metodo in metodos:
    r4   = metodo(f_test, 0, 2, 4)
    r10  = metodo(f_test, 0, 2, 10)
    r100 = metodo(f_test, 0, 2, 100)
    err  = abs(r10 - exacto)
    resultados_metodos[nombre] = (r4, r10, r100, err)
    print(f"  {nombre:<20} {r4:>10.6f} {r10:>10.6f} {r100:>10.6f} {err:>12.2e}")

# Gauss con distintos n
print(f"\n  {'Gauss (n pts)':<20} ", end="")
for n_gauss in [2, 3, 5, 10]:
    rg = gauss_legendre(f_test, 0, 2, n_gauss)
    err_g = abs(rg - exacto)
    print(f"n={n_gauss}: {rg:.6f} (err={err_g:.2e})   ", end="")
print()

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Convergencia de errores
# ─────────────────────────────────────────────────────────────
print("""
  Análisis de convergencia:
  Cómo disminuye el error a medida que aumenta n
""")
print(f"  {'n':>6} {'Error Trapecio':>16} {'Error Simpson 1/3':>18}")
print(f"  {'─'*44}")
for n in [2, 4, 8, 16, 32, 64]:
    et = abs(trapecio(f_test, 0, 2, n)   - exacto)
    es = abs(simpson13(f_test, 0, 2, n)  - exacto)
    print(f"  {n:>6} {et:>16.2e} {es:>18.2e}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 4: Integrales sin solución analítica
# ─────────────────────────────────────────────────────────────
print("""
  Integrales que NO tienen solución algebraica cerrada:
  Solo podemos calcularlas numéricamente.
""")

casos_sin_sol = [
    (lambda xv: np.exp(-xv**2),    0, 1,    "∫₀¹ e^(−x²) dx",     "≈0.7468  (relacionada a √π/2)"),
    (lambda xv: np.sin(xv)/xv,     0.001, np.pi, "∫₀^π sin(x)/x dx",  "≈1.8519  (función sinc)"),
    (lambda xv: np.sqrt(1+xv**4),  0, 1,    "∫₀¹ √(1+x⁴) dx",     "≈1.0894  (longitud de arco)"),
    (lambda xv: 1/np.log(xv),      2, 3,    "∫₂³ 1/ln(x) dx",     "≈0.8690  (integral logarítmica)"),
]

for f_n, a_n, b_n, nombre, nota in casos_sin_sol:
    t_val = trapecio(f_n, a_n, b_n, 1000)
    s_val = simpson13(f_n, a_n, b_n, 1000)
    g_val = gauss_legendre(f_n, a_n, b_n, 10)
    print(f"  {nombre}  {nota}")
    print(f"    Trapecio (n=1000): {t_val:.6f}")
    print(f"    Simpson  (n=1000): {s_val:.6f}")
    print(f"    Gauss    (n=10):   {g_val:.6f}\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 5: Visualización
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(16, 11))
fig.suptitle("Módulo 5 — Métodos Numéricos de Integración",
             fontsize=14, fontweight='bold', y=0.98)

f_vis = lambda xv: xv**2
a_v, b_v = 0, 2

# ── Regla del Trapecio ──
ax = axes[0, 0]
n_vis = 6
xv = np.linspace(a_v, b_v, 300)
ax.plot(xv, f_vis(xv), color='black', lw=2.5, zorder=5, label="f(x)=x²")
h_v = (b_v - a_v) / n_vis
xi_v = np.linspace(a_v, b_v, n_vis + 1)
for i in range(n_vis):
    trap = patches.Polygon(
        [(xi_v[i], 0), (xi_v[i+1], 0),
         (xi_v[i+1], f_vis(xi_v[i+1])), (xi_v[i], f_vis(xi_v[i]))],
        closed=True, facecolor='#BBDEFB', edgecolor='#1565C0',
        lw=1.5, alpha=0.7)
    ax.add_patch(trap)
aprox_t = trapecio(f_vis, a_v, b_v, n_vis)
ax.set_title(f"Trapecio (n={n_vis}) — Aprox={aprox_t:.4f}",
             fontsize=8)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# ── Regla de Simpson 1/3 ──
ax = axes[0, 1]
ax.plot(xv, f_vis(xv), color='black', lw=2.5, zorder=5, label="f(x)=x²")
n_s = 6
h_s = (b_v - a_v) / n_s
xi_s = np.linspace(a_v, b_v, n_s + 1)
colores_s = ['#BBDEFB', '#FFCDD2']
for i in range(0, n_s, 2):
    x0, x1, x2 = xi_s[i], xi_s[i+1], xi_s[i+2]
    y0, y1, y2 = f_vis(x0), f_vis(x1), f_vis(x2)
    # Parábola que pasa por los 3 puntos
    xp = np.linspace(x0, x2, 100)
    # Interpolación de Lagrange
    yp = (y0*(xp-x1)*(xp-x2)/((x0-x1)*(x0-x2)) +
          y1*(xp-x0)*(xp-x2)/((x1-x0)*(x1-x2)) +
          y2*(xp-x0)*(xp-x1)/((x2-x0)*(x2-x1)))
    ax.fill_between(xp, yp, alpha=0.4,
                    color=colores_s[(i//2) % 2])
    ax.plot(xp, yp, color='#C62828', lw=1.2, ls='--')
aprox_s = simpson13(f_vis, a_v, b_v, n_s)
ax.set_title(f"Simpson 1/3 (n={n_s}) — Aprox={aprox_s:.6f}",
             fontsize=8)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# ── Puntos de Gauss ──
ax = axes[0, 2]
ax.plot(xv, f_vis(xv), color='black', lw=2.5, label="f(x)=x²")
ax.fill_between(xv, f_vis(xv), alpha=0.15, color='#2E7D32')
for n_g, color, marker in [(2,'#E53935','o'),(3,'#1565C0','s'),(5,'#2E7D32','^')]:
    nodos, _ = np.polynomial.legendre.leggauss(n_g)
    xg = 0.5*(b_v-a_v)*nodos + 0.5*(b_v+a_v)
    ax.scatter(xg, f_vis(xg), color=color, s=100, zorder=5,
               marker=marker, label=f"Gauss n={n_g}")
ax.set_title("Gauss — Puntos óptimos de evaluación", fontsize=8)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# ── Convergencia del error ──
ax = axes[1, 0]
ns_conv = np.arange(2, 101, 2)
err_t = [abs(trapecio(f_vis, a_v, b_v, n) - exacto) for n in ns_conv]
err_s = [abs(simpson13(f_vis, a_v, b_v, n) - exacto) for n in ns_conv]
ax.semilogy(ns_conv, err_t, color='#E53935', lw=2, label="Trapecio  O(h²)")
ax.semilogy(ns_conv, err_s, color='#1565C0', lw=2, label="Simpson   O(h⁴)")
ax.set_title("Convergencia del error (∫₀² x² dx)", fontsize=8)
ax.set_xlabel("n (subintervalos)"); ax.set_ylabel("Error absoluto (log)")
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

# ── Integral sin solución: e^(-x²) ──
ax = axes[1, 1]
xv2 = np.linspace(0, 1, 300)
yv2 = np.exp(-xv2**2)
ax.plot(xv2, yv2, color='black', lw=2.5, label="e^(−x²)")
ax.fill_between(xv2, yv2, alpha=0.25, color='#6A1B9A',
                label=f"Área ≈ {simpson13(lambda xv: np.exp(-xv**2), 0, 1, 100):.4f}")
ax.set_title("Integral sin solución exacta\n∫₀¹ e^(-x²) dx",
             fontsize=8)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("f(x)")

# ── Comparación de métodos en barras ──
ax = axes[1, 2]
n_comp = 10
metodos_nombres = ['Trapecio', 'Simpson 1/3', 'Simpson 3/8', 'Gauss (n=5)']
valores = [
    trapecio(f_vis, a_v, b_v, n_comp),
    simpson13(f_vis, a_v, b_v, n_comp),
    simpson38(f_vis, a_v, b_v, n_comp),
    gauss_legendre(f_vis, a_v, b_v, 5),
]
errores = [abs(v - exacto) for v in valores]
colores_bar = ['#E53935', '#1565C0', '#2E7D32', '#6A1B9A']
bars = ax.bar(metodos_nombres, errores, color=colores_bar, alpha=0.8)
ax.set_yscale('log')
for bar, err in zip(bars, errores):
    ax.text(bar.get_x() + bar.get_width()/2, err*2,
            f'{err:.2e}', ha='center', va='bottom', fontsize=7)
ax.set_title(f"Comparación de errores (n={n_comp})",
             fontsize=8)
ax.set_ylabel("Error absoluto (log)"); ax.grid(True, alpha=0.3, axis='y')
plt.setp(ax.get_xticklabels(), rotation=15, ha='right', fontsize=8)

plt.subplots_adjust(left=0.07, right=0.97, top=0.93, bottom=0.08,
                    hspace=0.45, wspace=0.30)
plt.savefig("metodos_numericos_integracion.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n[OK]  Gráfica guardada: metodos_numericos_integracion.png")

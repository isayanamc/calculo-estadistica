"""
Módulo 6 - Series de Potencias, Taylor y Maclaurin
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

QUE ES UNA SERIE DE POTENCIAS?
--------------------------------
Una serie de potencias centrada en x = a es una serie de la forma:
    sum_{n=0}^{inf} cₙ · (x-a)^n = c0 + c1(x-a) + c2(x-a)^2 + ...

Es como un "polinomio infinito" donde los coeficientes cₙ se eligen
para que la serie represente exactamente a una funcion f(x).

RADIO DE CONVERGENCIA:
  Cada serie de potencias tiene un RADIO DE CONVERGENCIA R:
    |x - a| < R  →  la serie converge
    |x - a| > R  →  la serie diverge
    |x - a| = R  →  hay que analizar caso por caso

  El radio R se calcula con el criterio del cociente:
    1/R = lim n→inf |c_{n+1}/cₙ|

SERIES DE TAYLOR:
-----------------
Si f(x) tiene derivadas de todos los ordenes en x = a, su
serie de Taylor centrada en a es:

    f(x) = sum_{n=0}^{inf} f^{(n)}(a)/n! · (x-a)^n

    = f(a) + f'(a)(x-a) + f''(a)/2!(x-a)^2 + f'''(a)/3!(x-a)^3 + ...

La idea es construir un polinomio que "imite" a f(x) cerca de x = a:
  - El termino n=0 iguala el valor de f en a
  - El termino n=1 iguala la pendiente de f en a
  - El termino n=2 iguala la concavidad de f en a
  - Y asi sucesivamente para cada orden de derivada

SERIES DE MACLAURIN (caso especial con a = 0):
    f(x) = sum_{n=0}^{inf} f^{(n)}(0)/n! · x^n

SERIES FUNDAMENTALES (Maclaurin):
  e^x     = 1 + x + x^2/2! + x^3/3! + ... = sum x^n/n!
  sin(x)  = x - x^3/3! + x^5/5! - ... = sum (-1)^n x^{2n+1}/(2n+1)!
  cos(x)  = 1 - x^2/2! + x^4/4! - ... = sum (-1)^n x^{2n}/(2n)!
  ln(1+x) = x - x^2/2 + x^3/3 - ... = sum (-1)^{n+1} x^n/n
  1/(1-x) = 1 + x + x^2 + x^3 + ... = sum x^n  (para |x|<1)

APLICACION EN COMPUTACION:
  Los procesadores no calculan sin(x) ni e^x directamente.
  Usan aproximaciones polinomiales de Taylor truncadas.
  El numero de terminos determina la precision del resultado.
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = symbols('x')

# ─────────────────────────────────────────────────────────────
# SECCION 1: Series de Maclaurin de funciones comunes
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  SERIES DE MACLAURIN")
print("=" * 60)
print("""
  Se calculan evaluando f^{(n)}(0) para cada n y dividiendo entre n!
""")

funciones_taylor = [
    (exp(x),    "e^x",    10),
    (sin(x),    "sin(x)", 10),
    (cos(x),    "cos(x)", 10),
    (log(1+x),  "ln(1+x)", 8),
    (1/(1-x),   "1/(1-x)", 8),
    (sqrt(1+x), "sqrt(1+x)", 6),
]

for f_expr, nombre, n_max in funciones_taylor:
    serie = series(f_expr, x, 0, n_max)
    print(f"  f(x) = {nombre}")
    print(f"  Serie = {serie}")

    # Verificacion: evaluar en x=0.5 y comparar con valor real
    x_val = 0.5
    poly  = serie.removeO()
    aprox = float(poly.subs(x, x_val))
    real  = float(f_expr.subs(x, x_val))
    print(f"  Evaluacion en x=0.5:  Serie={aprox:.8f},  Exacto={real:.8f},  "
          f"Error={abs(aprox-real):.2e}")
    print()

# ─────────────────────────────────────────────────────────────
# SECCION 2: Series de Taylor centradas en a != 0
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  SERIES DE TAYLOR (centradas en a != 0)")
print("=" * 60)
print("""
  Cuando queremos aproximar f cerca de un punto x = a != 0,
  centramos la serie ahi para mejor precision en esa region.
""")

a_vals = [
    (sin(x), "sin(x)", pi/4, 6),
    (log(x), "ln(x)",  1,    6),
    (exp(x), "e^x",    1,    6),
]

for f_expr, nombre, a_val, n_max in a_vals:
    serie = series(f_expr, x, a_val, n_max)
    poly  = serie.removeO()
    print(f"  f(x) = {nombre}  centrada en x = {a_val}")
    print(f"  Serie = {serie}")

    # Evaluar en un punto cercano a 'a'
    x_test = float(a_val) + 0.1
    aprox  = float(poly.subs(x, x_test))
    real   = float(f_expr.subs(x, x_test))
    print(f"  En x={x_test:.2f}:  Aprox={aprox:.8f},  Exacto={real:.8f},  "
          f"Error={abs(aprox-real):.2e}")
    print()

# ─────────────────────────────────────────────────────────────
# SECCION 3: Convergencia segun numero de terminos
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  CONVERGENCIA SEGUN NUMERO DE TERMINOS")
print("=" * 60)
print("""
  Mostramos como mejora la aproximacion al agregar mas terminos.
  Funcion: e^x  en x = 1  (valor exacto = e ≈ 2.71828...)
""")

print(f"  {'Terminos':>10} {'Aproximacion':>14} {'Error':>12}")
print(f"  {'─'*40}")
x_val = 1.0
exacto_e = np.e
suma = 0
for k_val in range(11):
    suma += x_val**k_val / float(factorial(k_val))
    err = abs(suma - exacto_e)
    print(f"  n={k_val:<8} {suma:>14.10f} {err:>12.2e}")

# ─────────────────────────────────────────────────────────────
# SECCION 4: Radio de convergencia
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  RADIO DE CONVERGENCIA")
print("=" * 60)
print("""
  El radio de convergencia R determina en que intervalo
  converge la serie de potencias.

  Criterio: 1/R = lim n→inf |c_{n+1}/cₙ|
""")

series_radio = [
    ("sum x^n / n!   (e^x)",    "R = inf  (converge para todo x)"),
    ("sum x^n        (1/(1-x))","R = 1    (converge para |x| < 1)"),
    ("sum x^n / n    (ln(1+x))","R = 1    (converge para |x| < 1)"),
    ("sum n! * x^n",            "R = 0    (solo converge en x=0)"),
    ("sum x^n / n^2",           "R = 1    (converge en [-1, 1])"),
]

for serie_desc, radio in series_radio:
    print(f"  {serie_desc}")
    print(f"    --> {radio}\n")

# ─────────────────────────────────────────────────────────────
# SECCION 5: Visualizacion
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle("Modulo 6 -- Series de Potencias, Taylor y Maclaurin",
             fontsize=14, fontweight='bold')

xv = np.linspace(-np.pi, np.pi, 400)
colores = ['#E53935', '#1565C0', '#2E7D32', '#6A1B9A', '#E65100']

# Aproximaciones de sin(x) con distintos ordenes
ax = axes[0, 0]
ax.plot(xv, np.sin(xv), 'k-', lw=3, label="sin(x)  (exacta)")
for n_ord, color in [(1, colores[0]), (3, colores[1]),
                     (5, colores[2]), (7, colores[3]), (9, colores[4])]:
    poly = series(sin(x), x, 0, n_ord+1).removeO()
    f_poly = lambdify(x, poly, 'numpy')
    yv = np.clip(f_poly(xv), -3, 3)
    ax.plot(xv, yv, '--', color=color, lw=1.8, label=f"Orden {n_ord}")
ax.set_ylim(-2.5, 2.5)
ax.set_title("Taylor de sin(x) en x=0\nMas terminos = mejor aprox.", fontsize=10)
ax.legend(fontsize=7, loc='lower right'); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# Aproximaciones de e^x
ax = axes[0, 1]
xv2 = np.linspace(-2, 3, 300)
ax.plot(xv2, np.exp(xv2), 'k-', lw=3, label="e^x  (exacta)")
for n_ord, color in [(1, colores[0]), (2, colores[1]),
                     (4, colores[2]), (6, colores[3])]:
    poly = series(exp(x), x, 0, n_ord+1).removeO()
    f_poly = lambdify(x, poly, 'numpy')
    yv = np.clip(f_poly(xv2), -1, 25)
    ax.plot(xv2, yv, '--', color=color, lw=1.8, label=f"Orden {n_ord}")
ax.set_title("Taylor de e^x en x=0", fontsize=10)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_ylim(-1, 20)

# Error de aproximacion segun orden
ax = axes[0, 2]
x_test_v = np.array([0.5, 1.0, 2.0, 3.0])
ordenes = range(1, 12)
for x_t, color, label in zip(x_test_v, colores, ['x=0.5','x=1.0','x=2.0','x=3.0']):
    errores = []
    for n_ord in ordenes:
        poly = series(sin(x), x, 0, n_ord+2).removeO()
        f_poly = lambdify(x, poly, 'numpy')
        err = abs(float(f_poly(x_t)) - np.sin(x_t))
        errores.append(err + 1e-16)
    ax.semilogy(list(ordenes), errores, 'o-', color=color, lw=2, ms=5, label=label)
ax.set_title("Error de Taylor de sin(x)\nsegun orden del polinomio", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("Orden del polinomio"); ax.set_ylabel("Error absoluto (log)")

# Radio de convergencia: ln(1+x)
ax = axes[1, 0]
xv3 = np.linspace(-0.99, 1.5, 400)
ax.plot(xv3[xv3 <= 0.99], np.log(1 + xv3[xv3 <= 0.99]),
        'k-', lw=3, label="ln(1+x)  (exacta)")
for n_ord, color in [(3, colores[0]), (6, colores[1]), (12, colores[2])]:
    poly = series(log(1+x), x, 0, n_ord+1).removeO()
    f_poly = lambdify(x, poly, 'numpy')
    yv = f_poly(xv3)
    ax.plot(xv3, np.clip(yv, -3, 3), '--', color=color, lw=1.8,
            label=f"Orden {n_ord}")
ax.axvline(-1, color='red', ls=':', lw=2, label="Limite radio |x|=1")
ax.axvline(1,  color='red', ls=':', lw=2)
ax.set_ylim(-2, 1.5)
ax.set_title("Taylor de ln(1+x)\nRadio de convergencia R=1", fontsize=10)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# Convergencia numerica de e
ax = axes[1, 1]
n_terms = np.arange(0, 15)
sumas_e = np.cumsum([1.0**k / float(factorial(k)) for k in n_terms])
errores_e = np.abs(sumas_e - np.e)
ax.semilogy(n_terms, errores_e + 1e-16, 'o-', color=colores[0],
            lw=2, ms=6, label="|S_n - e|")
ax.set_title("Convergencia de sum x^n/n!\nhacia e  (x=1)", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("Numero de terminos n")
ax.set_ylabel("Error absoluto (log)")

# Comparacion visual de cos(x)
ax = axes[1, 2]
xv4 = np.linspace(-2*np.pi, 2*np.pi, 500)
ax.plot(xv4, np.cos(xv4), 'k-', lw=3, label="cos(x)  (exacta)")
for n_ord, color in [(2, colores[0]), (4, colores[1]),
                     (8, colores[2]), (12, colores[3])]:
    poly = series(cos(x), x, 0, n_ord+1).removeO()
    f_poly = lambdify(x, poly, 'numpy')
    yv = np.clip(f_poly(xv4), -3, 3)
    ax.plot(xv4, yv, '--', color=color, lw=1.8, label=f"Orden {n_ord}")
ax.set_ylim(-2, 2)
ax.set_title("Taylor de cos(x) en x=0\nConvierte para todo x real", fontsize=10)
ax.legend(fontsize=7, loc='lower right'); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

plt.subplots_adjust(left=0.07, right=0.97, top=0.92, bottom=0.08,
                    hspace=0.45, wspace=0.32)
plt.savefig("taylor_maclaurin.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n[OK]  Grafica guardada: taylor_maclaurin.png")

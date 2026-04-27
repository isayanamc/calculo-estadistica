"""
Módulo 6 - Series y Criterios de Convergencia
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

QUE ES UNA SERIE?
------------------
Una serie es la SUMA de los terminos de una sucesion:
    S = a1 + a2 + a3 + a4 + ... = suma_{n=1}^{infinito} aₙ

Pero sumar infinitos numeros puede dar un resultado FINITO o INFINITO.

La clave es usar las SUMAS PARCIALES:
    S1 = a1
    S2 = a1 + a2
    S3 = a1 + a2 + a3
    Sₙ = a1 + a2 + ... + aₙ

La serie CONVERGE si lim n→∞ Sₙ = L  (numero finito)
La serie DIVERGE si ese limite no existe o es infinito.

SERIES IMPORTANTES:
-------------------
  1. Serie geometrica:  sum r^n  (n=0 a infinito)
     Converge si |r| < 1  →  suma = 1/(1-r)
     Diverge  si |r| >= 1

  2. Serie armonica:    sum 1/n  (n=1 a infinito)
     DIVERGE aunque sus terminos tienden a 0.
     Es el ejemplo clasico de que "terminos pequeños" no garantiza convergencia.

  3. Serie p:           sum 1/n^p  (n=1 a infinito)
     Converge si p > 1
     Diverge  si p <= 1

  4. Serie de Basel:    sum 1/n^2  (n=1 a infinito) = pi^2/6
     Resultado famoso demostrado por Euler en 1734.

CRITERIOS DE CONVERGENCIA:
---------------------------
Para decidir si una serie converge SIN calcular su suma exacta:

  1. Criterio del termino general (divergencia):
     Si lim n→∞ aₙ ≠ 0  →  la serie DIVERGE
     (condicion necesaria, no suficiente para convergencia)

  2. Criterio de la integral:
     Si f(x) es continua, positiva y decreciente, y aₙ = f(n):
     sum aₙ  converge  <=>  integral de f(x) converge

  3. Criterio de comparacion:
     Si 0 <= aₙ <= bₙ y sum bₙ converge → sum aₙ converge
     Si aₙ >= bₙ >= 0 y sum bₙ diverge  → sum aₙ diverge

  4. Criterio del cociente (d'Alembert):
     L = lim n→∞ |a_{n+1} / aₙ|
     L < 1  →  converge absolutamente
     L > 1  →  diverge
     L = 1  →  no concluye (usar otro criterio)

  5. Criterio de la raiz (Cauchy):
     L = lim n→∞ |aₙ|^(1/n)
     L < 1  →  converge absolutamente
     L > 1  →  diverge
     L = 1  →  no concluye

  6. Criterio de Leibniz (series alternantes):
     Si aₙ > 0, aₙ es decreciente, y lim aₙ = 0:
     entonces sum (-1)^n * aₙ  CONVERGE
"""

import numpy as np
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
import matplotlib.pyplot as plt
from sympy import *

n, k = symbols('n k', positive=True, integer=True)

# ─────────────────────────────────────────────────────────────
# SECCION 1: Series geometricas
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  SERIES GEOMETRICAS")
print("=" * 60)
print("""
  sum_{n=0}^{inf} r^n = 1/(1-r)   si |r| < 1

  Esta es la unica formula de suma cerrada que tenemos
  para una serie infinita de forma directa.
  Todas las demas requieren criterios para saber si convergen.
""")

razones = [Rational(1,2), Rational(1,3), Rational(2,3), -Rational(1,2), 1, Rational(3,2)]
for r_val in razones:
    s = Sum(r_val**k, (k, 0, oo))
    resultado = s.doit()
    converge = resultado.is_finite
    print(f"  r = {str(r_val):<8} sum r^n = {str(resultado):<20} "
          f"{'[CONVERGE]' if converge else '[DIVERGE]'}")

# ─────────────────────────────────────────────────────────────
# SECCION 2: Series p y serie armonica
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  SERIE P Y SERIE ARMONICA")
print("=" * 60)
print("""
  Serie p:  sum_{n=1}^{inf} 1/n^p
    Converge si p > 1
    Diverge  si p <= 1

  La serie armonica (p=1) es el ejemplo clasico de una serie
  que DIVERGE aunque sus terminos aₙ = 1/n → 0.
  Esto demuestra que aₙ → 0 es NECESARIO pero NO SUFICIENTE
  para que la serie converja.

  La serie de Basel (p=2) da pi^2/6 — resultado sorprendente
  que conecta la suma de cuadrados con el numero pi.
""")

for p_val in [Rational(1,2), 1, Rational(3,2), 2, 3]:
    s = Sum(1/n**p_val, (n, 1, oo))
    resultado = s.doit()
    converge  = resultado.is_finite
    print(f"  p = {str(p_val):<6} sum 1/n^{str(p_val)} = {str(simplify(resultado)):<20} "
          f"{'[CONVERGE]' if converge else '[DIVERGE (armonica)]'}")

# ─────────────────────────────────────────────────────────────
# SECCION 3: Criterios de convergencia
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  CRITERIOS DE CONVERGENCIA")
print("=" * 60)

series_criterios = [
    # (a_n,               nombre,              criterio)
    (1/n**2,             "1/n^2",              "Serie p (p=2>1)"),
    (1/factorial(n),     "1/n!",               "Criterio del cociente"),
    (n**n/factorial(n),  "n^n/n!",             "Criterio de la raiz"),
    (1/(n*log(n)),       "1/(n*ln(n))",         "Criterio de la integral"),
    ((-1)**n/n,          "(-1)^n/n",            "Criterio de Leibniz"),
    (n**2/2**n,          "n^2/2^n",             "Criterio del cociente"),
    (1/(n*(n+1)),        "1/(n(n+1))",          "Series telescopicas"),
]

for a_n, nombre, criterio in series_criterios:
    print(f"\n  Serie: sum {nombre}")
    print(f"  Criterio aplicado: {criterio}")

    # Limite del termino general
    try:
        lim_an = limit(a_n, n, oo)
    except Exception:
        lim_an = None
    if lim_an == 0:
        print(f"  lim n→inf a_n = 0  (condicion necesaria [OK])")
    elif lim_an is None:
        print(f"  lim n→inf |a_n| = 0  (serie alternante, condicion [OK])")
    else:
        print(f"  lim n→inf a_n = {lim_an}  (DIVERGE - terminos no → 0)")

    # Criterio del cociente si aplica
    if criterio in ["Criterio del cociente", "Serie p (p=2>1)"]:
        try:
            a_n1 = a_n.subs(n, n+1)
            cociente = simplify(a_n1 / a_n)
            L = limit(Abs(cociente), n, oo)
            if L != oo:
                decision = "CONVERGE" if L < 1 else ("DIVERGE" if L > 1 else "Indeterminado")
                print(f"  |a_{{n+1}}/a_n| → {L}  →  {decision}")
        except Exception:
            pass

    # Resultado via SymPy
    try:
        resultado = Sum(a_n, (n, 1, oo)).doit()
        resultado_s = simplify(resultado)
        converge = resultado_s.is_finite
        print(f"  Suma exacta: {resultado_s}  "
              f"{'[CONVERGE]' if converge else '[DIVERGE]'}")
        if converge:
            print(f"  Valor numerico: {float(resultado_s.evalf()):.6f}")
    except Exception:
        print(f"  (Suma no elemental — se determina solo convergencia)")

# ─────────────────────────────────────────────────────────────
# SECCION 4: Sumas parciales y visualizacion de convergencia
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  SUMAS PARCIALES — VISUALIZACION DE CONVERGENCIA")
print("=" * 60)
print("""
  Calculamos Sₙ = sum_{k=1}^{n} a_k para valores crecientes de n
  y observamos si la sucesion de sumas parciales converge.
""")

def sumas_parciales(a_func, n_max, nombre, exacto=None):
    ns = np.arange(1, n_max+1)
    sumas = np.cumsum(a_func(ns))
    print(f"  sum {nombre}:")
    for i in [4, 9, 49, 99, 499]:
        if i < len(sumas):
            print(f"    S_{i+1:>4} = {sumas[i]:.8f}", end="")
            if exacto:
                print(f"   (error = {abs(sumas[i]-exacto):.2e})", end="")
            print()
    if exacto:
        print(f"    Valor exacto = {exacto:.8f}")
    print()
    return ns, sumas

ns1, s1 = sumas_parciales(lambda x: 1/x**2,     500, "1/n^2",    np.pi**2/6)
ns2, s2 = sumas_parciales(lambda x: 1/x,        500, "1/n  (armonica - diverge)")
ns3, s3 = sumas_parciales(lambda x: 1/2**x,     500, "(1/2)^n",  1.0)
ns4, s4 = sumas_parciales(lambda x: (-1)**(x+1)/x, 500, "(-1)^{n+1}/n", np.log(2))

# ─────────────────────────────────────────────────────────────
# SECCION 5: Visualizacion
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle("Modulo 6 -- Series y Criterios de Convergencia",
             fontsize=14, fontweight='bold')

colores = ['#1565C0', '#C62828', '#2E7D32', '#6A1B9A', '#E65100']

# Serie geometrica — convergencia segun r
ax = axes[0, 0]
nv = np.arange(0, 20)
for r_v, color, label in [
    (0.5, colores[0], "r=0.5 → suma=2"),
    (0.8, colores[1], "r=0.8 → suma=5"),
    (0.9, colores[2], "r=0.9 → suma=10"),
]:
    sumas_geom = np.cumsum(r_v**nv)
    ax.plot(nv, sumas_geom, 'o-', color=color, lw=1.5, ms=4, label=label)
ax.axhline(2,  color=colores[0], lw=1, ls='--', alpha=0.5)
ax.axhline(5,  color=colores[1], lw=1, ls='--', alpha=0.5)
ax.axhline(10, color=colores[2], lw=1, ls='--', alpha=0.5)
ax.set_title("Serie geometrica sum r^n\nSumas parciales segun r", fontsize=10)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("n"); ax.set_ylabel("Suma parcial S_n")

# Serie p — convergente vs divergente
ax = axes[0, 1]
nv2 = np.arange(1, 200)
for p_v, color, label, exacto_p in [
    (2, colores[0], "p=2 (converge: pi^2/6)", np.pi**2/6),
    (3, colores[1], "p=3 (converge: pi^4/90^{1/2})", np.pi**4/90),
]:
    sp = np.cumsum(1/nv2**p_v)
    ax.plot(nv2, sp, '-', color=color, lw=2, label=label)
    ax.axhline(exacto_p, color=color, lw=1.5, ls='--', alpha=0.6)
ax.set_title("Serie p convergente\nSumas parciales de 1/n^p", fontsize=10)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("n"); ax.set_ylabel("S_n")

# Serie armonica — divergencia lenta
ax = axes[0, 2]
nv3 = np.arange(1, 2001)
s_arm = np.cumsum(1/nv3)
ax.plot(nv3, s_arm, '-', color=colores[2], lw=2, label="sum 1/n (armonica)")
ax.plot(nv3, np.log(nv3), '--', color='red', lw=2,
        label="ln(n)  (asintota)")
ax.set_title("Serie armonica — DIVERGE\npero muy lentamente", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("n"); ax.set_ylabel("S_n")

# Sumas parciales de 1/n^2 convergiendo a pi^2/6
ax = axes[1, 0]
ax.plot(ns1, s1, '-', color=colores[0], lw=2, label="S_n = sum 1/k^2")
ax.axhline(np.pi**2/6, color='red', lw=2, ls='--',
           label=f"pi^2/6 = {np.pi**2/6:.6f}")
ax.fill_between(ns1, s1, np.pi**2/6, alpha=0.15, color='red',
                label="Error restante")
ax.set_title("sum 1/n^2 → pi^2/6\n(serie de Basel, Euler 1734)", fontsize=10)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("n"); ax.set_ylabel("S_n")

# Serie alternante de Leibniz
ax = axes[1, 1]
ax.plot(ns4, s4, '-', color=colores[3], lw=2,
        label="S_n = sum (-1)^{n+1}/n")
ax.axhline(np.log(2), color='red', lw=2, ls='--',
           label=f"ln(2) = {np.log(2):.6f}")
ax.set_title("Serie alternante\nsum (-1)^{n+1}/n → ln(2)", fontsize=10)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("n"); ax.set_ylabel("S_n")
ax.set_ylim(0.5, 0.9)

# Comparacion de velocidades de convergencia
ax = axes[1, 2]
nv4 = np.arange(1, 51)
err_geom = np.abs(np.cumsum((0.5)**nv4) - 1.0)
err_p2   = np.abs(np.cumsum(1/nv4**2) - np.pi**2/6)
err_p3   = np.abs(np.cumsum(1/nv4**3) - np.pi**4/90)  # aproximado
ax.semilogy(nv4, err_geom, 'o-', color=colores[0], lw=2, ms=3,
            label="Geometrica (r=1/2)")
ax.semilogy(nv4, err_p2,   's-', color=colores[1], lw=2, ms=3,
            label="Serie p (p=2)")
ax.semilogy(nv4, err_p3,   '^-', color=colores[2], lw=2, ms=3,
            label="Serie p (p=3)")
ax.set_title("Velocidad de convergencia\n|S_n - L| (escala log)", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("n"); ax.set_ylabel("Error |S_n - L|")

plt.subplots_adjust(left=0.07, right=0.97, top=0.92, bottom=0.08,
                    hspace=0.45, wspace=0.32)
plt.savefig("series_criterios.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n[OK]  Grafica guardada: series_criterios.png")

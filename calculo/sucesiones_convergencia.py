"""
Módulo 6 - Sucesiones y Convergencia
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

QUE ES UNA SUCESION?
---------------------
Una sucesion es una lista ORDENADA e INFINITA de numeros:
    a1, a2, a3, a4, ...

Cada elemento aₙ se genera mediante una FORMULA o REGLA que depende
del indice n (n = 1, 2, 3, ...).

Ejemplos:
  aₙ = 1/n        → 1, 1/2, 1/3, 1/4, ...     (decreciente hacia 0)
  aₙ = (-1)ⁿ      → -1, 1, -1, 1, ...          (oscilante)
  aₙ = n²         → 1, 4, 9, 16, ...            (creciente sin limite)
  aₙ = (1+1/n)ⁿ   → 2, 2.25, 2.37, ..., e      (converge a e)

CONVERGENCIA DE SUCESIONES:
----------------------------
Una sucesion {aₙ} CONVERGE si existe un numero finito L tal que:
    lim n→∞  aₙ = L

Esto significa que a partir de cierto n, todos los terminos
de la sucesion estan arbitrariamente cerca de L.

Si no existe ese limite, la sucesion DIVERGE.

TIPOS DE DIVERGENCIA:
  - Diverge a +∞: los terminos crecen sin limite   (aₙ = n²)
  - Diverge a -∞: los terminos decrecen sin limite  (aₙ = -n)
  - Diverge por oscilacion: los terminos no se estabilizan  (aₙ = (-1)ⁿ)

TIPOS DE SUCESIONES:
  - Monotona creciente:  a1 <= a2 <= a3 <= ...
  - Monotona decreciente: a1 >= a2 >= a3 >= ...
  - Acotada: existe M tal que |aₙ| <= M para todo n
  - Teorema: toda sucesion monotona y acotada CONVERGE

SUCESIONES IMPORTANTES EN COMPUTACION:
  - aₙ = (1 + 1/n)ⁿ  → converge a e (base del logaritmo natural)
  - Sucesion de Fibonacci: 1,1,2,3,5,8,13,... → razon aurea φ
  - aₙ = 1/2ⁿ → convergencia geometrica (complejidad O(log n))
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

n, k = symbols('n k', positive=True, integer=True)

# ─────────────────────────────────────────────────────────────
# SECCION 1: Definicion y primeros terminos
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  SUCESIONES — DEFINICION Y PRIMEROS TERMINOS")
print("=" * 60)
print("""
  Para cada sucesion mostramos:
    - Los primeros 8 terminos
    - El limite cuando n → infinito
    - Si converge o diverge
""")

sucesiones = [
    (1/n,               "1/n",              "Converge a 0",         "0"),
    ((-1)**n / n,       "(-1)^n / n",       "Converge a 0",         "0"),
    (n / (n + 1),       "n/(n+1)",          "Converge a 1",         "1"),
    ((n**2 + 1)/(2*n**2),"(n^2+1)/(2n^2)", "Converge a 1/2",       "1/2"),
    ((-1)**n,           "(-1)^n",            "Diverge (oscila)",     "no existe"),
    (n**2 / exp(n),     "n^2 / e^n",        "Converge a 0",         "0"),
    ((1 + 1/n)**n,      "(1 + 1/n)^n",      "Converge a e",         "e"),
    (Rational(1,2)**n,  "(1/2)^n",          "Converge a 0",         "0"),
]

for formula, nombre, comportamiento, lim_str in sucesiones:
    terminos = [float(formula.subs(n, i).evalf()) for i in range(1, 9)]
    terminos_str = ", ".join([f"{t:.4f}" for t in terminos])
    print(f"  a_n = {nombre}")
    print(f"    Terminos: {terminos_str}, ...")
    print(f"    lim n→∞ = {lim_str}")
    print(f"    Comportamiento: {comportamiento}")
    print()

# ─────────────────────────────────────────────────────────────
# SECCION 2: Tipos de sucesiones
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  TIPOS DE SUCESIONES")
print("=" * 60)
print("""
  Monotona creciente:  a_n <= a_{n+1}  para todo n
  Monotona decreciente: a_n >= a_{n+1}  para todo n
  Acotada superior: existe M tal que a_n <= M
  Acotada inferior: existe m tal que a_n >= m

  Teorema de Bolzano-Weierstrass:
    Toda sucesion monotona y acotada CONVERGE.
    No necesitamos calcular el limite — solo verificar
    que la sucesion es monotona y acotada.
""")

def analizar_sucesion(formula, nombre, n_max=20):
    terminos = np.array([float(formula.subs(n, i).evalf())
                         for i in range(1, n_max+1)])
    diferencias = np.diff(terminos)

    es_creciente  = np.all(diferencias >= -1e-10)
    es_decreciente = np.all(diferencias <= 1e-10)
    acotada_sup   = np.isfinite(terminos.max())
    acotada_inf   = np.isfinite(terminos.min())

    lim_val = limit(formula, n, oo)
    converge = lim_val.is_finite

    print(f"  a_n = {nombre}")
    print(f"    Monotona creciente:  {'[SI]' if es_creciente else '[NO]'}")
    print(f"    Monotona decreciente: {'[SI]' if es_decreciente else '[NO]'}")
    print(f"    Acotada:             {'[SI]' if (acotada_sup and acotada_inf) else '[NO]'}")
    print(f"    lim n→∞ = {lim_val}")
    print(f"    Conclusion:          {'CONVERGE [OK]' if converge else 'DIVERGE [X]'}")
    print()
    return terminos

casos_tipo = [
    (1/n,               "1/n"),
    (n/(n+1),           "n/(n+1)"),
    (Rational(1,2)**n,  "(1/2)^n"),
    (log(n)/n,          "ln(n)/n"),
]

terminos_guardados = {}
for formula, nombre in casos_tipo:
    terminos_guardados[nombre] = analizar_sucesion(formula, nombre)

# ─────────────────────────────────────────────────────────────
# SECCION 3: Sucesion de Fibonacci y la razon aurea
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  SUCESION DE FIBONACCI Y LA RAZON AUREA")
print("=" * 60)
print("""
  La sucesion de Fibonacci se define por recurrencia:
    F1 = 1,  F2 = 1,  Fn = F_{n-1} + F_{n-2}  para n >= 3

  Es decir: cada termino es la SUMA de los dos anteriores.
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

  Propiedad notable: el cociente F_{n+1}/Fn converge a la RAZON AUREA:
    phi = (1 + sqrt(5)) / 2 ≈ 1.61803...

  La razon aurea aparece en arte, arquitectura, biologia y en
  analisis de algoritmos (arboles AVL, busqueda de Fibonacci).
""")

fib = [1, 1]
for i in range(18):
    fib.append(fib[-1] + fib[-2])

razon_aurea = (1 + np.sqrt(5)) / 2
razones = [fib[i+1]/fib[i] for i in range(len(fib)-1)]

print(f"  Fibonacci: {fib[:12]}, ...")
print(f"  Razones F_{{n+1}}/Fn:")
for i in range(0, 12, 3):
    print(f"    F{i+2}/F{i+1} = {fib[i+1]}/{fib[i]} = {razones[i]:.6f}")
print(f"  Convergencia a phi = (1+sqrt(5))/2 = {razon_aurea:.6f}")
print(f"  Error en n=20: |{razones[-1]:.8f} - {razon_aurea:.8f}| = "
      f"{abs(razones[-1]-razon_aurea):.2e}")

# ─────────────────────────────────────────────────────────────
# SECCION 4: Visualizacion
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle("Modulo 6 -- Sucesiones y Convergencia",
             fontsize=14, fontweight='bold')

nv = np.arange(1, 51)
colores = ['#1565C0', '#C62828', '#2E7D32', '#6A1B9A', '#E65100', '#00838F']

# Sucesiones convergentes
ax = axes[0, 0]
sucesiones_plot = [
    (1/nv,             "1/n → 0",         colores[0]),
    (nv/(nv+1),        "n/(n+1) → 1",     colores[1]),
    ((0.5)**nv,        "(1/2)^n → 0",     colores[2]),
]
for yv, label, color in sucesiones_plot:
    ax.plot(nv, yv, 'o-', color=color, lw=1.5, ms=4, label=label)
ax.axhline(0, color='gray', lw=0.8, ls='--')
ax.axhline(1, color='gray', lw=0.8, ls='--')
ax.set_title("Sucesiones convergentes", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("n"); ax.set_ylabel("a_n")

# Sucesion oscilante y no convergente
ax = axes[0, 1]
an_alt = (-1)**nv / nv
an_osc = (-1)**nv
ax.plot(nv[:30], an_alt[:30], 'o-', color=colores[0], lw=1.5, ms=4,
        label="(-1)^n/n → 0  (converge)")
ax.plot(nv[:30], an_osc[:30], 's-', color=colores[1], lw=1.5, ms=4,
        label="(-1)^n  (diverge, oscila)")
ax.axhline(0, color='gray', lw=0.8, ls='--')
ax.set_title("Sucesion alternante vs oscilante", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("n"); ax.set_ylabel("a_n")

# Convergencia a e
ax = axes[0, 2]
an_e = (1 + 1/nv)**nv
ax.plot(nv, an_e, 'o-', color=colores[2], lw=1.5, ms=3, label="(1+1/n)^n")
ax.axhline(np.e, color='red', lw=2, ls='--', label=f"e = {np.e:.5f}")
ax.set_title("(1+1/n)^n converge a e", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("n"); ax.set_ylabel("a_n")
ax.set_ylim(2, 2.9)

# Fibonacci y razon aurea
ax = axes[1, 0]
nf = np.arange(1, len(razones)+1)
ax.plot(nf, razones, 'o-', color=colores[3], lw=1.5, ms=5,
        label="F_{n+1}/Fn")
ax.axhline(razon_aurea, color='red', lw=2, ls='--',
           label=f"phi = {razon_aurea:.5f}")
ax.set_title("Sucesion de Fibonacci\nConverge a la razon aurea phi", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("n"); ax.set_ylabel("F_{n+1}/F_n")

# Convergencia monotona y acotada
ax = axes[1, 1]
for (formula, nombre), color in zip(casos_tipo, colores):
    terminos = terminos_guardados[nombre]
    ax.plot(np.arange(1, len(terminos)+1), terminos, 'o-',
            color=color, lw=1.5, ms=4, label=nombre)
ax.axhline(0, color='gray', lw=0.8, ls='--', label="Limite = 0")
ax.axhline(1, color='gray', lw=0.8, ls=':',  label="Limite = 1")
ax.set_title("Sucesiones monotona y acotada\n(todas convergen)", fontsize=10)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("n"); ax.set_ylabel("a_n")

# Velocidad de convergencia comparada
ax = axes[1, 2]
nv2 = np.arange(1, 31)
err_arith = 1/nv2                     # convergencia aritmetica O(1/n)
err_geom  = (0.5)**nv2                # convergencia geometrica O((1/2)^n)
err_exp   = nv2**2 * np.exp(-nv2)    # superconvergencia
ax.semilogy(nv2, err_arith, 'o-', color=colores[0], lw=2, ms=4,
            label="1/n  (aritmetica)")
ax.semilogy(nv2, err_geom,  's-', color=colores[1], lw=2, ms=4,
            label="(1/2)^n  (geometrica)")
ax.semilogy(nv2, err_exp,   '^-', color=colores[2], lw=2, ms=4,
            label="n^2/e^n  (superlineal)")
ax.set_title("Velocidad de convergencia\n(escala logaritmica)", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("n"); ax.set_ylabel("|a_n - L|  (log)")

plt.subplots_adjust(left=0.07, right=0.97, top=0.92, bottom=0.08,
                    hspace=0.45, wspace=0.32)
plt.savefig("sucesiones_convergencia.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n[OK]  Grafica guardada: sucesiones_convergencia.png")

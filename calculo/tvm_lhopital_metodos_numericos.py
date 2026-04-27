"""
Módulo 3 - Teorema del Valor Medio, Regla de L'Hôpital
        y Métodos Numéricos de Derivadas
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

TEOREMA DEL VALOR MEDIO (TVM) PARA DERIVADAS
──────────────────────────────────────────────
Si f es CONTINUA en [a, b] y DERIVABLE en (a, b), entonces
existe al menos un punto c ∈ (a, b) tal que:

    f'(c) = [f(b) − f(a)] / (b − a)

¿Qué significa esto?
La derivada en algún punto interior c es IGUAL a la pendiente
de la recta secante que une los puntos (a, f(a)) y (b, f(b)).

Interpretación física: si un automóvil recorre 120 km en 1.5 horas,
en algún momento su velocidad EXACTA fue de 80 km/h (el promedio).

Caso especial — Teorema de Rolle:
Si además f(a) = f(b), entonces existe c ∈ (a,b) donde f'(c) = 0.
(La función debe tener al menos un máximo o mínimo en el interior.)

REGLA DE L'HÔPITAL
────────────────────
Se aplica cuando un límite produce una forma INDETERMINADA:
    0/0  ,  ∞/∞  ,  0·∞  ,  ∞−∞  ,  0⁰  ,  1^∞  ,  ∞⁰

La regla dice: si lim f(x)/g(x) es 0/0 o ∞/∞, entonces:

    lim f(x)/g(x)  =  lim f'(x)/g'(x)

Es decir: se derivan numerador y denominador POR SEPARADO
(no es la regla del cociente) y se vuelve a tomar el límite.
Se puede aplicar varias veces si el resultado sigue siendo indeterminado.

MÉTODOS NUMÉRICOS DE DERIVADAS
────────────────────────────────
Cuando no podemos derivar analíticamente (fórmula desconocida,
datos discretos, función muy compleja), usamos aproximaciones numéricas:

  Diferencia hacia adelante (orden 1):
    f'(x) ≈ [f(x+h) − f(x)] / h

  Diferencia hacia atrás (orden 1):
    f'(x) ≈ [f(x) − f(x−h)] / h

  Diferencia central (orden 2, más precisa):
    f'(x) ≈ [f(x+h) − f(x−h)] / (2h)

  Segunda derivada (diferencia central):
    f''(x) ≈ [f(x+h) − 2f(x) + f(x−h)] / h²

A medida que h → 0, la aproximación mejora, pero si h es
demasiado pequeño aparecen errores de redondeo numérico.
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = symbols('x')

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Teorema del Valor Medio
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  TEOREMA DEL VALOR MEDIO PARA DERIVADAS")
print("=" * 60)
print("""
  Enunciado: Si f es continua en [a,b] y derivable en (a,b),
  ∃ c ∈ (a,b) tal que:
      f'(c) = [f(b) − f(a)] / (b − a)
""")

def teorema_valor_medio(f_expr, a, b, nombre):
    """
    Encuentra el punto c del TVM: donde la tangente
    es paralela a la secante entre (a, f(a)) y (b, f(b)).
    """
    fp = diff(f_expr, x)
    fa = f_expr.subs(x, a)
    fb = f_expr.subs(x, b)
    pendiente_secante = (fb - fa) / (b - a)

    # Resolver f'(c) = pendiente de la secante
    c_sol = solve(fp - pendiente_secante, x)
    c_validos = [c for c in c_sol if c.is_real and a < c < b]

    print(f"  f(x) = {nombre}  en  [{a}, {b}]")
    print(f"  f({a}) = {fa},  f({b}) = {fb}")
    print(f"  Pendiente secante = [f({b})−f({a})] / ({b}−{a}) = {pendiente_secante}")
    print(f"  f'(x) = {fp}")
    print(f"  Resolver f'(c) = {pendiente_secante}  →  c = {c_validos}")
    for c in c_validos:
        print(f"    c = {c} ≈ {round(float(c),4)}: "
              f"f({round(float(c),4)}) = {round(float(f_expr.subs(x,c)),4)}")
    print()
    return c_validos, float(pendiente_secante)

casos_tvm = [
    (x**3 - x,  0, 2,    "x³ − x"),
    (sin(x),    0, pi,   "sin(x)"),
    (exp(x),    0, 2,    "eˣ"),
]
resultados_tvm = []
for f_expr, a, b, nombre in casos_tvm:
    c_vals, m = teorema_valor_medio(f_expr, a, b, nombre)
    resultados_tvm.append((f_expr, a, b, nombre, c_vals, m))

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Regla de L'Hôpital
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  REGLA DE L'HÔPITAL")
print("=" * 60)
print("""
  Pasos para aplicar L'Hôpital:
    1) Verificar que el límite produce una forma indeterminada
    2) Derivar numerador y denominador POR SEPARADO
    3) Evaluar el nuevo límite
    4) Repetir si sigue siendo indeterminado
""")

casos_lhopital = [
    # (función, punto, forma, nombre)
    (sin(x)/x,                     0,  "0/0",  "sin(x)/x"),
    ((exp(x)-1)/x,                  0,  "0/0",  "(eˣ−1)/x"),
    ((x**2-4)/(x-2),                2,  "0/0",  "(x²−4)/(x−2)"),
    ((1-cos(x))/x**2,               0,  "0/0",  "(1−cos x)/x²"),
    (log(x)/(x-1),                  1,  "0/0",  "ln(x)/(x−1)"),
    ((x**2)/(exp(x)),              oo,  "∞/∞",  "x²/eˣ"),
    (x*log(x),                      0,  "0·∞",  "x·ln(x)  (x→0⁺)"),
]

for f_expr, punto, forma, nombre in casos_lhopital:
    lim_directo = limit(f_expr, x, punto)
    print(f"  Forma {forma}:  lim  {nombre}")

    # Mostrar el proceso si es cociente
    if '/' in str(f_expr) and punto != oo:
        num, den = fraction(f_expr)
        v_num = limit(num, x, punto)
        v_den = limit(den, x, punto)
        if (v_num == 0 and v_den == 0) or \
           (v_num in [oo,-oo] and v_den in [oo,-oo]):
            dnum = diff(num, x)
            dden = diff(den, x)
            lim2 = limit(dnum/dden, x, punto)
            print(f"    Numerador→{v_num}, Denominador→{v_den}  ✓ aplica L'Hôpital")
            print(f"    Derivadas: {dnum} / {dden}")
            print(f"    Resultado: {lim2}")
        else:
            print(f"    Resultado directo: {lim_directo}")
    else:
        print(f"    Resultado: {lim_directo}")
    print()

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Métodos Numéricos de Derivadas
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  MÉTODOS NUMÉRICOS DE DERIVADAS")
print("=" * 60)
print("""
  Comparación de métodos para f(x) = sin(x) en x = π/4
  Valor exacto: f'(π/4) = cos(π/4) = √2/2 ≈ 0.70710678
""")

f_num  = np.sin
fp_exacta = np.cos
x0 = np.pi / 4
exacto = fp_exacta(x0)

print(f"  {'h':<12} {'Adelante':>12} {'Atrás':>12} "
      f"{'Central':>12} {'Error Central':>14}")
print(f"  {'─'*65}")

for hv in [0.1, 0.01, 0.001, 0.0001, 1e-7, 1e-14]:
    adelante = (f_num(x0+hv) - f_num(x0)) / hv
    atras    = (f_num(x0) - f_num(x0-hv)) / hv
    central  = (f_num(x0+hv) - f_num(x0-hv)) / (2*hv)
    err_c    = abs(central - exacto)
    print(f"  {hv:<12.0e} {adelante:>12.8f} {atras:>12.8f} "
          f"{central:>12.8f} {err_c:>14.2e}")

print(f"\n  Valor exacto:  {exacto:.8f}")
print("""
  Observaciones:
    • La diferencia CENTRAL es más precisa para el mismo h
    • El error decrece con h hasta cierto punto
    • Para h muy pequeño (< 1e-8), el error SUBE por redondeo numérico
""")

# Segunda derivada numérica
print("  Segunda derivada numérica  — f(x) = sin(x) en x = π/4")
print(f"  Valor exacto de f''(π/4) = -sin(π/4) ≈ {-np.sin(x0):.8f}")
for hv in [0.1, 0.01, 0.001]:
    fpp_num = (f_num(x0+hv) - 2*f_num(x0) + f_num(x0-hv)) / hv**2
    err = abs(fpp_num - (-np.sin(x0)))
    print(f"    h={hv}: f''≈{fpp_num:.8f}  error={err:.2e}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 4: Visualización
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Módulo 3 — TVM, Regla de L'Hôpital y Métodos Numéricos",
             fontsize=14, fontweight='bold')

# ── TVM en x³-x ──
ax = axes[0, 0]
xv = np.linspace(-0.5, 2.5, 300)
yv = xv**3 - xv
a_t, b_t = 0, 2
fa_t, fb_t = 0**3-0, 2**3-2
m_sec = (fb_t - fa_t) / (b_t - a_t)
c_tvm = float(resultados_tvm[0][4][0])
ax.plot(xv, yv, color='#1565C0', lw=2.5, label="f(x) = x³−x")
ax.plot([a_t, b_t], [fa_t, fb_t], color='orange', lw=2, ls='--', label="Secante")
yc = c_tvm**3 - c_tvm
xtan = np.linspace(c_tvm-1, c_tvm+1, 100)
ax.plot(xtan, m_sec*(xtan-c_tvm)+yc, color='green', lw=2, ls='-.',
        label=f"Tangente en c≈{round(c_tvm,3)}")
ax.scatter([a_t, b_t], [fa_t, fb_t], color='black', zorder=5, s=80)
ax.scatter([c_tvm], [yc], color='red', zorder=5, s=100,
           label=f"c ≈ {round(c_tvm,3)}")
ax.set_title("Teorema del Valor Medio\nf(x)=x³−x en [0,2]", fontsize=9)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# ── TVM en sin(x) ──
ax = axes[0, 1]
xv2 = np.linspace(-0.3, np.pi+0.3, 300)
a2, b2 = 0, float(pi)
fa2, fb2 = 0, 0
m_sec2 = 0
c_tvm2 = float(resultados_tvm[1][4][0])
ax.plot(xv2, np.sin(xv2), color='#C62828', lw=2.5, label="f(x) = sin(x)")
ax.plot([a2, b2], [fa2, fb2], color='orange', lw=2, ls='--',
        label="Secante (pendiente=0)")
yc2 = np.sin(c_tvm2)
xtan2 = np.linspace(c_tvm2-0.8, c_tvm2+0.8, 100)
ax.plot(xtan2, 0*(xtan2-c_tvm2)+yc2, color='green', lw=2, ls='-.',
        label=f"Tangente en c≈{round(c_tvm2,3)}")
ax.scatter([c_tvm2], [yc2], color='red', zorder=5, s=100,
           label=f"c = π/2 ≈ {round(c_tvm2,3)}")
ax.set_title("Teorema del Valor Medio\nf(x)=sin(x) en [0,π]", fontsize=9)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# ── L'Hôpital: sin(x)/x ──
ax = axes[0, 2]
xv3 = np.linspace(-10, 10, 500)
xv3_s = np.where(xv3==0, 1e-10, xv3)
ax.plot(xv3, np.sin(xv3_s)/xv3_s, color='#2E7D32', lw=2.5,
        label="sin(x)/x  →  forma 0/0 en x=0")
ax.scatter([0], [1], color='red', zorder=5, s=100,
           label="L'Hôpital: lim = 1")
ax.axhline(1, color='red', ls='--', lw=1, alpha=0.5)
ax.set_title("L'Hôpital: sin(x)/x\nlim x→0 = cos(0)/1 = 1", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_ylim(-0.5, 1.5)

# ── L'Hôpital: x²/eˣ → 0 ──
ax = axes[1, 0]
xv4 = np.linspace(0, 20, 300)
ax.plot(xv4, xv4**2/np.exp(xv4), color='#6A1B9A', lw=2.5,
        label="x²/eˣ  →  ∞/∞")
ax.axhline(0, color='red', ls='--', lw=1.5, label="lim x→∞ = 0")
ax.set_title("L'Hôpital: x²/eˣ → 0\n(eˣ crece más rápido que x²)", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# ── Error de aproximación numérica ──
ax = axes[1, 1]
hs = np.logspace(-14, 0, 100)
err_adelante = np.abs((np.sin(x0+hs) - np.sin(x0))/hs - exacto)
err_central  = np.abs((np.sin(x0+hs) - np.sin(x0-hs))/(2*hs) - exacto)
ax.loglog(hs, err_adelante, color='#E53935', lw=2, label="Diferencia adelante")
ax.loglog(hs, err_central,  color='#1565C0', lw=2, label="Diferencia central")
ax.set_title("Error vs tamaño de h\nf'(π/4) de sin(x)", fontsize=9)
ax.set_xlabel("h"); ax.set_ylabel("Error absoluto")
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.invert_xaxis()

# ── Comparación métodos numéricos ──
ax = axes[1, 2]
hv_plot = 0.3
xv5 = np.linspace(0, 2*np.pi, 200)
fp_exacta_v = np.cos(xv5)
fp_central  = (np.sin(xv5+hv_plot) - np.sin(xv5-hv_plot)) / (2*hv_plot)
fp_adelante = (np.sin(xv5+hv_plot) - np.sin(xv5)) / hv_plot
ax.plot(xv5, fp_exacta_v, color='black', lw=2.5, label="f'(x) exacta = cos(x)")
ax.plot(xv5, fp_central,  color='#1565C0', lw=2, ls='--', label=f"Central  (h={hv_plot})")
ax.plot(xv5, fp_adelante, color='#E53935', lw=2, ls=':',  label=f"Adelante (h={hv_plot})")
ax.set_title(f"Métodos numéricos vs exacto\nsin(x), h={hv_plot}", fontsize=9)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("f'(x)")

plt.tight_layout()
plt.savefig("tvm_lhopital_metodos_numericos.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: tvm_lhopital_metodos_numericos.png")

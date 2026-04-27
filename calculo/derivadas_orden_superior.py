"""
Módulo 2 - Derivación de Orden Superior
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

¿QUÉ SON LAS DERIVADAS DE ORDEN SUPERIOR?
───────────────────────────────────────────
Si f'(x) es la derivada de f, podemos derivar f'(x) nuevamente
para obtener la SEGUNDA DERIVADA, denotada f''(x) o d²y/dx².

En general:
  f'(x)   = primera derivada   →  tasa de cambio de f
  f''(x)  = segunda derivada   →  tasa de cambio de f'
  f'''(x) = tercera derivada   →  tasa de cambio de f''
  f⁽ⁿ⁾(x) = derivada de orden n

INTERPRETACIÓN FÍSICA:
  Si f(t) = posición de un objeto en el tiempo t, entonces:
  • f'(t)  = velocidad  (qué tan rápido se mueve)
  • f''(t) = aceleración (qué tan rápido cambia la velocidad)

INTERPRETACIÓN GEOMÉTRICA (segunda derivada):
  f''(x) describe la CONCAVIDAD de la curva:
  • f''(x) > 0  →  curva cóncava hacia ARRIBA ∪  (como tazón)
  • f''(x) < 0  →  curva cóncava hacia ABAJO ∩   (como colina)
  • f''(x) = 0  →  posible PUNTO DE INFLEXIÓN
    (lugar donde la curva cambia de concavidad)

NOTACIONES:
  f''(x)  =  y''  =  d²y/dx²  =  D²f  =  f⁽²⁾(x)
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = symbols('x')

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Derivadas de orden n
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  DERIVADAS DE ORDEN SUPERIOR")
print("=" * 60)
print("""
  Para calcular f''(x): derivar f'(x) una vez más.
  Para f'''(x): derivar f''(x), y así sucesivamente.
""")

funciones = [
    (x**5,          "x⁵",    5),
    (sin(x),        "sin(x)", 5),
    (exp(x),        "eˣ",     4),
    (log(x),        "ln(x)",  4),
    (x**2 * exp(x), "x²·eˣ",  3),
]

for f_expr, nombre, max_orden in funciones:
    print(f"  f(x) = {nombre}")
    fp = f_expr
    for n in range(1, max_orden + 1):
        fp = diff(fp, x)
        notacion = ["f'", "f''", "f'''", "f⁽⁴⁾", "f⁽⁵⁾"][n-1]
        print(f"    {notacion}(x) = {simplify(fp)}")
    print()

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Concavidad y puntos de inflexión
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  CONCAVIDAD Y PUNTOS DE INFLEXIÓN")
print("=" * 60)
print("""
  La segunda derivada f''(x) determina la concavidad:

  • Si f''(x) > 0 en (a,b)  →  f es CÓNCAVA HACIA ARRIBA en (a,b)
    La curva "sostiene agua". f' es creciente.

  • Si f''(x) < 0 en (a,b)  →  f es CÓNCAVA HACIA ABAJO en (a,b)
    La curva "derrama agua". f' es decreciente.

  PUNTO DE INFLEXIÓN: punto donde la concavidad cambia.
    Condición necesaria: f''(c) = 0
    Pero f''(c)=0 NO garantiza inflexión; hay que verificar
    que el signo de f'' realmente cambie a ambos lados de c.
""")

def analizar_concavidad(f_expr, nombre, intervalo=(-5, 5)):
    fp  = diff(f_expr, x)
    fpp = diff(fp, x)
    puntos_inf = solve(fpp, x)
    puntos_reales = [p for p in puntos_inf
                     if p.is_real and intervalo[0] < p < intervalo[1]]

    print(f"  f(x)   = {nombre}")
    print(f"  f'(x)  = {simplify(fp)}")
    print(f"  f''(x) = {simplify(fpp)}")
    print(f"  Resolver f''(x) = 0  →  x = {puntos_reales}")

    for p in puntos_reales:
        val_izq = fpp.subs(x, p - Rational(1,10))
        val_der = fpp.subs(x, p + Rational(1,10))
        cambio  = val_izq * val_der < 0
        tipo    = "✅ Punto de Inflexión (cambia concavidad)" if cambio \
                  else "❌ No es inflexión (no cambia concavidad)"
        print(f"    x = {p}  →  f''(x⁻)={round(float(val_izq),3)},  "
              f"f''(x⁺)={round(float(val_der),3)}  →  {tipo}")
    print()
    return fp, fpp

analizar_concavidad(x**3 - 3*x**2 + 2, "x³ − 3x² + 2")
analizar_concavidad(x**4 - 6*x**2,     "x⁴ − 6x²")
analizar_concavidad(sin(x),            "sin(x)")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Visualización
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Módulo 2 — Derivadas de Orden Superior y Concavidad",
             fontsize=14, fontweight='bold')

c_f   = '#1565C0'
c_fp  = '#E53935'
c_fpp = '#2E7D32'

xv = np.linspace(-1, 4, 400)
yf   = xv**3 - 3*xv**2 + 2
yfp  = 3*xv**2 - 6*xv
yfpp = 6*xv - 6

# f(x)
ax = axes[0, 0]
ax.plot(xv, yf, color=c_f, lw=2.5, label="f(x) = x³−3x²+2")
ax.axhline(0, color='black', lw=0.8)
ax.scatter([1], [0], color='red', zorder=5, s=70, label="Inflexión x=1")
ax.fill_between(xv[xv < 1], yf[xv < 1], alpha=0.10, color='orange', label="cóncava ↓")
ax.fill_between(xv[xv > 1], yf[xv > 1], alpha=0.10, color='blue',   label="cóncava ↑")
ax.set_title("f(x) = x³−3x²+2\n(función original)", fontsize=9)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_ylim(-3, 5)

# f'(x)
ax = axes[0, 1]
ax.plot(xv, yfp, color=c_fp, lw=2.5, label="f'(x) = 3x²−6x")
ax.axhline(0, color='black', lw=0.8)
ax.scatter([0, 2], [0, 0], color='purple', zorder=5, s=70,
           label="Críticos: x=0, x=2")
ax.set_title("f'(x) = 3x²−6x\n(donde f'=0: máx/mín locales)", fontsize=9)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# f''(x)
ax = axes[0, 2]
ax.plot(xv, yfpp, color=c_fpp, lw=2.5, label="f''(x) = 6x−6")
ax.axhline(0, color='black', lw=0.8)
ax.scatter([1], [0], color='red', zorder=5, s=70, label="f''=0  →  x=1")
ax.fill_between(xv, yfpp, 0, where=(yfpp > 0), alpha=0.12,
                color='blue',   label="cóncava ↑")
ax.fill_between(xv, yfpp, 0, where=(yfpp < 0), alpha=0.12,
                color='orange', label="cóncava ↓")
ax.set_title("f''(x) = 6x−6\n(signo determina concavidad)", fontsize=9)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# sin(x) con concavidades
xv2   = np.linspace(-2*np.pi, 2*np.pi, 500)
yf2   = np.sin(xv2)
yfp2  = np.cos(xv2)
yfpp2 = -np.sin(xv2)

ax = axes[1, 0]
ax.plot(xv2, yf2, color=c_f, lw=2.5, label="f(x) = sin(x)")
ax.fill_between(xv2, yf2, 0, where=(yfpp2 < 0), alpha=0.12,
                color='orange', label="cóncava ↓")
ax.fill_between(xv2, yf2, 0, where=(yfpp2 > 0), alpha=0.12,
                color='blue',   label="cóncava ↑")
ax.axhline(0, color='black', lw=0.8)
ax.set_title("sin(x) — regiones de concavidad", fontsize=10)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# f', f'' de sin(x)
ax = axes[1, 1]
ax.plot(xv2, yfp2,  color=c_fp,  lw=2,   label="f'(x)  = cos(x)")
ax.plot(xv2, yfpp2, color=c_fpp, lw=2, ls='--', label="f''(x) = −sin(x)")
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Derivadas 1ª y 2ª de sin(x)", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# Ciclo de derivadas de sin(x)
ax = axes[1, 2]
xv3 = np.linspace(0, 2*np.pi, 300)
ciclo = [
    (np.sin(xv3),  "f⁽⁰⁾ = sin(x)",  c_f),
    (np.cos(xv3),  "f'   = cos(x)",   c_fp),
    (-np.sin(xv3), "f''  = −sin(x)",  c_fpp),
    (-np.cos(xv3), "f''' = −cos(x)",  '#6A1B9A'),
    (np.sin(xv3),  "f⁽⁴⁾ = sin(x) ← ciclo completo", '#E65100'),
]
for y, label, color in ciclo:
    ax.plot(xv3, y, lw=2, label=label, color=color)
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Ciclo de derivadas de sin(x)\n(se repite cada 4 derivadas)", fontsize=9)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

plt.tight_layout()
plt.savefig("derivadas_orden_superior.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: derivadas_orden_superior.png")

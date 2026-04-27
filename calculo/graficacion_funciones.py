"""
Módulo 3 - Graficación de Funciones con Cálculo Diferencial
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

¿CÓMO AYUDA EL CÁLCULO A GRAFICAR?
─────────────────────────────────────
Antes del cálculo, graficar una función requería evaluar muchos puntos
y "adivinar" su comportamiento. Con la derivada, podemos determinar
de manera EXACTA y SISTEMÁTICA la forma de la gráfica:

  f'(x) → nos dice dónde sube, dónde baja y dónde están los extremos
  f''(x) → nos dice la concavidad y los puntos de inflexión

ANÁLISIS COMPLETO DE UNA FUNCIÓN — pasos:
  1. Dominio: ¿para qué valores de x está definida f?
  2. Intersecciones: f(0) para el eje y; f(x)=0 para el eje x
  3. Asíntotas: verticales (denominador = 0), horizontales (lím x→±∞)
  4. Monotonía (f'):
       f'(x) > 0 → f es CRECIENTE en ese intervalo
       f'(x) < 0 → f es DECRECIENTE en ese intervalo
       f'(x) = 0 → punto CRÍTICO (candidato a máximo o mínimo)
  5. Extremos locales — Criterio de la segunda derivada:
       f'(c)=0 y f''(c) > 0 → MÍNIMO local en x=c
       f'(c)=0 y f''(c) < 0 → MÁXIMO local en x=c
       f'(c)=0 y f''(c) = 0 → Criterio no concluye (revisar manualmente)
  6. Concavidad (f''): intervalo donde f''>0 (↑) o f''<0 (↓)
  7. Inflexión: donde f''=0 y cambia de signo
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = symbols('x')

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Análisis completo de una función
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  ANÁLISIS COMPLETO DE UNA FUNCIÓN CON CÁLCULO")
print("=" * 60)

def analisis_completo(f_expr, nombre, intervalo=(-5, 5)):
    """
    Realiza el análisis completo de una función usando f' y f'':
    dominio implícito, monotonía, extremos y concavidad.
    """
    fp  = diff(f_expr, x)
    fpp = diff(fp, x)

    print(f"\n{'─'*55}")
    print(f"  f(x) = {nombre}")
    print(f"{'─'*55}")
    print(f"  f'(x)  = {simplify(fp)}")
    print(f"  f''(x) = {simplify(fpp)}")

    # Puntos críticos: f'(x) = 0
    criticos = solve(fp, x)
    criticos_reales = [c for c in criticos
                       if c.is_real and intervalo[0] <= c <= intervalo[1]]
    print(f"\n  Puntos críticos (f'=0): x = {criticos_reales}")

    for c in criticos_reales:
        val_f   = f_expr.subs(x, c)
        val_fpp = fpp.subs(x, c)
        if val_fpp > 0:
            tipo = f"MÍNIMO local  (f''({c})={val_fpp} > 0)"
        elif val_fpp < 0:
            tipo = f"MÁXIMO local  (f''({c})={val_fpp} < 0)"
        else:
            tipo = f"Criterio 2da no concluye  (f''({c})=0)"
        print(f"    x={c}: f({c})={val_f}  →  {tipo}")

    # Puntos de inflexión: f''(x) = 0
    inflexion = solve(fpp, x)
    inf_reales = [p for p in inflexion
                  if p.is_real and intervalo[0] <= p <= intervalo[1]]
    print(f"\n  Puntos de inflexión (f''=0): x = {inf_reales}")
    for p in inf_reales:
        val_izq = fpp.subs(x, p - Rational(1,10))
        val_der = fpp.subs(x, p + Rational(1,10))
        if val_izq * val_der < 0:
            print(f"    x={p}: f({p})={f_expr.subs(x,p)}  →  ✅ Inflexión confirmada")
        else:
            print(f"    x={p}  →  ❌ No es inflexión (no cambia concavidad)")

    # Monotonía por intervalos
    print(f"\n  Monotonía:")
    puntos = sorted([float(intervalo[0])] +
                    [float(c) for c in criticos_reales] +
                    [float(intervalo[1])])
    for i in range(len(puntos) - 1):
        mid = (puntos[i] + puntos[i+1]) / 2
        signo = fp.subs(x, mid)
        direccion = "creciente ↑" if signo > 0 else "decreciente ↓"
        print(f"    ({round(puntos[i],2)}, {round(puntos[i+1],2)}): "
              f"f'={round(float(signo),3)}  →  {direccion}")
    print()

funciones_analisis = [
    (x**3 - 3*x**2 - 9*x + 2,  "x³ − 3x² − 9x + 2"),
    (x**4 - 8*x**2,             "x⁴ − 8x²"),
    (x*exp(-x),                 "x·e⁻ˣ"),
]

for f_expr, nombre in funciones_analisis:
    analisis_completo(f_expr, nombre)

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Visualización — f, f', f'' en paralelo
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
fig.suptitle("Módulo 3 — Graficación de Funciones con Cálculo Diferencial",
             fontsize=14, fontweight='bold')

datos = [
    (lambda xv: xv**3 - 3*xv**2 - 9*xv + 2,
     lambda xv: 3*xv**2 - 6*xv - 9,
     lambda xv: 6*xv - 6,
     "x³−3x²−9x+2",
     np.linspace(-3, 6, 400),
     [(-1, 7), (3, -25)],   # (x, y) de críticos: máx, mín
     [1]),                   # inflexiones
    (lambda xv: xv**4 - 8*xv**2,
     lambda xv: 4*xv**3 - 16*xv,
     lambda xv: 12*xv**2 - 16,
     "x⁴−8x²",
     np.linspace(-3.5, 3.5, 400),
     [(0, 0), (-2, -16), (2, -16)],
     [-2/np.sqrt(3), 2/np.sqrt(3)]),
    (lambda xv: xv * np.exp(-xv),
     lambda xv: np.exp(-xv) - xv*np.exp(-xv),
     lambda xv: -2*np.exp(-xv) + xv*np.exp(-xv),
     "x·e⁻ˣ",
     np.linspace(-1, 6, 400),
     [(1, np.e**-1)],
     [2]),
]

colores = ['#1565C0', '#E53935', '#2E7D32']
etiquetas = ["f(x)", "f'(x)", "f''(x)"]

for col, (f_num, fp_num, fpp_num, nombre, xv,
          criticos, inflexiones) in enumerate(datos):

    ys = [f_num(xv), fp_num(xv), fpp_num(xv)]

    for fila, (y, etiq, color) in enumerate(zip(ys, etiquetas, colores)):
        ax = axes[fila, col]
        ax.plot(xv, y, color=color, lw=2.5, label=f"{etiq} = {nombre}")
        ax.axhline(0, color='black', lw=0.8)
        ax.axvline(0, color='black', lw=0.8, alpha=0.3)

        # Marcar críticos solo en f(x)
        if fila == 0:
            for cx, cy in criticos:
                ax.scatter([cx], [cy], color='red', zorder=5, s=80)
            for ix in inflexiones:
                ax.scatter([ix], [f_num(np.array([ix]))[0]],
                           color='purple', zorder=5, s=80, marker='D')

        # Marcar ceros de f' en la gráfica de f'
        if fila == 1:
            for cx, _ in criticos:
                ax.scatter([cx], [0], color='red', zorder=5, s=80,
                           label=f"f'={0} en x={cx}")

        ax.set_title(f"{etiq}  —  {nombre}", fontsize=9)
        ax.legend(fontsize=7)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel("x")
        ax.set_ylabel(etiq)

        # Límites razonables
        y_finite = y[np.isfinite(y)]
        if len(y_finite) > 0:
            rango = max(abs(y_finite.max()), abs(y_finite.min()))
            ax.set_ylim(-min(rango*1.3, 40), min(rango*1.3, 40))

plt.tight_layout()
plt.savefig("graficacion_funciones.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: graficacion_funciones.png")

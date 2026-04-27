"""
Módulo 5 - Longitudes de Arco y Áreas de Superficies
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

¿QUÉ ES LA LONGITUD DE ARCO?
──────────────────────────────
La longitud de arco es la distancia real que recorrerías si caminaras
sobre la curva f(x) entre dos puntos x=a y x=b.

No es simplemente b−a (eso sería la distancia horizontal),
sino la longitud real de la curva, que siempre es mayor o igual
a la distancia en línea recta.

DERIVACIÓN DE LA FÓRMULA:
  Imagina dividir la curva en pequeños segmentos Δs.
  Cada segmento se aproxima con la hipotenusa de un triángulo:
    Δs ≈ √(Δx² + Δy²) = √(1 + (Δy/Δx)²) · Δx

  Tomando el límite cuando Δx → 0:
    ds = √(1 + [f'(x)]²) dx

  La longitud total es:
    L = ∫[a,b] √(1 + [f'(x)]²) dx

ÁREA DE UNA SUPERFICIE DE REVOLUCIÓN:
  Cuando giramos una curva f(x) alrededor del eje x,
  generamos una superficie tridimensional.

  Imagina cada pequeño arco ds generando un anillo circular
  de radio f(x) y "altura" ds. El área de ese anillo es 2π·f(x)·ds.

  El área total de la superficie es:
    S = ∫[a,b] 2π·f(x)·√(1 + [f'(x)]²) dx

  Si giramos alrededor del eje y:
    S = ∫[a,b] 2π·x·√(1 + [f'(x)]²) dx

CASOS CONOCIDOS (verificación):
  • Circunferencia de un círculo de radio r:
    f(x) = √(r²−x²),  L = πr  (semicírculo)  → L completo = 2πr ✓
  • Área lateral de un cilindro de radio r y altura h:
    S = 2πrh ✓
  • Área de una esfera de radio r:
    S = 4πr² ✓
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import *

x = symbols('x', real=True)

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Longitud de arco
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  LONGITUD DE ARCO")
print("=" * 60)
print("""
  Fórmula: L = ∫[a,b] √(1 + [f'(x)]²) dx

  Procedimiento:
    1) Calcular f'(x)
    2) Calcular [f'(x)]²
    3) Construir el integrando √(1 + [f'(x)]²)
    4) Integrar en [a, b]
""")

def longitud_arco(f_expr, a, b, nombre):
    fp   = diff(f_expr, x)
    integrado = sqrt(1 + fp**2)
    L = integrate(integrado, (x, a, b))
    L_simplificado = simplify(L)

    print(f"  f(x) = {nombre}  en  [{a}, {b}]")
    print(f"  f'(x) = {fp}")
    print(f"  Integrando: √(1 + ({fp})²) = {simplify(integrado)}")
    print(f"  L = {L_simplificado}")
    try:
        print(f"  L ≈ {float(L_simplificado):.6f}")
    except Exception:
        print(f"  L ≈ {float(L_simplificado.evalf()):.6f}")
    print()
    return L_simplificado

casos_arco = [
    (x,             0, 1,    "x  (línea recta, esperamos √2 ≈ 1.4142)"),
    (x**2,          0, 1,    "x²"),
    (x**Rational(3,2), 0, 4, "x^(3/2)"),
    (log(x),        1, exp(1), "ln(x)  en [1, e]"),
    (cosh(x),      -1, 1,    "cosh(x)"),
]

for f_expr, a, b, nombre in casos_arco:
    longitud_arco(f_expr, a, b, nombre)

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Área de superficie de revolución
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  ÁREA DE SUPERFICIE DE REVOLUCIÓN")
print("=" * 60)
print("""
  Girando f(x) alrededor del eje x:
    S = ∫[a,b] 2π·f(x)·√(1 + [f'(x)]²) dx

  Girando alrededor del eje y:
    S = ∫[a,b] 2π·x·√(1 + [f'(x)]²) dx
""")

def area_superficie(f_expr, a, b, nombre, eje='x'):
    fp   = diff(f_expr, x)
    ds   = sqrt(1 + fp**2)
    if eje == 'x':
        integrado = 2 * pi * f_expr * ds
    else:
        integrado = 2 * pi * x * ds
    S = integrate(integrado, (x, a, b))
    S_simplificado = simplify(S)

    print(f"  f(x) = {nombre}  en  [{a}, {b}]  (eje {eje})")
    print(f"  S = 2π ∫ {'f(x)' if eje=='x' else 'x'}·√(1+f'²) dx")
    print(f"  S = {S_simplificado}")
    try:
        print(f"  S ≈ {float(S_simplificado):.6f}")
    except Exception:
        print(f"  S ≈ {float(S_simplificado.evalf()):.6f}")
    print()
    return S_simplificado

# Verificación con esfera: f(x) = √(r²-x²), S debe dar 4πr²
r_val = 1
print("  Verificación: esfera de radio 1 → S debe ser 4π ≈ 12.5664")
f_esfera = sqrt(1 - x**2)
area_superficie(f_esfera, -1, 1, "√(1−x²)  [semicírculo → esfera radio 1]")

casos_sup = [
    (x,       0, 1, "x  (cono)"),
    (x**2,    0, 1, "x²"),
    (sqrt(x), 0, 4, "√x"),
]

for f_expr, a, b, nombre in casos_sup:
    area_superficie(f_expr, a, b, nombre)

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Visualización
# ─────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(15, 9))
fig.suptitle("Módulo 5 — Longitudes de Arco y Superficies de Revolución",
             fontsize=14, fontweight='bold')

# ── Longitud de arco de x² ──
ax1 = fig.add_subplot(2, 3, 1)
xv = np.linspace(0, 1, 300)
ax1.plot(xv, xv**2, color='#1565C0', lw=3, label="f(x) = x²")
# Aproximación con segmentos
n_seg = 8
xseg = np.linspace(0, 1, n_seg+1)
yseg = xseg**2
for i in range(n_seg):
    ax1.plot([xseg[i], xseg[i+1]], [yseg[i], yseg[i+1]],
             color='#E53935', lw=1.5, alpha=0.7)
    ax1.scatter([xseg[i]], [yseg[i]], color='#E53935', s=30, zorder=5)
L_num = float(integrate(sqrt(1 + (2*x)**2), (x, 0, 1)).evalf())
ax1.set_title(f"Longitud de arco de x²\nL ≈ {L_num:.4f}", fontsize=9)
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)
ax1.set_xlabel("x"); ax1.set_ylabel("y")

# ── Comparación longitud arco vs distancia recta ──
ax2 = fig.add_subplot(2, 3, 2)
funciones_L = [
    (lambda xv: xv,       lambda xv: np.ones_like(xv),      "x",     0, 2),
    (lambda xv: xv**2,    lambda xv: 2*xv,                  "x²",    0, 2),
    (lambda xv: np.sin(xv), lambda xv: np.cos(xv),          "sin(x)",0, np.pi),
]
colores_L = ['#1565C0', '#C62828', '#2E7D32']
for (f_n, fp_n, nombre, a_n, b_n), color in zip(funciones_L, colores_L):
    xv_n = np.linspace(a_n, b_n, 1000)
    L_aprox = np.trapezoid(np.sqrt(1 + fp_n(xv_n)**2), xv_n)
    dist_recta = np.sqrt((b_n - a_n)**2 + (f_n(b_n) - f_n(a_n))**2)
    ax2.barh(nombre, L_aprox, color=color, alpha=0.7,
             label=f"L={L_aprox:.3f}")
    ax2.barh(nombre, dist_recta, color=color, alpha=0.3, hatch='//')
ax2.set_title("Longitud arco (sólido) vs\ndistancia recta (rayado)", fontsize=9)
ax2.set_xlabel("Longitud"); ax2.grid(True, alpha=0.3, axis='x')

# ── Superficie de revolución de √x ──
ax3 = fig.add_subplot(2, 3, 3, projection='3d')
xv3 = np.linspace(0, 4, 50)
theta = np.linspace(0, 2*np.pi, 60)
X3, T = np.meshgrid(xv3, theta)
R3 = np.sqrt(X3)
Y3 = R3 * np.cos(T)
Z3 = R3 * np.sin(T)
ax3.plot_surface(X3, Y3, Z3, alpha=0.4, color='#2E7D32')
ax3.set_title("Superficie: √x\ngirada en eje x", fontsize=9)
ax3.set_xlabel("x"); ax3.set_ylabel("y"); ax3.set_zlabel("z")

# ── Segmentos ds acumulando longitud ──
ax4 = fig.add_subplot(2, 3, 4)
xv4 = np.linspace(0, 2, 300)
fp4 = 2*xv4
ds4 = np.sqrt(1 + fp4**2)
L_acum = np.cumsum(ds4 * (xv4[1] - xv4[0]))
ax4.plot(xv4, L_acum, color='#6A1B9A', lw=2.5,
         label="L(x) = ∫₀ˣ √(1+4t²) dt")
ax4.set_title("Longitud acumulada de x²\ncomo función del límite superior",
              fontsize=9)
ax4.legend(fontsize=8); ax4.grid(True, alpha=0.3)
ax4.set_xlabel("x"); ax4.set_ylabel("L(x)")

# ── Superficie de revolución del cono ──
ax5 = fig.add_subplot(2, 3, 5, projection='3d')
xv5 = np.linspace(0, 1, 30)
theta5 = np.linspace(0, 2*np.pi, 60)
X5, T5 = np.meshgrid(xv5, theta5)
Y5 = X5 * np.cos(T5)
Z5 = X5 * np.sin(T5)
ax5.plot_surface(X5, Y5, Z5, alpha=0.4, color='#E65100')
S_cono = float(integrate(2*pi*x*sqrt(2), (x, 0, 1)).evalf())
ax5.set_title(f"Cono: f(x)=x girada\nS = π√2 ≈ {S_cono:.4f}", fontsize=9)
ax5.set_xlabel("x"); ax5.set_ylabel("y"); ax5.set_zlabel("z")

# ── Esfera generada por semicírculo ──
ax6 = fig.add_subplot(2, 3, 6, projection='3d')
theta6 = np.linspace(0, np.pi, 40)
phi6   = np.linspace(0, 2*np.pi, 60)
T6, P6 = np.meshgrid(theta6, phi6)
X6 = np.sin(T6) * np.cos(P6)
Y6 = np.sin(T6) * np.sin(P6)
Z6 = np.cos(T6)
ax6.plot_surface(X6, Y6, Z6, alpha=0.3, color='#1565C0')
ax6.set_title("Esfera (radio=1)\nS = 4π ≈ 12.566", fontsize=9)
ax6.set_xlabel("x"); ax6.set_ylabel("y"); ax6.set_zlabel("z")

plt.tight_layout()
plt.savefig("longitud_arco_superficies.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: longitud_arco_superficies.png")

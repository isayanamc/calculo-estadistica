"""
Módulo 2 - Reglas de Derivación y Regla de la Cadena
FUN-05 Cálculo Diferencial e Integral | Universidad CENFOTEC

¿POR QUÉ NECESITAMOS REGLAS?
──────────────────────────────
Calcular cada derivada desde la definición (límite del cociente) es tedioso.
Las REGLAS DE DERIVACIÓN son atajos que se demuestran una vez usando esa
definición y luego se aplican directamente.

Las principales reglas son:

  1. POTENCIA:    d/dx[xⁿ] = n·xⁿ⁻¹
     Ejemplo:     d/dx[x⁵] = 5x⁴

  2. LINEALIDAD:  d/dx[c·f(x)] = c·f'(x)   (constante sale)
                  d/dx[f+g] = f' + g'        (derivada de suma)

  3. PRODUCTO:    d/dx[u·v] = u'·v + u·v'
     Regla del producto — NO es (uv)' = u'v'

  4. COCIENTE:    d/dx[u/v] = (u'·v - u·v') / v²
     Regla del cociente — NO es (u/v)' = u'/v'

  5. CADENA:      d/dx[g(h(x))] = g'(h(x)) · h'(x)
     Para funciones compuestas: derivar la "exterior" y multiplicar
     por la derivada de la "interior"

TABLA DE DERIVADAS FUNDAMENTALES:
  d/dx[xⁿ]    = n·xⁿ⁻¹         d/dx[eˣ]    = eˣ
  d/dx[ln x]  = 1/x             d/dx[aˣ]    = aˣ·ln(a)
  d/dx[sin x] = cos x           d/dx[cos x] = −sin x
  d/dx[tan x] = sec²x           d/dx[sec x] = sec x·tan x
  d/dx[arcsin x] = 1/√(1−x²)   d/dx[arctan x] = 1/(1+x²)
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = symbols('x')

# ─────────────────────────────────────────────────────────────
# SECCIÓN 1: Reglas básicas
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("  REGLAS BÁSICAS DE DERIVACIÓN")
print("=" * 60)
print("""
  Regla de la Potencia: d/dx[xⁿ] = n·xⁿ⁻¹
  Funciona para cualquier exponente: enteros, fracciones, negativos.
""")

reglas_basicas = [
    (x**5,                "x⁵"),
    (3*x**4 - 2*x**2 + 7, "3x⁴ − 2x² + 7"),
    (sqrt(x),             "√x  = x^(1/2)"),
    (x**Rational(3, 2),   "x^(3/2)"),
    (1/x**3,              "1/x³ = x^(−3)"),
]

print("  Algebraicas y Radicales:")
for f_expr, nombre in reglas_basicas:
    fp = diff(f_expr, x)
    print(f"    f(x) = {nombre:<22} →  f'(x) = {fp}")

print("""
  Exponenciales y Logarítmicas:
  La función eˣ es especial: su derivada ES ella misma.
  Para ln(x), la derivada es 1/x (definida solo para x > 0).
""")
func_exp_log = [
    (exp(x),        "eˣ"),
    (exp(3*x),      "e^(3x)       ← cadena: 3·eˣ"),
    (2**x,          "2ˣ           ← aˣ → aˣ·ln(a)"),
    (log(x),        "ln(x)"),
    (log(x, 10),    "log₁₀(x)"),
    (log(x**2 + 1), "ln(x²+1)    ← cadena"),
]
for f_expr, nombre in func_exp_log:
    fp = simplify(diff(f_expr, x))
    print(f"    f(x) = {nombre:<28} →  f'(x) = {fp}")

print("""
  Trigonométricas:
  Las derivadas de sin y cos forman un ciclo:
    sin → cos → −sin → −cos → sin → ...
""")
func_trig = [
    (sin(x), "sin(x)"),
    (cos(x), "cos(x)"),
    (tan(x), "tan(x)"),
    (sec(x), "sec(x)"),
    (csc(x), "csc(x)"),
    (cot(x), "cot(x)"),
]
for f_expr, nombre in func_trig:
    fp = simplify(diff(f_expr, x))
    print(f"    f(x) = {nombre:<10} →  f'(x) = {fp}")

print("""
  Trigonométricas Inversas:
  Estas aparecen con frecuencia al integrar expresiones con raíces.
  Resultado: derivadas algebraicas (sin trig).
""")
func_inv = [
    (asin(x),   "arcsin(x)"),
    (acos(x),   "arccos(x)"),
    (atan(x),   "arctan(x)"),
    (atan(x/2), "arctan(x/2)"),
]
for f_expr, nombre in func_inv:
    fp = simplify(diff(f_expr, x))
    print(f"    f(x) = {nombre:<14} →  f'(x) = {fp}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 2: Regla del Producto y del Cociente
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  REGLA DEL PRODUCTO Y DEL COCIENTE")
print("=" * 60)
print("""
  ERROR COMÚN: pensar que (u·v)' = u'·v'  → INCORRECTO
  La regla correcta del PRODUCTO es:
      [u·v]' = u'·v + u·v'
  "Derivada del primero por el segundo más el primero por derivada del segundo"

  Para el COCIENTE:
      [u/v]' = (u'·v − u·v') / v²
  "Derivada del numerador por denominador menos numerador por derivada del denominador,
  todo dividido entre el denominador al cuadrado"
""")

print("  Regla del Producto:")
productos = [
    (x**2 * sin(x),       "x² · sin(x)"),
    (exp(x) * cos(x),     "eˣ · cos(x)"),
    (x * log(x),          "x · ln(x)"),
    ((x**2+1) * tan(x),   "(x²+1) · tan(x)"),
]
for f_expr, nombre in productos:
    fp = simplify(diff(f_expr, x))
    print(f"    f(x) = {nombre:<26} →  f'(x) = {fp}")

print("\n  Regla del Cociente:")
cocientes = [
    (sin(x)/x,           "sin(x) / x"),
    (exp(x)/(x**2+1),    "eˣ / (x²+1)"),
    ((x**2-1)/(x**2+1),  "(x²−1) / (x²+1)"),
    (log(x)/x,           "ln(x) / x"),
]
for f_expr, nombre in cocientes:
    fp = simplify(diff(f_expr, x))
    print(f"    f(x) = {nombre:<26} →  f'(x) = {fp}")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 3: Regla de la Cadena
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  REGLA DE LA CADENA")
print("=" * 60)
print("""
  Cuando f(x) = g(h(x))  — función COMPUESTA —
  la derivada se calcula así:

      f'(x) = g'(h(x)) · h'(x)
              ─────────   ─────
              "exterior"  "interior"

  Clave: primero se deriva la función exterior dejando la interior
         intacta, luego se multiplica por la derivada de la interior.

  Ejemplo mental: sin(x²)
    • Exterior: sin(u)  → derivada: cos(u)
    • Interior: u = x²  → derivada: 2x
    • Resultado: cos(x²) · 2x = 2x·cos(x²)
""")

cadena = [
    (sin(x**2),         "sin(x²)",       "exterior=sin, interior=x²"),
    (exp(x**3 + 2*x),   "e^(x³+2x)",     "exterior=eˣ, interior=x³+2x"),
    ((x**2 + 5)**8,     "(x²+5)⁸",       "exterior=u⁸, interior=x²+5"),
    (sqrt(3*x**2 - 1),  "√(3x²−1)",      "exterior=√u, interior=3x²−1"),
    (log(sin(x)),       "ln(sin(x))",     "exterior=ln, interior=sin(x)"),
    (sin(exp(x)),       "sin(eˣ)",        "exterior=sin, interior=eˣ"),
    (atan(sqrt(x)),     "arctan(√x)",     "cadena doble"),
]

for f_expr, nombre, tipo in cadena:
    fp = simplify(diff(f_expr, x))
    print(f"  f(x) = {nombre:<20} [{tipo}]")
    print(f"         f'(x) = {fp}\n")

# ─────────────────────────────────────────────────────────────
# SECCIÓN 4: Visualización
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Módulo 2 — Reglas de Derivación y Regla de la Cadena",
             fontsize=14, fontweight='bold')

xv  = np.linspace(-2, 4, 400)
xv2 = np.linspace(-2*np.pi, 2*np.pi, 500)
colores = ['#1565C0', '#C62828', '#2E7D32', '#6A1B9A', '#E65100', '#00838F']

# f(x)=x³ y su derivada
ax = axes[0, 0]
ax.plot(xv, xv**3,   color=colores[0], lw=2.5, label="f(x) = x³")
ax.plot(xv, 3*xv**2, color=colores[1], lw=2, ls='--', label="f'(x) = 3x²")
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Potencia: d/dx[x³] = 3x²", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_ylim(-15, 30)

# f(x)=sin(x) y su derivada
ax = axes[0, 1]
ax.plot(xv2, np.sin(xv2), color=colores[2], lw=2.5, label="f(x) = sin(x)")
ax.plot(xv2, np.cos(xv2), color=colores[3], lw=2, ls='--', label="f'(x) = cos(x)")
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Trigonométrica: d/dx[sin(x)] = cos(x)", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# f(x)=eˣ y su derivada (son iguales)
ax = axes[0, 2]
xv3 = np.linspace(-2, 3, 300)
ax.plot(xv3, np.exp(xv3), color=colores[4], lw=2.5, label="f(x) = eˣ")
ax.plot(xv3, np.exp(xv3), color=colores[1], lw=2, ls='--', alpha=0.6,
        label="f'(x) = eˣ  (¡igual!)")
ax.set_title("Exponencial: d/dx[eˣ] = eˣ\n(única función = su propia derivada)", fontsize=9)
ax.set_ylim(-1, 15)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y")

# Regla del producto: x²·sin(x)
ax = axes[1, 0]
yf  = xv**2 * np.sin(xv)
yfp = 2*xv*np.sin(xv) + xv**2*np.cos(xv)
ax.plot(xv, yf,  color=colores[0], lw=2.5, label="f(x) = x²·sin(x)")
ax.plot(xv, yfp, color=colores[1], lw=2, ls='--',
        label="f'(x) = 2x·sin(x)+x²·cos(x)")
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Regla del Producto: x²·sin(x)", fontsize=10)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_ylim(-15, 15)

# Regla de la cadena: sin(x²)
ax = axes[1, 1]
yf2  = np.sin(xv**2)
yfp2 = 2*xv*np.cos(xv**2)
ax.plot(xv, yf2,  color=colores[2], lw=2.5, label="f(x) = sin(x²)")
ax.plot(xv, yfp2, color=colores[3], lw=2, ls='--',
        label="f'(x) = 2x·cos(x²)")
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Regla de la Cadena: sin(x²)\nf'=cos(x²)·2x", fontsize=10)
ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_ylim(-10, 10)

# Regla del cociente: sin(x)/x
ax = axes[1, 2]
xv_c = np.linspace(-4*np.pi, 4*np.pi, 800)
xv_c_safe = np.where(xv_c == 0, 1e-10, xv_c)
yf3  = np.sin(xv_c_safe) / xv_c_safe
yfp3 = (xv_c_safe*np.cos(xv_c_safe) - np.sin(xv_c_safe)) / xv_c_safe**2
ax.plot(xv_c, yf3,  color=colores[4], lw=2.5, label="f(x) = sin(x)/x")
ax.plot(xv_c, yfp3, color=colores[5], lw=2, ls='--',
        label="f'(x) = [x·cos(x)−sin(x)]/x²")
ax.axhline(0, color='black', lw=0.8)
ax.set_title("Regla del Cociente: sin(x)/x", fontsize=10)
ax.legend(fontsize=7); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_ylim(-0.5, 1.2)

plt.tight_layout()
plt.savefig("reglas_derivacion.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅  Gráfica guardada: reglas_derivacion.png")

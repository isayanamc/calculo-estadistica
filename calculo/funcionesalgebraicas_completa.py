import numpy as np
import matplotlib.pyplot as plt


def info_funciones_algebraicas():
    """
    Imprime información teórica sobre funciones algebraicas
    """
    print("=" * 80)
    print("FUNCIONES ALGEBRAICAS - DEFINICIONES Y PROPIEDADES")
    print("=" * 80)

    print("\n📊 FUNCIONES POLINÓMICAS:")
    print("-" * 80)

    print("\n1. FUNCIÓN LINEAL: f(x) = mx + b")
    print("   • Definición: Polinomio de grado 1")
    print("   • Forma general: f(x) = mx + b")
    print("   • Dominio: (-∞, ∞)")
    print("   • Rango: (-∞, ∞)")
    print("   • Gráfica: Línea recta")
    print("   • m = pendiente (tasa de cambio)")
    print("   • b = intersección con el eje y")
    print("   • Derivada: f'(x) = m")

    print("\n2. FUNCIÓN CUADRÁTICA: f(x) = ax² + bx + c")
    print("   • Definición: Polinomio de grado 2")
    print("   • Dominio: (-∞, ∞)")
    print("   • Rango: Depende del coeficiente 'a':")
    print("     - Si a > 0: [k, ∞) donde k es el vértice")
    print("     - Si a < 0: (-∞, k] donde k es el vértice")
    print("   • Gráfica: Parábola")
    print("   • Vértice: x = -b/(2a)")
    print("   • Eje de simetría: x = -b/(2a)")
    print("   • Derivada: f'(x) = 2ax + b")
    print("   • Aplicaciones: Trayectorias, optimización")

    print("\n3. FUNCIÓN CÚBICA: f(x) = ax³ + bx² + cx + d")
    print("   • Definición: Polinomio de grado 3")
    print("   • Dominio: (-∞, ∞)")
    print("   • Rango: (-∞, ∞)")
    print("   • Gráfica: Curva en forma de 'S'")
    print("   • Puede tener 1, 2 o 3 raíces reales")
    print("   • Puntos de inflexión: donde f''(x) = 0")
    print("   • Derivada: f'(x) = 3ax² + 2bx + c")

    print("\n4. FUNCIÓN CUÁRTICA: f(x) = ax⁴ + bx³ + cx² + dx + e")
    print("   • Definición: Polinomio de grado 4")
    print("   • Dominio: (-∞, ∞)")
    print("   • Rango: Depende de 'a'")
    print("   • Gráfica: Forma de 'W' o 'M'")
    print("   • Puede tener hasta 4 raíces reales")
    print("   • Derivada: f'(x) = 4ax³ + 3bx² + 2cx + d")

    print("\n📐 FUNCIONES RADICALES:")
    print("-" * 80)

    print("\n5. RAÍZ CUADRADA: f(x) = √x")
    print("   • Definición: Función inversa de x²")
    print("   • Dominio: [0, ∞)")
    print("   • Rango: [0, ∞)")
    print("   • Gráfica: Media parábola horizontal")
    print("   • Derivada: f'(x) = 1/(2√x)")
    print("   • Importante: Solo definida para x ≥ 0")
    print("   • Crece de forma decreciente (desacelerada)")

    print("\n6. RAÍZ CÚBICA: f(x) = ∛x")
    print("   • Definición: Función inversa de x³")
    print("   • Dominio: (-∞, ∞)")
    print("   • Rango: (-∞, ∞)")
    print("   • Gráfica: Curva suave que pasa por el origen")
    print("   • Derivada: f'(x) = 1/(3∛(x²))")
    print("   • Importante: Definida para todos los reales")
    print("   • Punto de inflexión en el origen")

    print("\n7. FUNCIÓN RADICAL GENERAL: f(x) = a√(bx + c) + d")
    print("   • a: factor de estiramiento vertical")
    print("   • b: factor de estiramiento horizontal")
    print("   • c: desplazamiento horizontal")
    print("   • d: desplazamiento vertical")
    print("   • Dominio: Resolver bx + c ≥ 0")

    print("\n📈 FUNCIONES RACIONALES:")
    print("-" * 80)

    print("\n8. FUNCIÓN RACIONAL: f(x) = P(x)/Q(x)")
    print("   • Definición: Razón de dos polinomios")
    print("   • Dominio: Todos los x donde Q(x) ≠ 0")
    print("   • Asíntotas verticales: donde Q(x) = 0")
    print("   • Asíntotas horizontales: límites cuando x → ±∞")
    print("   • Ejemplo simple: f(x) = 1/x")
    print("     - Asíntota vertical: x = 0")
    print("     - Asíntota horizontal: y = 0")

    print("\n🔢 PROPIEDADES GENERALES:")
    print("-" * 80)
    print("   • Función PAR: f(-x) = f(x) → Simétrica respecto al eje y")
    print("   • Función IMPAR: f(-x) = -f(x) → Simétrica respecto al origen")
    print("   • Continuidad: Sin 'saltos' o 'huecos'")
    print("   • Creciente: Si x₁ < x₂ → f(x₁) < f(x₂)")
    print("   • Decreciente: Si x₁ < x₂ → f(x₁) > f(x₂)")
    print("\n" + "=" * 80 + "\n")


def graficar_polinomios_completos():
    """
    Grafica funciones polinómicas con todas sus propiedades
    """
    x = np.linspace(-5, 5, 1000)

    fig, axes = plt.subplots(2, 3, figsize=(20, 12))
    fig.suptitle('Funciones Polinómicas - Gráficas y Propiedades',
                 fontsize=20, fontweight='bold', y=0.995)

    # 1. Lineal: f(x) = 2x + 1
    y1 = 2 * x + 1
    axes[0, 0].plot(x, y1, 'b-', linewidth=3)
    axes[0, 0].set_title('f(x) = 2x + 1 (Lineal)\nDominio: ℝ | Rango: ℝ\nm = 2 (pendiente), b = 1 (intercepto)',
                         fontsize=11, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 0].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 0].plot(0, 1, 'ro', markersize=10, label='Intercepto y')
    axes[0, 0].plot(-0.5, 0, 'go', markersize=10, label='Raíz')
    axes[0, 0].legend()

    # 2. Cuadrática: f(x) = x²
    y2 = x ** 2
    axes[0, 1].plot(x, y2, 'r-', linewidth=3)
    axes[0, 1].set_title('f(x) = x² (Cuadrática)\nDominio: ℝ | Rango: [0, ∞)\nVértice: (0, 0) | Eje simetría: x = 0',
                         fontsize=11, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 1].plot(0, 0, 'ro', markersize=10, label='Vértice (mínimo)')
    axes[0, 1].legend()
    axes[0, 1].set_ylim(-1, 25)

    # 3. Cúbica: f(x) = x³
    y3 = x ** 3
    axes[0, 2].plot(x, y3, 'g-', linewidth=3)
    axes[0, 2].set_title('f(x) = x³ (Cúbica)\nDominio: ℝ | Rango: ℝ\nPunto de inflexión: (0, 0) | Función IMPAR',
                         fontsize=11, fontweight='bold')
    axes[0, 2].grid(True, alpha=0.3)
    axes[0, 2].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 2].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 2].plot(0, 0, 'ro', markersize=10, label='Punto inflexión')
    axes[0, 2].legend()
    axes[0, 2].set_ylim(-50, 50)

    # 4. Cuártica: f(x) = x⁴
    y4 = x ** 4
    axes[1, 0].plot(x, y4, 'purple', linewidth=3)
    axes[1, 0].set_title('f(x) = x⁴ (Cuártica)\nDominio: ℝ | Rango: [0, ∞)\nVértice: (0, 0) | Función PAR',
                         fontsize=11, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 0].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 0].plot(0, 0, 'ro', markersize=10, label='Mínimo absoluto')
    axes[1, 0].legend()
    axes[1, 0].set_ylim(-10, 200)

    # 5. Parábola con vértice: f(x) = -(x-1)² + 4
    y5 = -(x - 1) ** 2 + 4
    axes[1, 1].plot(x, y5, 'orange', linewidth=3)
    axes[1, 1].set_title('f(x) = -(x-1)² + 4\nDominio: ℝ | Rango: (-∞, 4]\nVértice: (1, 4) | Abre hacia abajo',
                         fontsize=11, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 1].plot(1, 4, 'ro', markersize=10, label='Vértice (máximo)')
    axes[1, 1].axvline(x=1, color='red', linestyle='--', alpha=0.5, label='Eje simetría')
    # Calcular y marcar raíces
    raices = [1 - 2, 1 + 2]
    axes[1, 1].plot(raices, [0, 0], 'go', markersize=10, label='Raíces')
    axes[1, 1].legend()

    # 6. Polinomio mixto: f(x) = x³ - 3x² + 2
    y6 = x ** 3 - 3 * x ** 2 + 2
    axes[1, 2].plot(x, y6, 'brown', linewidth=3)
    axes[1, 2].set_title('f(x) = x³ - 3x² + 2\nDominio: ℝ | Rango: ℝ\nTiene máximo y mínimo locales',
                         fontsize=11, fontweight='bold')
    axes[1, 2].grid(True, alpha=0.3)
    axes[1, 2].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 2].axvline(x=0, color='k', linewidth=0.5)
    # Calcular puntos críticos (derivada = 0: 3x² - 6x = 0)
    x_criticos = [0, 2]
    y_criticos = [2, -2]
    axes[1, 2].plot(x_criticos, y_criticos, 'ro', markersize=10, label='Puntos críticos')
    axes[1, 2].legend()
    axes[1, 2].set_ylim(-20, 20)

    plt.tight_layout()
    plt.show()


def graficar_radicales_completos():
    """
    Grafica funciones radicales con todas sus propiedades
    """
    fig, axes = plt.subplots(2, 3, figsize=(20, 12))
    fig.suptitle('Funciones Radicales - Gráficas y Propiedades',
                 fontsize=20, fontweight='bold', y=0.995)

    # 1. Raíz cuadrada básica
    x1 = np.linspace(0, 10, 1000)
    y1 = np.sqrt(x1)
    axes[0, 0].plot(x1, y1, 'b-', linewidth=3)
    axes[0, 0].set_title('f(x) = √x\nDominio: [0, ∞) | Rango: [0, ∞)\nCrecimiento desacelerado',
                         fontsize=11, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 0].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 0].plot(0, 0, 'ro', markersize=10, label='Punto inicial')
    axes[0, 0].plot([1, 4, 9], [1, 2, 3], 'go', markersize=8, label='Puntos notables')
    axes[0, 0].legend()

    # 2. Raíz cúbica
    x2 = np.linspace(-10, 10, 1000)
    y2 = np.cbrt(x2)
    axes[0, 1].plot(x2, y2, 'r-', linewidth=3)
    axes[0, 1].set_title('f(x) = ∛x\nDominio: ℝ | Rango: ℝ\nFunción IMPAR | Punto inflexión: (0,0)',
                         fontsize=11, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 1].plot(0, 0, 'ro', markersize=10, label='Punto inflexión')
    axes[0, 1].plot([1, 8, -1, -8], [1, 2, -1, -2], 'go', markersize=8, label='Puntos notables')
    axes[0, 1].legend()

    # 3. f(x) = 2√x + 1 (transformación)
    y3 = 2 * np.sqrt(x1) + 1
    axes[0, 2].plot(x1, y3, 'g-', linewidth=3)
    axes[0, 2].set_title('f(x) = 2√x + 1\nDominio: [0, ∞) | Rango: [1, ∞)\nEstiramiento vertical × 2, despl. vert. +1',
                         fontsize=11, fontweight='bold')
    axes[0, 2].grid(True, alpha=0.3)
    axes[0, 2].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 2].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 2].plot(0, 1, 'ro', markersize=10, label='Punto inicial (0,1)')
    axes[0, 2].axhline(y=1, color='red', linestyle='--', alpha=0.5, label='Valor mínimo')
    axes[0, 2].legend()

    # 4. f(x) = √(x+2) - 1 (desplazamientos)
    x4 = np.linspace(-2, 10, 1000)
    y4 = np.sqrt(x4 + 2) - 1
    axes[1, 0].plot(x4, y4, 'purple', linewidth=3)
    axes[1, 0].set_title('f(x) = √(x+2) - 1\nDominio: [-2, ∞) | Rango: [-1, ∞)\nDespl. horiz. -2, despl. vert. -1',
                         fontsize=11, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 0].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 0].plot(-2, -1, 'ro', markersize=10, label='Punto inicial (-2,-1)')
    axes[1, 0].axvline(x=-2, color='red', linestyle='--', alpha=0.5, label='Límite dominio')
    axes[1, 0].legend()

    # 5. Semicírculo: f(x) = √(16 - x²)
    x5 = np.linspace(-4, 4, 1000)
    y5 = np.sqrt(16 - x5 ** 2)
    axes[1, 1].plot(x5, y5, 'orange', linewidth=3)
    axes[1, 1].set_title('f(x) = √(16 - x²)\nDominio: [-4, 4] | Rango: [0, 4]\nSemicírculo de radio 4',
                         fontsize=11, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 1].plot(0, 4, 'ro', markersize=10, label='Punto máximo (0,4)')
    axes[1, 1].plot([-4, 4], [0, 0], 'go', markersize=10, label='Extremos')
    axes[1, 1].set_aspect('equal')
    axes[1, 1].legend()

    # 6. Raíz cuadrada inversa: f(x) = -√x
    y6 = -np.sqrt(x1)
    axes[1, 2].plot(x1, y6, 'brown', linewidth=3)
    axes[1, 2].set_title('f(x) = -√x\nDominio: [0, ∞) | Rango: (-∞, 0]\nReflexión de √x respecto al eje x',
                         fontsize=11, fontweight='bold')
    axes[1, 2].grid(True, alpha=0.3)
    axes[1, 2].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 2].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 2].plot(0, 0, 'ro', markersize=10, label='Punto inicial')
    axes[1, 2].legend()

    plt.tight_layout()
    plt.show()


def graficar_racionales_completos():
    """
    Grafica funciones racionales con asíntotas
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Funciones Racionales - Gráficas y Asíntotas',
                 fontsize=20, fontweight='bold', y=0.995)

    # 1. f(x) = 1/x
    x1_pos = np.linspace(0.1, 10, 500)
    x1_neg = np.linspace(-10, -0.1, 500)
    y1_pos = 1 / x1_pos
    y1_neg = 1 / x1_neg
    axes[0, 0].plot(x1_pos, y1_pos, 'b-', linewidth=3)
    axes[0, 0].plot(x1_neg, y1_neg, 'b-', linewidth=3)
    axes[0, 0].axvline(x=0, color='red', linestyle='--', linewidth=2, label='Asíntota vertical: x=0')
    axes[0, 0].axhline(y=0, color='green', linestyle='--', linewidth=2, label='Asíntota horizontal: y=0')
    axes[0, 0].set_title('f(x) = 1/x\nDominio: ℝ - {0} | Rango: ℝ - {0}\nFunción IMPAR | Hipérbola',
                         fontsize=11, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_xlim(-10, 10)
    axes[0, 0].set_ylim(-10, 10)
    axes[0, 0].legend()

    # 2. f(x) = 1/x²
    y2_pos = 1 / x1_pos ** 2
    y2_neg = 1 / x1_neg ** 2
    axes[0, 1].plot(x1_pos, y2_pos, 'r-', linewidth=3)
    axes[0, 1].plot(x1_neg, y2_neg, 'r-', linewidth=3)
    axes[0, 1].axvline(x=0, color='red', linestyle='--', linewidth=2, label='Asíntota vertical: x=0')
    axes[0, 1].axhline(y=0, color='green', linestyle='--', linewidth=2, label='Asíntota horizontal: y=0')
    axes[0, 1].set_title('f(x) = 1/x²\nDominio: ℝ - {0} | Rango: (0, ∞)\nFunción PAR | Siempre positiva',
                         fontsize=11, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_xlim(-10, 10)
    axes[0, 1].set_ylim(-1, 10)
    axes[0, 1].legend()

    # 3. f(x) = (x+1)/(x-2)
    x3 = np.linspace(-10, 10, 2000)
    y3 = (x3 + 1) / (x3 - 2)
    # Eliminar valores cerca de la asíntota
    y3[np.abs(y3) > 50] = np.nan
    axes[1, 0].plot(x3, y3, 'g-', linewidth=3)
    axes[1, 0].axvline(x=2, color='red', linestyle='--', linewidth=2, label='Asíntota vertical: x=2')
    axes[1, 0].axhline(y=1, color='green', linestyle='--', linewidth=2, label='Asíntota horizontal: y=1')
    axes[1, 0].set_title('f(x) = (x+1)/(x-2)\nDominio: ℝ - {2} | Intercepto y: -1/2\nIntercepto x: -1',
                         fontsize=11, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_xlim(-10, 10)
    axes[1, 0].set_ylim(-10, 10)
    axes[1, 0].plot(-1, 0, 'ro', markersize=10, label='Raíz: x=-1')
    axes[1, 0].plot(0, -0.5, 'bo', markersize=10, label='Intercepto y')
    axes[1, 0].legend()

    # 4. f(x) = x/(x²-4) = x/((x-2)(x+2))
    y4 = x3 / (x3 ** 2 - 4)
    y4[np.abs(y4) > 50] = np.nan
    axes[1, 1].plot(x3, y4, 'purple', linewidth=3)
    axes[1, 1].axvline(x=2, color='red', linestyle='--', linewidth=2, label='Asíntota vert: x=2')
    axes[1, 1].axvline(x=-2, color='red', linestyle='--', linewidth=2, label='Asíntota vert: x=-2')
    axes[1, 1].axhline(y=0, color='green', linestyle='--', linewidth=2, label='Asíntota horiz: y=0')
    axes[1, 1].set_title('f(x) = x/(x²-4)\nDominio: ℝ - {-2, 2} | Función IMPAR\nDos asíntotas verticales',
                         fontsize=11, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].set_xlim(-10, 10)
    axes[1, 1].set_ylim(-5, 5)
    axes[1, 1].plot(0, 0, 'ro', markersize=10, label='Origen (raíz)')
    axes[1, 1].legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Primero mostrar la información teórica
    info_funciones_algebraicas()

    # Esperar a que el usuario lea
    input("Presiona ENTER para ver las gráficas de POLINOMIOS...")
    graficar_polinomios_completos()

    input("\nPresiona ENTER para ver las gráficas de RADICALES...")
    graficar_radicales_completos()

    input("\nPresiona ENTER para ver las gráficas de RACIONALES...")
    graficar_racionales_completos()

    print("\n✅ ¡Repaso completado! Guarda estas gráficas para estudiar.")
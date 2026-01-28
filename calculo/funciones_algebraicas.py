import numpy as np
import matplotlib.pyplot as plt


def graficar_polinomios():
    """
    Grafica diferentes tipos de funciones polinómicas
    """
    x = np.linspace(-5, 5, 1000)

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('Funciones Algebraicas - Polinomios', fontsize=18, fontweight='bold')

    # 1. Lineal: f(x) = 2x + 1
    axes[0, 0].plot(x, 2 * x + 1, 'b-', linewidth=2)
    axes[0, 0].set_title('Lineal: f(x) = 2x + 1', fontsize=12, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 0].axvline(x=0, color='k', linewidth=0.5)

    # 2. Cuadrática: f(x) = x²
    axes[0, 1].plot(x, x ** 2, 'r-', linewidth=2)
    axes[0, 1].set_title('Cuadrática: f(x) = x²', fontsize=12, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 1].axvline(x=0, color='k', linewidth=0.5)

    # 3. Cúbica: f(x) = x³
    axes[0, 2].plot(x, x ** 3, 'g-', linewidth=2)
    axes[0, 2].set_title('Cúbica: f(x) = x³', fontsize=12, fontweight='bold')
    axes[0, 2].grid(True, alpha=0.3)
    axes[0, 2].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 2].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 2].set_ylim(-50, 50)

    # 4. Cuártica: f(x) = x⁴
    axes[1, 0].plot(x, x ** 4, 'purple', linewidth=2)
    axes[1, 0].set_title('Cuártica: f(x) = x⁴', fontsize=12, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 0].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 0].set_ylim(-10, 200)

    # 5. Polinomio mixto: f(x) = x³ - 3x² + 2
    axes[1, 1].plot(x, x ** 3 - 3 * x ** 2 + 2, 'orange', linewidth=2)
    axes[1, 1].set_title('Mixto: f(x) = x³ - 3x² + 2', fontsize=12, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 1].set_ylim(-20, 20)

    # 6. Parábola invertida: f(x) = -x² + 4
    axes[1, 2].plot(x, -x ** 2 + 4, 'brown', linewidth=2)
    axes[1, 2].set_title('Parábola invertida: f(x) = -x² + 4', fontsize=12, fontweight='bold')
    axes[1, 2].grid(True, alpha=0.3)
    axes[1, 2].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 2].axvline(x=0, color='k', linewidth=0.5)

    plt.tight_layout()
    plt.show()


def graficar_radicales():
    """
    Grafica funciones con radicales
    """
    x = np.linspace(0, 10, 1000)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Funciones Algebraicas - Radicales', fontsize=18, fontweight='bold')

    # 1. Raíz cuadrada
    axes[0, 0].plot(x, np.sqrt(x), 'b-', linewidth=2)
    axes[0, 0].set_title('f(x) = √x', fontsize=14, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 0].axvline(x=0, color='k', linewidth=0.5)

    # 2. Raíz cúbica (puede tener valores negativos)
    x_cubica = np.linspace(-10, 10, 1000)
    axes[0, 1].plot(x_cubica, np.cbrt(x_cubica), 'r-', linewidth=2)
    axes[0, 1].set_title('f(x) = ∛x', fontsize=14, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 1].axvline(x=0, color='k', linewidth=0.5)

    # 3. f(x) = 2√x + 1
    axes[1, 0].plot(x, 2 * np.sqrt(x) + 1, 'g-', linewidth=2)
    axes[1, 0].set_title('f(x) = 2√x + 1', fontsize=14, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 0].axvline(x=0, color='k', linewidth=0.5)

    # 4. f(x) = √(16 - x²) (semicírculo)
    x_circulo = np.linspace(-4, 4, 1000)
    y_circulo = np.sqrt(16 - x_circulo ** 2)
    axes[1, 1].plot(x_circulo, y_circulo, 'purple', linewidth=2)
    axes[1, 1].set_title('f(x) = √(16 - x²)', fontsize=14, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 1].set_aspect('equal')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("=== Graficando funciones polinómicas ===")
    graficar_polinomios()

    print("\n=== Graficando funciones radicales ===")
    graficar_radicales()
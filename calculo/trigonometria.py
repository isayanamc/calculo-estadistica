import numpy as np
import matplotlib.pyplot as plt


def graficar_funciones_trig(x_min=-2 * np.pi, x_max=2 * np.pi):
    """
    Grafica las 6 funciones trigonométricas principales
    """
    x = np.linspace(x_min, x_max, 1000)

    # Crear figura con 6 subplots (2 filas, 3 columnas)
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('Funciones Trigonométricas', fontsize=18, fontweight='bold')

    # 1. sin(x)
    axes[0, 0].plot(x, np.sin(x), 'b-', linewidth=2)
    axes[0, 0].set_title('sin(x)', fontsize=14, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 0].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 0].set_ylim(-1.5, 1.5)

    # 2. cos(x)
    axes[0, 1].plot(x, np.cos(x), 'r-', linewidth=2)
    axes[0, 1].set_title('cos(x)', fontsize=14, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 1].set_ylim(-1.5, 1.5)

    # 3. tan(x)
    y_tan = np.tan(x)
    # Limitar valores extremos para mejor visualización
    y_tan[np.abs(y_tan) > 10] = np.nan
    axes[0, 2].plot(x, y_tan, 'g-', linewidth=2)
    axes[0, 2].set_title('tan(x)', fontsize=14, fontweight='bold')
    axes[0, 2].grid(True, alpha=0.3)
    axes[0, 2].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 2].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 2].set_ylim(-5, 5)

    # 4. csc(x) = 1/sin(x)
    y_csc = 1 / np.sin(x)
    y_csc[np.abs(y_csc) > 10] = np.nan
    axes[1, 0].plot(x, y_csc, 'purple', linewidth=2)
    axes[1, 0].set_title('csc(x) = 1/sin(x)', fontsize=14, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 0].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 0].set_ylim(-5, 5)

    # 5. sec(x) = 1/cos(x)
    y_sec = 1 / np.cos(x)
    y_sec[np.abs(y_sec) > 10] = np.nan
    axes[1, 1].plot(x, y_sec, 'orange', linewidth=2)
    axes[1, 1].set_title('sec(x) = 1/cos(x)', fontsize=14, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 1].set_ylim(-5, 5)

    # 6. cot(x) = 1/tan(x)
    y_cot = 1 / np.tan(x)
    y_cot[np.abs(y_cot) > 10] = np.nan
    axes[1, 2].plot(x, y_cot, 'brown', linewidth=2)
    axes[1, 2].set_title('cot(x) = 1/tan(x)', fontsize=14, fontweight='bold')
    axes[1, 2].grid(True, alpha=0.3)
    axes[1, 2].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 2].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 2].set_ylim(-5, 5)

    plt.tight_layout()
    plt.show()


def comparar_sin_cos():
    """
    Compara sin(x) y cos(x) en la misma gráfica
    """
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    plt.figure(figsize=(12, 6))
    plt.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
    plt.plot(x, np.cos(x), 'r--', linewidth=2, label='cos(x)')

    # Marcar puntos importantes
    puntos_x = [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]
    for px in puntos_x:
        plt.axvline(x=px, color='gray', linestyle=':', alpha=0.5)

    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Comparación: sin(x) vs cos(x)', fontsize=16, fontweight='bold')
    plt.legend(fontsize=12)
    plt.ylim(-1.5, 1.5)

    # Agregar etiquetas en el eje x
    plt.xticks(
        [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
        ['-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π']
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("=== Graficando todas las funciones trigonométricas ===")
    graficar_funciones_trig()

    print("\n=== Comparando sin(x) y cos(x) ===")
    comparar_sin_cos()
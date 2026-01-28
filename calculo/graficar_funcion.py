import numpy as np
import matplotlib.pyplot as plt


def graficar_funcion_y_derivada(func, x_min=-10, x_max=10, titulo="Función y su Derivada"):
    """
    Grafica una función y su derivada lado a lado

    Args:
        func: función a graficar (ejemplo: lambda x: x**2)
        x_min: valor mínimo de x
        x_max: valor máximo de x
        titulo: título del gráfico
    """
    # Crear puntos en x
    x = np.linspace(x_min, x_max, 1000)

    # Calcular y (la función)
    y = func(x)

    # Calcular y' (la derivada) numéricamente usando gradiente
    y_derivada = np.gradient(y, x)

    # Crear el gráfico con 2 subplots
    plt.figure(figsize=(14, 6))

    # Subplot 1: La función original
    plt.subplot(1, 2, 1)
    plt.plot(x, y, 'b-', linewidth=2, label='f(x)')
    plt.grid(True, alpha=0.3)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('f(x)', fontsize=12)
    plt.title('Función Original', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)

    # Subplot 2: La derivada
    plt.subplot(1, 2, 2)
    plt.plot(x, y_derivada, 'r-', linewidth=2, label="f'(x)")
    plt.grid(True, alpha=0.3)
    plt.xlabel('x', fontsize=12)
    plt.ylabel("f'(x)", fontsize=12)
    plt.title('Derivada', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)

    plt.suptitle(titulo, fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()


# EJEMPLOS DE USO
if __name__ == "__main__":
    print("=== Ejemplo 1: f(x) = x² ===")
    graficar_funcion_y_derivada(
        func=lambda x: x ** 2,
        x_min=-5,
        x_max=5,
        titulo="f(x) = x²   →   f'(x) = 2x"
    )

    print("\n=== Ejemplo 2: f(x) = sin(x) ===")
    graficar_funcion_y_derivada(
        func=lambda x: np.sin(x),
        x_min=-2 * np.pi,
        x_max=2 * np.pi,
        titulo="f(x) = sin(x)   →   f'(x) = cos(x)"
    )

    print("\n=== Ejemplo 3: f(x) = e^x ===")
    graficar_funcion_y_derivada(
        func=lambda x: np.exp(x),
        x_min=-2,
        x_max=2,
        titulo="f(x) = e^x   →   f'(x) = e^x"
    )
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def calcular_limite_racionalizacion():
    x = sp.Symbol('x')

    # Definición de la función según tus notas: (sqrt(x+1) - 1) / x
    numerador = sp.sqrt(x + 1) - 1
    denominador = x
    f_expr = numerador / denominador
    punto_critico = 0

    print("PASO 1: EVALUACIÓN")
    # Verificamos la forma indeterminada 0/0 [cite: 122, 182]
    eval_num = numerador.subs(x, punto_critico)
    eval_den = denominador.subs(x, punto_critico)
    print(f"f({punto_critico}) = {eval_num}/{eval_den} -> Indeterminado")

    print("\nPASO 2: IDENTIFICAR EL INDETERMINADOR")
    # El factor que causa el problema es x [cite: 127]
    print(f"Como x tiende a {punto_critico}, el factor problemático es: x")

    print("\nPASO 3: RESOLVER POR RACIONALIZACIÓN")
    # Aplicamos la técnica del conjugado para eliminar la raíz [cite: 139, 146]
    conjugado = sp.sqrt(x + 1) + 1
    print(f"Multiplicando por el conjugado: {conjugado}")

    # Sympy resuelve cancelando al mal portado internamente [cite: 157, 187]
    resultado_limite = sp.limit(f_expr, x, punto_critico)
    print(f"Resultado final: {resultado_limite}")

    # Visualización gráfica para tu Portafolio [cite: 1307]
    x_vals = np.linspace(-0.99, 2, 400)
    f_num = sp.lambdify(x, f_expr, "numpy")
    y_vals = f_num(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="f(x) Racionalizada", color='green')
    plt.plot(punto_critico, float(resultado_limite), 'ro', markerfacecolor='white', label='Hueco (Límite)')
    plt.axvline(0, color='black', lw=0.5)
    plt.axhline(0, color='black', lw=0.5)
    plt.title("Análisis Gráfico: Racionalización de Límites")
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Asegúrate de que PyCharm ejecute este archivo directamente sin argumentos adicionales
    calcular_limite_racionalizacion()
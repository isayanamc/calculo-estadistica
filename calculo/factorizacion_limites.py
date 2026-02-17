import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def calcular_limite_factorizacion():
    x = sp.Symbol('x')

    # Definicion de la funcion: (x^2 + 4x + 3) / (x + 3)
    # Basado en los ejercicios de limites algebraicos de la clase
    numerador = x ** 2 + 4 * x + 3
    denominador = x + 3
    f_expr = numerador / denominador
    punto_critico = -3

    print("PASO 1: EVALUAR")
    # Se realiza la sustitucion directa para comprobar la forma 0/0
    eval_num = numerador.subs(x, punto_critico)
    eval_den = denominador.subs(x, punto_critico)
    print(f"Al evaluar x = {punto_critico} obtenemos: {eval_num}/{eval_den}")
    print("Resultado: Forma indeterminada 0/0")

    print("\nPASO 2: INDETERMINADOR")
    # El 'mal portado' es el factor que hace que el denominador sea cero
    indeterminador = x - punto_critico
    print(f"Como x -> {punto_critico}, el factor a cancelar es: ({indeterminador})")

    print("\nPASO 3: RESOLVER (FACTORIZAR Y CANCELAR)")
    # Se descompone el numerador en sus factores
    num_factorizado = sp.factor(numerador)
    print(f"Numerador factorizado: {num_factorizado}")

    # El limite se calcula simplificando la expresion
    resultado_limite = sp.limit(f_expr, x, punto_critico)
    print(f"Limite final tras cancelacion: {resultado_limite}")

    # Visualizacion grafica para el Portafolio de evidencias
    x_range = np.linspace(punto_critico - 2, punto_critico + 2, 400)
    # Generacion de valores evitando la division por cero para el grafico
    y_range = [(v ** 2 + 4 * v + 3) / (v + 3) if v != -3 else None for v in x_range]

    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_range, label="f(x) Factorizada", color='blue')
    plt.plot(punto_critico, float(resultado_limite), 'ro', markerfacecolor='white', label='Punto Indeterminado')
    plt.axvline(0, color='black', lw=0.5)
    plt.axhline(0, color='black', lw=0.5)
    plt.title("Analisis de Limites por Factorizacion")
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    calcular_limite_factorizacion()
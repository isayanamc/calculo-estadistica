import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def calcular_limites_absolutos_detallado():
    x = sp.Symbol('x')

    # 1. Definicion de la funcion y punto critico
    # Basado en el ejemplo de la clase: |x - 3| / (x - 3)
    numerador = sp.Abs(x - 3)
    denominador = x - 3
    f_expr = numerador / denominador
    punto_critico = 3

    print("--- ANALISIS DE LIMITE CON VALOR ABSOLUTO ---")

    # PASO 1: EVALUACION INICIAL
    # Se comprueba la forma indeterminada 0/0
    eval_num = numerador.subs(x, punto_critico)
    eval_den = denominador.subs(x, punto_critico)
    print(f"PASO 1: Evaluar en x = {punto_critico}")
    print(f"Resultado: {eval_num}/{eval_den} -> Indeterminado 0/0")

    # PASO 2: COMPORTAMIENTO DEL VALOR ABSOLUTO (EL MAL PORTADO)
    # Segun la teoria, el valor absoluto cambia de definicion en el punto critico
    print("\nPASO 2: Analisis del Indeterminador")
    print(f"Para x < {punto_critico} (izquierda), |x-3| se comporta como -(x-3)")
    print(f"Para x > {punto_critico} (derecha), |x-3| se comporta como (x-3)")

    # PASO 3: CALCULO DE LIMITES LATERALES
    print("\nPASO 3: Resolver limites laterales")
    limite_izq = sp.limit(f_expr, x, punto_critico, dir='-')
    limite_der = sp.limit(f_expr, x, punto_critico, dir='+')

    print(f"Limite por la izquierda (x -> {punto_critico}-): {limite_izq}")
    print(f"Limite por la derecha   (x -> {punto_critico}+): {limite_der}")

    # PASO 4: CONCLUSION SOBRE LA EXISTENCIA
    print("\nPASO 4: Conclusion")
    if limite_izq != limite_der:
        print(f"Como {limite_izq} != {limite_der}, el limite NO EXISTE en x = {punto_critico}")
    else:
        print(f"Los laterales coinciden. El limite es {limite_izq}")

    # REPRESENTACION GRAFICA
    # Se genera el grafico para mostrar la discontinuidad no evitable
    x_vals = np.linspace(punto_critico - 2, punto_critico + 2, 1000)
    y_vals = [float(f_expr.subs(x, v)) if v != punto_critico else None for v in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="f(x) = |x-3|/(x-3)", color='purple', lw=2)

    # Marcadores de los limites laterales
    plt.plot(punto_critico, float(limite_izq), 'ro', markerfacecolor='white')
    plt.plot(punto_critico, float(limite_der), 'ro', markerfacecolor='white')

    plt.axvline(punto_critico, color='gray', linestyle='--', alpha=0.5)
    plt.title("Grafico de Discontinuidad por Valor Absoluto")
    plt.grid(True, linestyle=':')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    calcular_limites_absolutos_detallado()
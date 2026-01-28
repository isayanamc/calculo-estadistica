import numpy as np
import matplotlib.pyplot as plt


def info_funciones_trig():
    """
    Imprime información teórica sobre funciones trigonométricas
    """
    print("=" * 80)
    print("FUNCIONES TRIGONOMÉTRICAS - DEFINICIONES Y PROPIEDADES")
    print("=" * 80)

    print("\n📐 FUNCIONES BÁSICAS:")
    print("-" * 80)

    print("\n1. SENO: sin(x)")
    print("   • Definición: Razón entre cateto opuesto e hipotenusa")
    print("   • Dominio: (-∞, ∞)")
    print("   • Rango: [-1, 1]")
    print("   • Período: 2π")
    print("   • Derivada: cos(x)")
    print("   • Valores importantes:")
    print("     - sin(0) = 0")
    print("     - sin(π/6) = 1/2")
    print("     - sin(π/4) = √2/2")
    print("     - sin(π/3) = √3/2")
    print("     - sin(π/2) = 1")

    print("\n2. COSENO: cos(x)")
    print("   • Definición: Razón entre cateto adyacente e hipotenusa")
    print("   • Dominio: (-∞, ∞)")
    print("   • Rango: [-1, 1]")
    print("   • Período: 2π")
    print("   • Derivada: -sin(x)")
    print("   • Valores importantes:")
    print("     - cos(0) = 1")
    print("     - cos(π/6) = √3/2")
    print("     - cos(π/4) = √2/2")
    print("     - cos(π/3) = 1/2")
    print("     - cos(π/2) = 0")

    print("\n3. TANGENTE: tan(x)")
    print("   • Definición: tan(x) = sin(x)/cos(x)")
    print("   • Dominio: x ≠ π/2 + nπ (donde n es entero)")
    print("   • Rango: (-∞, ∞)")
    print("   • Período: π")
    print("   • Derivada: sec²(x)")
    print("   • Asíntotas verticales en x = π/2 + nπ")

    print("\n📐 FUNCIONES RECÍPROCAS:")
    print("-" * 80)

    print("\n4. COSECANTE: csc(x)")
    print("   • Definición: csc(x) = 1/sin(x)")
    print("   • Dominio: x ≠ nπ (donde n es entero)")
    print("   • Rango: (-∞, -1] ∪ [1, ∞)")
    print("   • Período: 2π")
    print("   • Derivada: -csc(x)cot(x)")

    print("\n5. SECANTE: sec(x)")
    print("   • Definición: sec(x) = 1/cos(x)")
    print("   • Dominio: x ≠ π/2 + nπ")
    print("   • Rango: (-∞, -1] ∪ [1, ∞)")
    print("   • Período: 2π")
    print("   • Derivada: sec(x)tan(x)")

    print("\n6. COTANGENTE: cot(x)")
    print("   • Definición: cot(x) = 1/tan(x) = cos(x)/sin(x)")
    print("   • Dominio: x ≠ nπ")
    print("   • Rango: (-∞, ∞)")
    print("   • Período: π")
    print("   • Derivada: -csc²(x)")

    print("\n📊 IDENTIDADES TRIGONOMÉTRICAS IMPORTANTES:")
    print("-" * 80)
    print("   • Identidad Pitagórica: sin²(x) + cos²(x) = 1")
    print("   • tan²(x) + 1 = sec²(x)")
    print("   • cot²(x) + 1 = csc²(x)")
    print("   • sin(2x) = 2sin(x)cos(x)")
    print("   • cos(2x) = cos²(x) - sin²(x)")
    print("\n" + "=" * 80 + "\n")


def graficar_funciones_trig_completas():
    """
    Grafica las 6 funciones trigonométricas con anotaciones
    """
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    fig, axes = plt.subplots(2, 3, figsize=(20, 12))
    fig.suptitle('Funciones Trigonométricas - Gráficas y Propiedades',
                 fontsize=20, fontweight='bold', y=0.995)

    # 1. sin(x)
    axes[0, 0].plot(x, np.sin(x), 'b-', linewidth=3)
    axes[0, 0].set_title('sin(x)\nDominio: ℝ | Rango: [-1, 1] | Período: 2π',
                         fontsize=12, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 0].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 0].set_ylim(-1.5, 1.5)
    axes[0, 0].set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
    axes[0, 0].set_xticklabels(['-2π', '-π', '0', 'π', '2π'])
    # Marcar puntos importantes
    axes[0, 0].plot([0, np.pi / 2, np.pi], [0, 1, 0], 'ro', markersize=8)

    # 2. cos(x)
    axes[0, 1].plot(x, np.cos(x), 'r-', linewidth=3)
    axes[0, 1].set_title('cos(x)\nDominio: ℝ | Rango: [-1, 1] | Período: 2π',
                         fontsize=12, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 1].set_ylim(-1.5, 1.5)
    axes[0, 1].set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
    axes[0, 1].set_xticklabels(['-2π', '-π', '0', 'π', '2π'])
    axes[0, 1].plot([0, np.pi / 2, np.pi], [1, 0, -1], 'ro', markersize=8)

    # 3. tan(x)
    y_tan = np.tan(x)
    y_tan[np.abs(y_tan) > 10] = np.nan
    axes[0, 2].plot(x, y_tan, 'g-', linewidth=3)
    axes[0, 2].set_title('tan(x) = sin(x)/cos(x)\nDominio: x ≠ π/2 + nπ | Rango: ℝ | Período: π',
                         fontsize=12, fontweight='bold')
    axes[0, 2].grid(True, alpha=0.3)
    axes[0, 2].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 2].axvline(x=0, color='k', linewidth=0.5)
    axes[0, 2].set_ylim(-5, 5)
    axes[0, 2].set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
    axes[0, 2].set_xticklabels(['-2π', '-π', '0', 'π', '2π'])
    # Marcar asíntotas
    for asintota in [-3 * np.pi / 2, -np.pi / 2, np.pi / 2, 3 * np.pi / 2]:
        axes[0, 2].axvline(x=asintota, color='red', linestyle='--', alpha=0.5, linewidth=2)

    # 4. csc(x)
    y_csc = 1 / np.sin(x)
    y_csc[np.abs(y_csc) > 10] = np.nan
    axes[1, 0].plot(x, y_csc, 'purple', linewidth=3)
    axes[1, 0].set_title('csc(x) = 1/sin(x)\nDominio: x ≠ nπ | Rango: (-∞,-1]∪[1,∞) | Período: 2π',
                         fontsize=12, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 0].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 0].set_ylim(-5, 5)
    axes[1, 0].set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
    axes[1, 0].set_xticklabels(['-2π', '-π', '0', 'π', '2π'])

    # 5. sec(x)
    y_sec = 1 / np.cos(x)
    y_sec[np.abs(y_sec) > 10] = np.nan
    axes[1, 1].plot(x, y_sec, 'orange', linewidth=3)
    axes[1, 1].set_title('sec(x) = 1/cos(x)\nDominio: x ≠ π/2 + nπ | Rango: (-∞,-1]∪[1,∞) | Período: 2π',
                         fontsize=12, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 1].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 1].set_ylim(-5, 5)
    axes[1, 1].set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
    axes[1, 1].set_xticklabels(['-2π', '-π', '0', 'π', '2π'])

    # 6. cot(x)
    y_cot = 1 / np.tan(x)
    y_cot[np.abs(y_cot) > 10] = np.nan
    axes[1, 2].plot(x, y_cot, 'brown', linewidth=3)
    axes[1, 2].set_title('cot(x) = 1/tan(x)\nDominio: x ≠ nπ | Rango: ℝ | Período: π',
                         fontsize=12, fontweight='bold')
    axes[1, 2].grid(True, alpha=0.3)
    axes[1, 2].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 2].axvline(x=0, color='k', linewidth=0.5)
    axes[1, 2].set_ylim(-5, 5)
    axes[1, 2].set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
    axes[1, 2].set_xticklabels(['-2π', '-π', '0', 'π', '2π'])

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Primero mostrar la información teórica
    info_funciones_trig()

    # Luego mostrar las gráficas
    input("Presiona ENTER para ver las gráficas...")
    graficar_funciones_trig_completas()
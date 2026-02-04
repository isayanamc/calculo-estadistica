import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

print("="*80)
print("PROBLEMA 3: TIEMPO DE RESPUESTA DE APLICACIÓN")
print("="*80)
print("\nFunción: T(n) = (n³ - 8)/(n - 2)")
print("Contexto: Tiempo promedio de respuesta con n usuarios simultáneos")
print("\n" + "-"*80)

# Definir la función
def T(n):
    return (n**3 - 8) / (n - 2)

# ============================================================================
# TAREA 1: Calcular valores cercanos a n = 2
# ============================================================================
print("\n[TAREA 1] Calculando T(n) para valores cercanos a n = 2:")
print("-"*80)

valores_prueba = [1.9, 1.95, 1.99, 1.999, 2.001, 2.01, 2.05, 2.1]
print(f"{'n':^10} | {'T(n)':^15}")
print("-"*30)
for n_val in valores_prueba:
    try:
        resultado = T(n_val)
        print(f"{n_val:^10.4f} | {resultado:^15.6f}")
    except:
        print(f"{n_val:^10.4f} | {'Indefinido':^15}")

# ============================================================================
# TAREA 2: Evaluar directamente en n = 2
# ============================================================================
print("\n[TAREA 2] Evaluación directa en n = 2:")
print("-"*80)
numerador_en_2 = 2**3 - 8
denominador_en_2 = 2 - 2
print(f"Numerador: 2³ - 8 = {numerador_en_2}")
print(f"Denominador: 2 - 2 = {denominador_en_2}")
print(f"Resultado: {numerador_en_2}/{denominador_en_2} = 0/0")
print("\n⚠️  ¡FORMA INDETERMINADA 0/0!")
print("    Necesitamos usar técnicas algebraicas para resolver este límite.")

# ============================================================================
# TAREA 3: Factorización y simplificación
# ============================================================================
print("\n[TAREA 3] Factorización y cálculo del límite:")
print("-"*80)

# Usar SymPy
n = sp.Symbol('n')
numerador = n**3 - 8
denominador = n - 2

print("\n📐 Paso 1: Identificar la forma")
print("   n³ - 8 = n³ - 2³")
print("   Esta es una DIFERENCIA DE CUBOS")

print("\n📐 Paso 2: Aplicar la fórmula")
print("   Fórmula: a³ - b³ = (a - b)(a² + ab + b²)")
print("   Donde: a = n, b = 2")

print("\n📐 Paso 3: Factorizar")
print("   n³ - 2³ = (n - 2)(n² + n·2 + 2²)")
print("   n³ - 8 = (n - 2)(n² + 2n + 4)")

numerador_factorizado = sp.factor(numerador)
print(f"\n   Verificación con SymPy: {numerador_factorizado}")

print("\n📐 Paso 4: Simplificar la fracción")
print("   T(n) = (n - 2)(n² + 2n + 4)")
print("          ─────────────────────")
print("                (n - 2)")
print("\n   Cancelando (n - 2):")
print("   T(n) = n² + 2n + 4  (para n ≠ 2)")

print("\n📐 Paso 5: Calcular el límite")
print("   lim (n→2) T(n) = lim (n→2) (n² + 2n + 4)")
print("   lim (n→2) T(n) = 2² + 2(2) + 4")
print("   lim (n→2) T(n) = 4 + 4 + 4")
print("   lim (n→2) T(n) = 12")

# Verificar con SymPy
limite = sp.limit(numerador/denominador, n, 2)
print(f"\n   ✅ Verificación con SymPy: {limite}")

# ============================================================================
# TAREA 4: Graficar
# ============================================================================
print("\n[TAREA 4] Generando gráfica...")
print("-"*80)

# Crear valores para graficar (evitando n = 2)
n_vals = np.linspace(0, 5, 1000)
n_vals = n_vals[np.abs(n_vals - 2) > 0.01]
T_vals = (n_vals**3 - 8) / (n_vals - 2)

# Crear la figura con dos subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Vista general
ax1.plot(n_vals, T_vals, 'purple', linewidth=2, label='T(n) = (n³-8)/(n-2)')
ax1.plot(2, 12, 'ro', markersize=12, label=f'Límite en n=2: {limite}', zorder=5)
ax1.axvline(x=2, color='red', linestyle='--', alpha=0.5, linewidth=1.5, label='n = 2 (punto crítico)')
ax1.axhline(y=12, color='green', linestyle='--', alpha=0.3, linewidth=1.5)
ax1.grid(True, alpha=0.3)
ax1.set_xlabel('n (usuarios simultáneos)', fontsize=12, fontweight='bold')
ax1.set_ylabel('T(n) (tiempo de respuesta)', fontsize=12, fontweight='bold')
ax1.set_title('Tiempo de Respuesta - Vista General', fontsize=14, fontweight='bold')
ax1.legend(fontsize=10, loc='upper left')
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 35)

# Anotar el punto límite
ax1.annotate(f'lim = {limite}',
            xy=(2, 12),
            xytext=(2.7, 15),
            fontsize=11,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', color='red', lw=2))

# Subplot 2: Zoom cerca de n = 2
n_zoom = np.linspace(1.5, 2.5, 500)
n_zoom = n_zoom[np.abs(n_zoom - 2) > 0.001]
T_zoom = (n_zoom**3 - 8) / (n_zoom - 2)

ax2.plot(n_zoom, T_zoom, 'purple', linewidth=3, label='T(n)')
ax2.plot(2, 12, 'ro', markersize=15, label=f'lim T(n) = {limite}', zorder=5)
ax2.axvline(x=2, color='red', linestyle='--', alpha=0.5, linewidth=2)
ax2.axhline(y=12, color='green', linestyle='--', alpha=0.5, linewidth=2)
ax2.grid(True, alpha=0.3)
ax2.set_xlabel('n (usuarios simultáneos)', fontsize=12, fontweight='bold')
ax2.set_ylabel('T(n)', fontsize=12, fontweight='bold')
ax2.set_title('Zoom cerca de n = 2', fontsize=14, fontweight='bold')
ax2.legend(fontsize=11)
ax2.set_xlim(1.5, 2.5)
ax2.set_ylim(10, 14)

# Anotar valores cercanos
for n_test in [1.9, 2.1]:
    t_test = T(n_test)
    ax2.plot(n_test, t_test, 'go', markersize=8, zorder=4)
    ax2.text(n_test, t_test + 0.3, f'{t_test:.2f}',
            ha='center', fontsize=9,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7))

plt.tight_layout()
plt.savefig('problema3_tiempo_respuesta.png', dpi=150, bbox_inches='tight')
print("✅ Gráfica guardada como: problema3_tiempo_respuesta.png")
plt.show()

# ============================================================================
# TAREA 5: Interpretación
# ============================================================================
print("\n[TAREA 5] Interpretación del resultado:")
print("-"*80)
print(f"✓ El límite cuando n → 2 es {limite} unidades de tiempo.")
print()
print("✓ SIGNIFICADO PRÁCTICO:")
print("  - Aunque la función T(n) no está definida EXACTAMENTE con 2 usuarios,")
print("  - El tiempo de respuesta se aproxima a 12 unidades")
print("    cuando el número de usuarios se acerca a 2.")
print()
print("✓ CONCLUSIÓN:")
print("  - Con 2 usuarios simultáneos, el tiempo esperado es 12 unidades")
print("  - Este valor es importante para estimar el rendimiento de la aplicación")
print("  - Ayuda a planificar recursos y optimizar la experiencia del usuario")

print("\n" + "="*80)
print("✅ PROBLEMA 3 COMPLETADO")
print("="*80)
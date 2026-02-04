import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

print("="*80)
print("PROBLEMA 1: RENDIMIENTO DE UN SERVIDOR")
print("="*80)
print("\nFunción: R(t) = (t³ - 27)/(t - 3)")
print("Contexto: Cantidad de solicitudes que un servidor maneja por segundo")
print("\n" + "-"*80)

# Definir la función
def R(t):
    return (t**3 - 27) / (t - 3)

# ============================================================================
# TAREA 1: Calcular valores cercanos a t = 3
# ============================================================================
print("\n[TAREA 1] Calculando R(t) para valores cercanos a t = 3:")
print("-"*80)

valores_prueba = [2.9, 2.99, 2.999, 3.001, 3.01, 3.1]
print(f"{'t':^10} | {'R(t)':^15}")
print("-"*30)
for t_val in valores_prueba:
    try:
        resultado = R(t_val)
        print(f"{t_val:^10.4f} | {resultado:^15.6f}")
    except:
        print(f"{t_val:^10.4f} | {'Indefinido':^15}")

# ============================================================================
# TAREA 2: Evaluar directamente en t = 3
# ============================================================================
print("\n[TAREA 2] Evaluación directa en t = 3:")
print("-"*80)
numerador_en_3 = 3**3 - 27
denominador_en_3 = 3 - 3
print(f"Numerador: 3³ - 27 = {numerador_en_3}")
print(f"Denominador: 3 - 3 = {denominador_en_3}")
print(f"Resultado: {numerador_en_3}/{denominador_en_3} = 0/0")
print("\n⚠️  ¡FORMA INDETERMINADA 0/0!")
print("    Necesitamos usar técnicas algebraicas para resolver este límite.")

# ============================================================================
# TAREA 3: Factorización y simplificación
# ============================================================================
print("\n[TAREA 3] Factorización y cálculo del límite:")
print("-"*80)

# Usar SymPy para factorización simbólica
t = sp.Symbol('t')
numerador = t**3 - 27
denominador = t - 3

print("\n📐 Paso 1: Identificar la forma")
print("   t³ - 27 = t³ - 3³")
print("   Esta es una DIFERENCIA DE CUBOS")

print("\n📐 Paso 2: Aplicar la fórmula")
print("   Fórmula: a³ - b³ = (a - b)(a² + ab + b²)")
print("   Donde: a = t, b = 3")

print("\n📐 Paso 3: Factorizar")
print("   t³ - 3³ = (t - 3)(t² + t·3 + 3²)")
print("   t³ - 27 = (t - 3)(t² + 3t + 9)")

numerador_factorizado = sp.factor(numerador)
print(f"\n   Verificación con SymPy: {numerador_factorizado}")

print("\n📐 Paso 4: Simplificar la fracción")
print("   R(t) = (t - 3)(t² + 3t + 9)")
print("          ─────────────────────")
print("                (t - 3)")
print("\n   Cancelando (t - 3):")
print("   R(t) = t² + 3t + 9  (para t ≠ 3)")

print("\n📐 Paso 5: Calcular el límite")
print("   lim (t→3) R(t) = lim (t→3) (t² + 3t + 9)")
print("   lim (t→3) R(t) = 3² + 3(3) + 9")
print("   lim (t→3) R(t) = 9 + 9 + 9")
print("   lim (t→3) R(t) = 27")

# Verificar con SymPy
limite = sp.limit(numerador/denominador, t, 3)
print(f"\n   ✅ Verificación con SymPy: {limite}")

# ============================================================================
# TAREA 4: Graficar
# ============================================================================
print("\n[TAREA 4] Generando gráfica...")
print("-"*80)

# Crear valores para graficar (evitando t = 3)
t_vals = np.linspace(0, 6, 1000)
t_vals = t_vals[np.abs(t_vals - 3) > 0.01]  # Evitar exactamente t = 3
R_vals = (t_vals**3 - 27) / (t_vals - 3)

# Crear la figura con dos subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Vista general
ax1.plot(t_vals, R_vals, 'b-', linewidth=2, label='R(t) = (t³-27)/(t-3)')
ax1.plot(3, 27, 'ro', markersize=12, label=f'Límite en t=3: {limite}', zorder=5)
ax1.axvline(x=3, color='red', linestyle='--', alpha=0.5, linewidth=1.5, label='t = 3 (punto crítico)')
ax1.axhline(y=27, color='green', linestyle='--', alpha=0.3, linewidth=1.5)
ax1.grid(True, alpha=0.3)
ax1.set_xlabel('t (segundos)', fontsize=12, fontweight='bold')
ax1.set_ylabel('R(t) (solicitudes/segundo)', fontsize=12, fontweight='bold')
ax1.set_title('Rendimiento del Servidor - Vista General', fontsize=14, fontweight='bold')
ax1.legend(fontsize=10, loc='upper left')
ax1.set_xlim(0, 6)
ax1.set_ylim(0, 50)

# Anotar el punto límite
ax1.annotate(f'lim = {limite}',
            xy=(3, 27),
            xytext=(3.5, 30),
            fontsize=11,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', color='red', lw=2))

# Subplot 2: Zoom cerca de t = 3
t_zoom = np.linspace(2.5, 3.5, 500)
t_zoom = t_zoom[np.abs(t_zoom - 3) > 0.001]
R_zoom = (t_zoom**3 - 27) / (t_zoom - 3)

ax2.plot(t_zoom, R_zoom, 'b-', linewidth=3, label='R(t)')
ax2.plot(3, 27, 'ro', markersize=15, label=f'lim R(t) = {limite}', zorder=5)
ax2.axvline(x=3, color='red', linestyle='--', alpha=0.5, linewidth=2)
ax2.axhline(y=27, color='green', linestyle='--', alpha=0.5, linewidth=2)
ax2.grid(True, alpha=0.3)
ax2.set_xlabel('t (segundos)', fontsize=12, fontweight='bold')
ax2.set_ylabel('R(t)', fontsize=12, fontweight='bold')
ax2.set_title('Zoom cerca de t = 3', fontsize=14, fontweight='bold')
ax2.legend(fontsize=11)
ax2.set_xlim(2.5, 3.5)
ax2.set_ylim(24, 30)

# Anotar valores cercanos
for t_test in [2.9, 3.1]:
    r_test = R(t_test)
    ax2.plot(t_test, r_test, 'go', markersize=8, zorder=4)
    ax2.text(t_test, r_test - 0.5, f'{r_test:.2f}',
            ha='center', fontsize=9,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7))

plt.tight_layout()
plt.savefig('problema1_servidor.png', dpi=150, bbox_inches='tight')
print("✅ Gráfica guardada como: problema1_servidor.png")
plt.show()

# ============================================================================
# TAREA 5: Interpretación
# ============================================================================
print("\n[TAREA 5] Interpretación del resultado:")
print("-"*80)
print(f"✓ El límite cuando t → 3 es {limite} solicitudes por segundo.")
print()
print("✓ SIGNIFICADO PRÁCTICO:")
print("  - Aunque la función R(t) no está definida EXACTAMENTE en t = 3,")
print("  - El servidor se acerca a manejar 27 solicitudes/segundo")
print("    cuando el tiempo se aproxima a 3 segundos.")
print()
print("✓ CONCLUSIÓN:")
print("  - En t = 3 segundos, el rendimiento esperado del servidor es 27 req/s")
print("  - Este valor representa la 'tendencia' del sistema en ese instante")
print("  - Es útil para planificación de capacidad y escalamiento")

print("\n" + "="*80)
print("✅ PROBLEMA 1 COMPLETADO")
print("="*80)
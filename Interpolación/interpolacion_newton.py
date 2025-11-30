import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# 1. Definir los puntos del ejercicio
x = np.array([-1, 0, 1, 2, 3, 4])
y = np.array([3, 0, 4, 0, 1, 0])

# 2. Calcular Diferencias Divididas (Metodología del Libro)
n = len(x)
coef = np.zeros([n, n])
coef[:, 0] = y

for j in range(1, n):
    for i in range(n - j):
        coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

newton_coeffs = coef[0, :]

print("-" * 30)
print("Coeficientes de Newton (Diagonal Superior):")
print(newton_coeffs)
print("-" * 30)

# 3. Expandir para obtener la forma estándar (a_i)
# P(x) = b0 + b1(x-x0) + b2(x-x0)(x-x1) ...
P_standard = Polynomial([0])  # Polinomio acumulador
termino = Polynomial([1])  # Término (x-x0)...

for i in range(n):
    # Sumamos el término actual: b_i * (x-x0)...(x-xi_minus_1)
    P_standard = P_standard + newton_coeffs[i] * termino

    # Preparamos el siguiente término multiplicando por (x - x_i)
    # Polynomial([-x[i], 1]) crea el polinomio (1*x - x[i])
    termino = termino * Polynomial([-x[i], 1])

print("Coeficientes a_i del polinomio estándar:")
print("(Orden: a0, a1, a2 ... a5)")
coeffs = P_standard.coef
for i, a in enumerate(coeffs):
    print(f"a_{i} = {a:.4f}")
print("-" * 30)

# 4. Gráfica de comprobación
x_plot = np.linspace(-1.5, 4.5, 200)
y_plot = P_standard(x_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, label="Polinomio P(x)", color="blue")
plt.plot(x, y, "ro", label="Puntos Dato", markersize=8)
plt.title("Ejercicio 3: Interpolación de Newton")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

# Verificar valores en los puntos
print("Verificación de valores P(x) en los puntos dados:")
for xi, yi in zip(x, y):
    val = P_standard(xi)
    print(f"P({xi}) = {val:.4f} (Esperado: {yi})")

plt.show()

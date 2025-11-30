import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# 1. Datos
x = np.array([0, 1, 3, 4])
y = np.array([1, 2, 0, 4])

# 2. Crear el polinomio de Lagrange
polinomio = lagrange(x, y)

print("El polinomio es:")
print(polinomio)  # Te muestra los coeficientes

# 3. Verificación (Inciso b)
print("\nVerificación en los puntos originales:")
for xi, yi in zip(x, y):
    print(f"P({xi}) = {polinomio(xi)} (Esperado: {yi})")

# 4. Interpolación (Inciso c)
resultado = polinomio(3.5)
print(f"\nEl valor interpolado en f(3.5) es: {resultado}")

# 5. Gráfica
x_graf = np.linspace(-1, 5, 100)
plt.plot(x_graf, polinomio(x_graf), label="Polinomio Lagrange")
plt.plot(x, y, "ro", label="Puntos datos")
plt.plot(3.5, resultado, "go", label=f"f(3.5)={resultado:.4f}")
plt.grid(True)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Definir los Datos ---
x = np.array([0.0, 1.0, 2.0])  # Puntos x
y = np.array([0.0, 1.0, 8.0])  # Puntos y
n = len(x)

# --- 2. Preparar la Mesa (Deltas) ---
# delta_x (anchos h_i) y Diferencias Divididas (Delta_i)
delta_x = np.diff(x)  # [1.0, 1.0]
delta_y = np.diff(y) / delta_x  # [1.0, 7.0]

# --- 3. Armar el Sistema Matricial A * c = r ---
A = np.zeros((n, n))
r = np.zeros(n)

# Condiciones de Spline Natural (Bordes)
A[0, 0] = 1.0  # c1 = 0
A[-1, -1] = 1.0  # cn = 0

# Llenar las filas internas (tridiagonal)
# En este caso solo hay una fila interna (i=1 para el punto x=1)
for i in range(1, n - 1):
    # La fila del medio de la "receta"
    A[i, i - 1] = delta_x[i - 1]  # Izquierda
    A[i, i] = 2 * (delta_x[i - 1] + delta_x[i])  # Centro (2 * suma deltas)
    A[i, i + 1] = delta_x[i]  # Derecha

    # El lado derecho de la ecuación
    r[i] = 3 * (delta_y[i] - delta_y[i - 1])

# --- 4. Resolver el Sistema ---
# Esto nos da el vector [c1, c2, c3]
c = np.linalg.solve(A, r)

print("Curvaturas (c):", c)  # Debería dar [0.  4.5  0.]

# --- 5. Calcular coeficientes b y d ---
# a ya lo tenemos (es y)
b = np.zeros(n - 1)
d = np.zeros(n - 1)
a = y[0 : n - 1]

for i in range(n - 1):
    d[i] = (c[i + 1] - c[i]) / (3 * delta_x[i])
    b[i] = delta_y[i] - (delta_x[i] / 3) * (2 * c[i] + c[i + 1])

# Imprimir los polinomios para verificar
print("\nPolinomios resultantes:")
for i in range(n - 1):
    print(f"Tramo {i + 1} [{x[i]} a {x[i + 1]}]:")
    print(
        f" S(x) = {a[i]:.2f} + {b[i]:.2f}(x-{x[i]}) + {c[i]:.2f}(x-{x[i]})^2 + {d[i]:.2f}(x-{x[i]})^3"
    )

# --- 6. Graficar ---
plt.figure(figsize=(8, 6))

# Puntos originales
plt.plot(x, y, "ro", markersize=10, label="Datos Originales")

# Graficar cada tramo
colors = ["blue", "green"]
for i in range(n - 1):
    # Generar puntos finos para que se vea curva suave
    x_fino = np.linspace(x[i], x[i + 1], 100)
    # Evaluar polinomio: a + b(diff) + c(diff)^2 + d(diff)^3
    diff = x_fino - x[i]
    y_fino = a[i] + b[i] * diff + c[i] * diff**2 + d[i] * diff**3

    plt.plot(
        x_fino, y_fino, color=colors[i], linewidth=2, label=f"Spline Tramo {i + 1}"
    )

plt.title("Ejercicio 7: Trazador Cúbico Natural (Python)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

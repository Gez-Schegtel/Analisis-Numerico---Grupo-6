import sympy as sp
import matplotlib.pyplot as plt
import numpy as np


def resolver_newton_ejercicio_3():
    # --- 1. DATOS DEL EJERCICIO 3 ---
    # Puntos: (-1,3), (0,0), (1,4), (2,0), (3,1), (4,0)
    x_input = [-1, 0, 1, 2, 3, 4]
    y_input = [3, 0, 4, 0, 1, 0]

    # Convertimos a SymPy para que las fracciones sean exactas
    x = [sp.sympify(val) for val in x_input]
    y = [sp.sympify(val) for val in y_input]
    n = len(x)

    print(f"Calculando polinomio interpolante para {n} puntos...")
    print("-" * 50)

    # --- 2. TABLA DE DIFERENCIAS DIVIDIDAS ---
    # Creamos una matriz n x n llena de ceros
    # coef[i][j] guardará la diferencia dividida
    coef = [[sp.Integer(0)] * n for _ in range(n)]

    # La primera columna son los valores de y
    for i in range(n):
        coef[i][0] = y[i]

    # Algoritmo de Diferencias Divididas
    # F[x_i, ..., x_{i+j}] = (F[x_{i+1}...x_{i+j}] - F[x_i...x_{i+j-1}]) / (x_{i+j} - x_i)
    for j in range(1, n):
        for i in range(n - j):
            numerador = coef[i + 1][j - 1] - coef[i][j - 1]
            denominador = x[i + j] - x[i]
            coef[i][j] = numerador / denominador

    # Los coeficientes b_i de Newton son la primera fila de la tabla
    b = coef[0]

    print("Coeficientes de la forma de Newton (b_i):")
    sp.pprint(b)
    print("-" * 50)

    # --- 3. CONSTRUCCIÓN DEL POLINOMIO ---
    x_sym = sp.symbols("x")
    P = 0

    # P(x) = b0 + b1(x-x0) + b2(x-x0)(x-x1) + ...
    for i in range(n):
        termino = b[i]
        for k in range(i):
            termino *= x_sym - x[k]
        P += termino

    # --- 4. EXPANDIR PARA HALLAR LOS COEFICIENTES a_i ---
    # El ejercicio pide a5*x^5 + ... + a0
    P_expandido = sp.expand(P)

    print("POLINOMIO FINAL EXPANDIDO P(x):")
    sp.pprint(P_expandido)
    print("-" * 50)

    # Extraer los coeficientes ordenados
    # Poly devuelve [a5, a4, a3, a2, a1, a0]
    coeffs_finales = sp.Poly(P_expandido, x_sym).all_coeffs()

    print("RESPUESTA FINAL (Coeficientes a_i):")
    nombres = ["a5", "a4", "a3", "a2", "a1", "a0"]
    for nombre, valor in zip(nombres, coeffs_finales):
        print(f"{nombre} = {valor}")

    # --- 5. GRÁFICA PARA COMPROBAR ---
    f_num = sp.lambdify(x_sym, P_expandido, "numpy")

    # Rango de graficación un poco más amplio que los puntos
    x_grid = np.linspace(min(x_input) - 0.5, max(x_input) + 0.5, 200)
    y_grid = f_num(x_grid)

    plt.figure(figsize=(8, 6))
    plt.plot(x_grid, y_grid, "b-", label="Polinomio P(x)")
    plt.plot(x_input, y_input, "ro", markersize=8, label="Datos")
    plt.title(f"Ejercicio 3: Interpolación de Newton (Grado {n - 1})")
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    resolver_newton_ejercicio_3()

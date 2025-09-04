# %% [markdown]
"""
# Practica N° 1: Números complejos
## Análisis Numérico

### Objetivos
- Aplicar conceptos de números complejos mediante su implementación en Python.
- Desarrollar habilidades en la representación, operaciones y transformaciones de números complejos usando herramientas computacionales.
- Familiarizarse con el uso de librerías estándar de Python como `cmath`, `matplotlib` y `numpy`.

**Tipo de actividad:** grupal.

### Formato de entrega:
1. Resolvé las actividades propuestas utilizando un cuaderno Jupyter.
2. Asegurate de comentar el código con explicaciones claras que permitan comprender cada paso de la resolución.
3. Una vez finalizada la práctica, deberán crear un documento complementario que incluya:
    a. Nombre de la actividad.
    b. Datos completos del grupo (nombres y apellidos de los integrantes).
    c. Enlace al cuaderno compartido (asegurarse de que el acceso esté habilitado).
4. Subí el documento complementario en la tarea "Práctica N.º 1: Números complejos" disponible en el aula virtual.
"""

# %% [markdown]
"""
### Consideraciones iniciales:

* Los números complejos en Python se representan con una `j` para la parte imaginaria.
    * Ejemplo: `3+2j`; `22-3j`; `9j`, etc.
* Para seguir con las buenas prácticas de la programación en Python, importamos todas las librerías a utilizar al principio del documento.
"""

# %%
# Importación de librerías.
import cmath
import numpy as np
import matplotlib.pyplot as plt

# Configuración para que los gráficos de Matplotlib se vean mejor
plt.style.use("seaborn-v0_8-whitegrid")


# %%
def entrada_complejo() -> complex:
    # ~~~ Esta función devuelve un número complejo a partir del input del usuario. ~~~ #
    while True:
        try:
            numero_complejo = complex(
                input(
                    "Ingresá un número complejo para su análisis, con una letra j al final para indicar la parte imaginaria: "
                ).replace(" ", "")
            )
            break
        except ValueError:
            print(
                "El formato de entrada no es válido. El la forma aceptada para los números complejos es del tipo <a + bj>."
            )
    return numero_complejo


# %% [markdown]
"""
### Actividad 1
**Representación binómica y partes de un complejo**

Escribir un programa que, dado un número complejo z = a + bi, muestre:
- Parte real.
- Parte imaginaria.
- Representación binómica.
"""

# %%
z = entrada_complejo()

## Extraemos la parte real del número complejo:
parte_real = z.real

## Extraemos la parte imaginaria del número complejo:
parte_imaginaria = z.imag

print(f"La parte real del número {z} es {parte_real}")
print(f"La parte imaginaria del número {z} es {parte_imaginaria}j")

if parte_imaginaria >= 0:
    print(
        f"Representación binómica del número complejo: {parte_real} + {parte_imaginaria}j"
    )
else:
    print(
        f"Representación binómica del número complejo: {parte_real} - {abs(parte_imaginaria)}j"
    )

# %% [markdown]
"""
### Actividad 2
**Operaciones básicas**

Crear una función que reciba dos números complejos y devuelva:
- Suma
- Resta
- Producto
- Cociente

Mostrar los resultados en consola con formato a + bi.
"""

# %%
z1 = entrada_complejo()
z2 = entrada_complejo()

print(f"{z1} + {z2} = {z1 + z2}")
print(f"{z1} - {z2} = {z1 - z2}")
print(f"{z1} * {z2} = {z1 * z2}")
print(f"{z1} / {z2} = {z1 / z2}")

# %% [markdown]
"""
### Actividad 3
**Potencias de i**

Construir una función que calcule 𝑖^𝑛 para un valor entero n ingresado por el usuario. Mostrar el resultado simplificado.
"""

# %%
i = 1j
n = int(input("Ingrese la potencia a la que quiere elevar el número imaginario i."))

potencia_i = i**n
if potencia_i.real != 0:
    print(int(potencia_i.real))
else:
    print(str(int(potencia_i.imag)).replace("1", "j"))

# %% [markdown]
"""
### Actividad 4
**Módulo y conjugado**

Dado un número complejo z, calcular:
- Su módulo.
- Su conjugado.
- Verificar que `z * z̄ = |z|²`.
"""

# %%
z = entrada_complejo()
modulo_z = abs(z)
conjugado_z = z.conjugate()

print(f"Módulo de {z} = |{z}| = {modulo_z}")
print(f"Conjugado de {z}: {conjugado_z}")
print(f"Verificamos la propiedad z * z̄ = |z|²: {z * conjugado_z} = {modulo_z**2}")

# %% [markdown]
"""
### Actividad 5
**División entre números complejos**

Implementar una función que divida dos números complejos sin usar el operador '/', utilizando la fórmula de conjugado y módulo.

**Recordá que la fórmula para la división es la siguiente:**

$$ \frac{z}{w} = zw^{-1} = z \frac{\bar{w}}{|w|^2} $$
"""

# %%
z = entrada_complejo()
w = entrada_complejo()

conjugado_w = w.conjugate()

division_formula = z * conjugado_w / abs(w) ** 2

print(f""""División con la fórmula "tradicional": {division_formula}""")
print(f"""División utilizando el operador "/": {z / w}""")


# %% [markdown]
"""
### Actividad 6
**Forma polar y trigonométrica**

Para un número complejo dado:
- Calcular su módulo.
- Calcular su argumento (en radianes y grados).
- Escribir su forma trigonométrica.

**Recordar que la forma trigonométrica es la siguiente:**

$$ z = r(\cos \theta + i \sin \theta) $$
"""

# %%
## Opción 1: Calculamos el módulo y el argumento del número complejo con una sola función, al mismo tiempo.
z = entrada_complejo()

# Esta función de math nos devuelve una tupla con el módulo y el argumento. Equivalente a (abs(z), phase(z))
mod, ang_rad = cmath.polar(z)

ang_deg = np.degrees(ang_rad)

print(
    f"El número complejo en su forma trigonométrica es: {mod} * (cos({ang_deg:.4f}.) + i * sen({ang_deg:.4f}))"
)

# %%
## Opción 2: Calculamos el módulo y el argumento por separado.
z = entrada_complejo()

mod = abs(z)
ang_rad = cmath.phase(z)  # Al argumento se lo conoce también como fase.
ang_deg = np.degrees(ang_rad)

print(
    f"El número complejo en su forma trigonométrica es: {mod} * (cos({ang_deg:.4f}) + i * sen({ang_deg:.4f}))"
)

# %% [markdown]
"""
### Actividad 7
**Representación grafica**

De la guía de ejercicios prácticos realice el punto 6:

> 6. Sean $z_1 = 4 - 3i$ y $z_2 = -1 + 2i$. Obtenga gráfica y analíticamente.
>    
>    a) $|z_1 + z_2|$,
>    
>    b) $|z_1 - z_2|$,
>    
>    c) $\bar{z}_1 - \bar{z}_2$ y
>    
>    d) $|2\bar{z}_1 - 3\bar{z}_2 - 2|$.

* Realice las operaciones de forma manual y el procedimiento utilizando un cuaderno Jupyter.
* Realice la gráfica de los números con el resultado de la operación, dar formato a los ejes e indicar con los títulos la referencia a los ejercicios.

> Para facilitar la lectura del código, vamos a definir primero la función que nos permite realizar los gráficos para los distintos puntos. También se definen los números del enunciado.
"""

# %%
# ~~~ Definición de los números complejos iniciales ~~~ #
z1 = 4 - 3j
z2 = -1 + 2j

print(f"Número z1: {z1}")
print(f"Número z2: {z2}")


# ~~~ Función auxiliar para graficar ~~~ #
def graficar_complejos(complejos: dict, titulo: str, vectores_origen_cero=True):
    """
    Grafica una colección de números complejos como vectores en el plano.

    Args:
        complejos (dict): Diccionario {etiqueta: número_complejo}.
        titulo (str): Título del gráfico.
        vectores_origen_cero (bool): Si es True, todos los vectores parten de (0,0).
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    max_val = 0

    # Dibuja cada vector y su etiqueta
    for label, z in complejos.items():
        ax.arrow(
            0,
            0,
            z.real,
            z.imag,
            head_width=0.2,
            head_length=0.3,
            fc="blue",
            ec="blue",
            label=label,
        )
        ax.text(
            z.real * 1.1,
            z.imag * 1.15,
            f"{label} = ({z.real:.1f}, {z.imag:.1f}i)",
            fontsize=12,
        )
        max_val = max(max_val, abs(z.real), abs(z.imag))

    # Formato del gráfico
    ax.set_title(titulo, fontsize=16)
    ax.set_xlabel("Eje Real", fontsize=12)
    ax.set_ylabel("Eje Imaginario", fontsize=12)
    ax.axhline(0, color="grey", lw=1)
    ax.axvline(0, color="grey", lw=1)
    ax.grid(True, linestyle="--", alpha=0.6)

    # Asegurar que el gráfico sea cuadrado y centrado
    limit = max_val + 2
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_aspect("equal", adjustable="box")

    plt.show()


# %% [markdown]
"""
**a) $|z_1 + z_2|$**

**Resolución Analítica (Manual y con Python):**

1.  **Suma de los complejos:**
    $z_1 + z_2 = (4 - 3i) + (-1 + 2i)$
    $z_1 + z_2 = (4 - 1) + (-3 + 2)i$
    $z_1 + z_2 = 3 - 1i$

2.  **Cálculo del módulo:**
    $|z_1 + z_2| = |3 - i| = \sqrt{3^2 + (-1)^2}$
    $|z_1 + z_2| = \sqrt{9 + 1} = \sqrt{10}$

Ahora, realizamos el mismo cálculo con Python.
"""

# %%
# 1. Sumar los números complejos
z_suma = z1 + z2

# 2. Calcular el módulo del resultado
modulo_suma = abs(z_suma)

print(f"Paso 1: z1 + z2 = ({z1}) + ({z2}) = {z_suma}")
print(f"Paso 2: |{z_suma}| = {modulo_suma:.4f}")
print(f"El valor de sqrt(10) es: {np.sqrt(10):.4f}")

# %% [markdown]
"""
**Representación Gráfica:**

La suma de dos vectores complejos puede visualizarse con la "regla del paralelogramo". El vector resultante `z_suma` es la diagonal del paralelogramo formado por `z1` y `z2`.

"""

# %%
# Diccionario de complejos a graficar
a_graficar = {"z1": z1, "z2": z2, "z1 + z2": z_suma}

graficar_complejos(a_graficar, titulo="a) Suma: |z1 + z2|")

# %% [markdown]
"""
**b) $|z_1 - z_2|$**

**Resolución Analítica (Manual y con Python):**

1.  **Resta de los complejos:**
    $z_1 - z_2 = (4 - 3i) - (-1 + 2i)$
    $z_1 - z_2 = (4 - (-1)) + (-3 - 2)i$
    $z_1 - z_2 = 5 - 5i$

2.  **Cálculo del módulo:**
    $|z_1 - z_2| = |5 - 5i| = \sqrt{5^2 + (-5)^2}$
    $|z_1 - z_2| = \sqrt{25 + 25} = \sqrt{50} = 5\sqrt{2}$

Ahora, con Python:

"""

# %%
# 1. Restar los números complejos
z_resta = z1 - z2

# 2. Calcular el módulo del resultado
modulo_resta = abs(z_resta)

print(f"Paso 1: z1 - z2 = ({z1}) - ({z2}) = {z_resta}")
print(f"Paso 2: |{z_resta}| = {modulo_resta:.4f}")
print(f"El valor de 5*sqrt(2) es: {5 * np.sqrt(2):.4f}")

# %% [markdown]
"""
**Representación Gráfica:**

La resta $z_1 - z_2$ es equivalente a la suma $z_1 + (-z_2)$. El vector resultante `z_resta` puede verse como la diagonal del paralelogramo formado por `z1` y `-z2`. Gráficamente, el vector `z1 - z2` es el vector que une la punta de `z2` con la punta de `z1`.
"""

# %%
# Diccionario de complejos a graficar
b_graficar = {"z1": z1, "z2": z2, "z1 - z2": z_resta}

graficar_complejos(b_graficar, titulo="b) Resta: |z1 - z2|")

# %% [markdown]
"""
**c) $\bar{z}_1 - \bar{z}_2$**

**Resolución Analítica (Manual y con Python):**

1.  **Calcular los conjugados:**
    $\bar{z}_1 = \overline{4 - 3i} = 4 + 3i$
    $\bar{z}_2 = \overline{-1 + 2i} = -1 - 2i$

2.  **Restar los conjugados:**
    $\bar{z}_1 - \bar{z}_2 = (4 + 3i) - (-1 - 2i)$
    $\bar{z}_1 - \bar{z}_2 = (4 - (-1)) + (3 - (-2))i$
    $\bar{z}_1 - \bar{z}_2 = 5 + 5i$

Ahora, con Python:
"""

# %%
# 1. Calcular los conjugados
z1_conj = z1.conjugate()
z2_conj = z2.conjugate()

# 2. Restar los conjugados
resultado_c = z1_conj - z2_conj

print(f"Paso 1: z1_conj = {z1_conj}, z2_conj = {z2_conj}")
print(f"Paso 2: z1_conj - z2_conj = ({z1_conj}) - ({z2_conj}) = {resultado_c}")

# %% [markdown]
"""
**Representación Gráfica:**

Graficamos los vectores de los conjugados, $\bar{z}_1$ y $\bar{z}_2$, y el vector resultante de su resta. El conjugado de un número es su reflejo a través del eje real.


"""

# %%
# Diccionario de complejos a graficar
c_graficar = {"z1_conj": z1_conj, "z2_conj": z2_conj, "resultado": resultado_c}

graficar_complejos(c_graficar, titulo="c) Resta de Conjugados")

# %% [markdown]
"""

**d) $|2\bar{z}_1 - 3\bar{z}_2 - 2|$**

**Resolución Analítica (Manual y con Python):**

1.  **Calcular los conjugados y múltiplos:**
    $2\bar{z}_1 = 2(4 + 3i) = 8 + 6i$
    $3\bar{z}_2 = 3(-1 - 2i) = -3 - 6i$

2.  **Realizar la operación completa:**
    $2\bar{z}_1 - 3\bar{z}_2 - 2 = (8 + 6i) - (-3 - 6i) - 2$
    $= (8 - (-3) - 2) + (6 - (-6))i$
    $= (8 + 3 - 2) + (6 + 6)i$
    $= 9 + 12i$

3.  **Calcular el módulo:**
    $|9 + 12i| = \sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15$

Ahora, con Python:

"""

# %%
# Los conjugados z1_conj y z2_conj ya fueron calculados.

# 1. Realizar la operación completa
resultado_d = 2 * z1_conj - 3 * z2_conj - 2

# 2. Calcular el módulo
modulo_d = abs(resultado_d)

print(f"Paso 1: 2*z1_conj = {2 * z1_conj}")
print(f"Paso 2: 3*z2_conj = {3 * z2_conj}")
print(f"Paso 3: (2*z1_conj) - (3*z2_conj) - 2 = {resultado_d}")
print(f"Paso 4: |{resultado_d}| = {modulo_d}")

# %% [markdown]
"""
**Representación Gráfica:**

Para visualizar esta operación, graficaremos los vectores intermedios ($2\bar{z}_1$ y $-3\bar{z}_2 - 2$) y el vector resultante final.

"""

# %%
# Vectores intermedios
v1 = 2 * z1_conj
v2 = -3 * z2_conj - 2
resultado_d = v1 + v2

# Diccionario de complejos a graficar
d_graficar = {"2*z1_conj": v1, "-3*z2_conj - 2": v2, "Resultado": resultado_d}

graficar_complejos(d_graficar, titulo="d) Operación Combinada")


# %% [markdown]
"""
### Actividad 8
**Potencia en forma polar**

Implementar el teorema de De Moivre para calcular 𝑧 𝑛 usando la forma polar del número complejo.
"""

# %% [markdown]
"""
### Actividad 9
**Raíces n-ésimas de un número complejo**

Dado un número complejo z y un entero n, calcular las n raíces de z y graficarlas en el plano complejo.
"""

# %% [markdown]
"""
### Actividad 10
**Sistemas de ecuaciones**

Resolver los sistemas de ecuaciones del punto 16 y realizar la comprobación en un cuaderno Jupyter.
"""

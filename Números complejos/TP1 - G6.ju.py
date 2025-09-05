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

### Consideraciones iniciales:

* Los números complejos en Python se representan con una `j` para la parte imaginaria.
    * Ejemplo: `3+2j`; `22-3j`; `9j`, etc.
* Para seguir con las buenas prácticas de la programación en Python, importamos todas las librerías a utilizar al principio del documento.
"""

# %%
# Importación de librerías.
import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Configuración para que los gráficos de Matplotlib se vean mejor
plt.style.use("seaborn-v0_8-whitegrid")


# La siguiente función se definió para permitir la entrada de datos del usuario.
# Se conserva por si se quiere cambiar el comportamiento del notebook a uno interactivo en el futuro,
# pero no se utilizará en la versión actual para garantizar la reproducibilidad del documento.
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

def complejo_forma_binomica(z: complex) -> str:
    parte_real = z.real
    parte_imaginaria = z.imag

    if parte_imaginaria >= 0:
        return f"{parte_real:.2f} + {parte_imaginaria:.2f}i"
    else:
        return f"{parte_real:.2f} - {abs(parte_imaginaria):.2f}i"


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
# Se define un valor fijo para el número complejo en lugar de pedirlo al usuario.
z = 3 + 4j

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
# Se definen valores fijos para los números complejos.
z1 = 5 - 2j
z2 = -3 + 4j

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
# Se define un valor fijo para la potencia n.
n = 3

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
# Se define un valor fijo para el número complejo.
z = -4 - 3j
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
# Se definen valores fijos para los números complejos.
z = 10 + 5j
w = 1 + 2j

conjugado_w = w.conjugate()

division_formula = z * conjugado_w / abs(w) ** 2

print(f""""División con la fórmula "tradicional": {division_formula:.2f}""")
print(f"""División utilizando el operador "/": {(z / w):.2f}""")

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
# Se define un valor fijo para el número complejo.
z = -1 + 1j

# Esta función de math nos devuelve una tupla con el módulo y el argumento. Equivalente a (abs(z), phase(z))
mod, ang_rad = cmath.polar(z)

ang_deg = np.degrees(ang_rad)

print(
    f"El número complejo en su forma trigonométrica es: {mod:.4f} * (cos({ang_deg:.4f}.) + i * sen({ang_deg:.4f}))"
)

## Opción 2: Calculamos el módulo y el argumento por separado.
# Se usa el mismo valor fijo para demostrar que el resultado es idéntico.
z = -1 + 1j

mod = abs(z)
ang_rad = cmath.phase(z)  # Al argumento se lo conoce también como fase.
ang_deg = np.degrees(ang_rad)

print(
    f"El número complejo en su forma trigonométrica es: {mod:.4f} * (cos({ang_deg:.4f}) + i * sen({ang_deg:.4f}))"
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

Implementar el teorema de De Moivre para calcular 𝑧^𝑛 usando la forma polar del número complejo.

**Recordá que el teorema de Moivre enuncia lo siguiente:**

$$ z^n = [r(\cos \theta + i \sin \theta)]^n = r^n(\cos(n\theta) + i \sin(n\theta)) $$
$$ z^n = \underbrace{r^n \cos(n\theta)}_{\text{Parte Real (a)}} + i \underbrace{(r^n \sin(n\theta))}_{\text{Parte Imaginaria (b)}} $$
... donde $r = |z|$ es el módulo de $z$.
"""


# %%
## Opción 1: Utlizando la librería math.
def mostrar_binomico(a, b):
    """Devuelve un complejo en formato a + bi"""
    if b >= 0:
        return f"{a:.3f} + {b:.3f}i"
    else:
        return f"{a:.3f} - {abs(b):.3f}i"


# Programa principal
# Se definen valores fijos para z y n.
z = 1 + 1j
n = 5

# Paso 1: convertir a forma polar
r = abs(z)  # módulo
theta = math.atan2(z.imag, z.real)  # argumento en radianes

# Paso 2: aplicar De Moivre
r_n = r**n
theta_n = n * theta

# Paso 3: volver a forma binómica
resultado_real = r_n * math.cos(theta_n)
resultado_imag = r_n * math.sin(theta_n)

# Mostrar resultados
print(f"\nNúmero en forma polar: r = {r:.3f}, θ = {theta:.3f} rad")
print(f"Aplicando De Moivre: z^{n} = {r:.2f}^{n} (cos({n}*θ) + i·sin({n}*θ))")
print(f"Resultado en binómica: {mostrar_binomico(resultado_real, resultado_imag)}")

# %%
## Opción 2: Utilizamos únicamente las funciones de cmath.
# Se usan los mismos valores fijos para z y n para consistencia.
z = 1 + 1j
n = 5

# Paso 1: Convertir el número a forma polar.
r, theta = cmath.polar(z)

# Paso 2: Aplicamos el teorema de Moivre.
r_n = r**n
theta_n = theta * n

moivre = cmath.rect(r_n, theta_n) # Esta función toma el módulo de z y el valor de theta, y devuelve el número complejo en forma binómica.

"""
Usar la función rect es lo mismo que hacer lo siguiente: 

parte_real = r_n * math.cos(theta_n)
parte_imaginaria = r_n * math.sin(theta_n)
resultado = complex(parte_real, parte_imaginaria)
"""

print(f"Teorema de Moivre: z^{n} = {r:.2f} ^ {n}(cos({n}*{theta:.2f}) + i*sin({n}*{theta:.2f}))")
print(f"Comprobación: {z**n} = {complejo_forma_binomica(moivre)}")


# %% [markdown]
"""
### Actividad 9
**Raíces n-ésimas de un número complejo**

Dado un número complejo z y un entero n, calcular las n raíces de z y graficarlas en el plano complejo.
"""


# %%
# Se definen valores fijos para z y n.
z = 8j
n = 3

# Paso 1: convertir a forma polar
r, theta = cmath.polar(z)

# Paso 2: calcular raíces
raices = list()
for k in range(n):
    r_n = r ** (1 / n)
    angle = (theta + 2 * math.pi * k) / n
    raiz = cmath.rect(r_n, angle)
    raices.append(raiz)
    print(f"Raíz {k + 1}: {complejo_forma_binomica(raiz)}")

# Paso 3: graficar en el plano complejo
plt.figure(figsize=(8, 8)) # Crear una figura de tamaño adecuado
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.5)

for raiz in raices:
    plt.plot(
        raiz.real, raiz.imag, "o", markersize=8, label=f"{complejo_forma_binomica(raiz)}"
    )

plt.title(f"Raíces {n}-ésimas de {z}")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginaria")
plt.legend()
plt.axis("equal")
plt.show()

# %% [markdown]
"""
### Actividad 10
**Sistemas de ecuaciones**

Resolver los sistemas de ecuaciones del punto 16 y realizar la comprobación en un cuaderno Jupyter.
"""

# %%
# ~~~ Definición de las variables simbólicas ~~~
# Esta línea le dice a SymPy que trate 'z', 'w', 'x', e 'y' no como
# variables de Python que guardan un valor, sino como símbolos matemáticos
# abstractos. Son las incógnitas de nuestros sistemas de ecuaciones.
z, w, x, y = sp.symbols("z w x y")

# ==============================
# Sistema a)
# z + w = 2 - 3i
# z - w = -3 + i
# ==============================

# ~~~ Creación de la lista de ecuaciones para el sistema a) ~~~
# eqs_a es una lista de Python que contendrá las dos ecuaciones del sistema.
# sp.solve() necesita esta lista para saber qué resolver.
eqs_a = [
    # ~~~ Definición de la primera ecuación ~~~
    # sp.Eq() crea un objeto de igualdad simbólica. Representa matemáticamente
    # la ecuación "lado_izquierdo = lado_derecho".
    # El primer argumento (z + w) es el lado izquierdo.
    # El segundo argumento (2 - 3 * sp.I) es el lado derecho.
    # Nota el uso de sp.I para la unidad imaginaria.
    sp.Eq(z + w, 2 - 3 * sp.I),

    # ~~~ Definición de la segunda ecuación ~~~
    # Se crea el objeto para la segunda ecuación del sistema, z - w = -3 + i.
    sp.Eq(z - w, -3 + sp.I),
]

# ~~~ Resolución del sistema a) ~~~
# sp.solve() es la función principal que resuelve sistemas de ecuaciones.
# - El primer argumento, `eqs_a`, es la lista de ecuaciones que debe satisfacer.
# - El segundo argumento, `(z, w)`, es una tupla con los símbolos que queremos despejar.
# SymPy aplicará métodos algebraicos (como sustitución o eliminación) para encontrar los valores.
sol_a = sp.solve(eqs_a, (z, w))

# ~~~ Impresión de la solución ~~~
# sp.solve devuelve un diccionario donde las claves son los símbolos (z, w)
# y los valores son sus soluciones.
print("a) Solución:", sol_a)


# ==============================
# Sistema b)
# z + 3w = 1 + 2i
# i*z + w = 2 - i
# ==============================

# ~~~ Creación de la lista de ecuaciones para el sistema b) ~~~
# De nuevo, una lista para almacenar las ecuaciones del segundo sistema.
eqs_b = [
    # ~~~ Primera ecuación del sistema b) ~~~
    # Se define la ecuación z + 3w = 1 + 2i.
    sp.Eq(z + 3 * w, 1 + 2 * sp.I),

    # ~~~ Segunda ecuación del sistema b) ~~~
    # Se define la ecuación i*z + w = 2 - i.
    # SymPy entiende perfectamente la multiplicación de la unidad imaginaria (sp.I) por un símbolo (z).
    sp.Eq(sp.I * z + w, 2 - sp.I),
]

# ~~~ Resolución del sistema b) ~~~
# Se resuelve el sistema de ecuaciones `eqs_b` para las incógnitas `z` y `w`.
sol_b = sp.solve(eqs_b, (z, w))
print("b) Solución:", sol_b)


# ==============================
# Sistema c)
# (2+i)x + 2y = 1 + 7i
# (1-i)x + i*y = 0
# ==============================

# ~~~ Creación de la lista de ecuaciones para el sistema c) ~~~
eqs_c = [
    # ~~~ Primera ecuación del sistema c) ~~~
    # Aquí se muestra cómo usar coeficientes complejos para las variables.
    # (2 + sp.I) actúa como el coeficiente que multiplica al símbolo x.
    sp.Eq((2 + sp.I) * x + 2 * y, 1 + 7 * sp.I),

    # ~~~ Segunda ecuación del sistema c) ~~~
    # Se define la segunda ecuación con sus respectivos coeficientes complejos.
    sp.Eq((1 - sp.I) * x + sp.I * y, 0),
]

# ~~~ Resolución del sistema c) ~~~
# Se resuelve el sistema para las incógnitas `x` e `y`.
sol_c = sp.solve(eqs_c, (x, y))
print("c) Solución:", sol_c)


# ==============================
# Sistema d)
# (1+i)x - i*y = 2 + i
# (2+i)x + (2-i)y = 2i
# ==============================

# ~~~ Creación de la lista de ecuaciones para el sistema d) ~~~
eqs_d = [
    # ~~~ Primera ecuación del sistema d) ~~~
    # Se define la ecuación (1+i)x - i*y = 2 + i.
    sp.Eq((1 + sp.I) * x - sp.I * y, 2 + sp.I),

    # ~~~ Segunda ecuación del sistema d) ~~~
    # Se define la ecuación (2+i)x + (2-i)y = 2i.
    sp.Eq((2 + sp.I) * x + (2 - sp.I) * y, 2 * sp.I),
]

# ~~~ Resolución del sistema d) ~~~
# Se resuelve el último sistema para las incógnitas `x` e `y`.
sol_d = sp.solve(eqs_d, (x, y))
print("d) Solución:", sol_d)

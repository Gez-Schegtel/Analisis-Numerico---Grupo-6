# %% [markdown]
"""
# Practica N° 2: Transformada de Laplace

## 1) Cálculo de la Transformada de Laplace

Resolver los siguientes ejercicios de la [guía]()

* Ej. 1: 6
* Ej. 2: 5
* Ej. 3: 4
* Ej. 4: 3
* Ej. 5: 2
* Ej. 6: a
* Ej. 7: 2
* Ej. 8: a
* Ej. 9: b

a) Analíticamente (usando propiedades/tablas).
b) Con SymPy (Python) para verificar.

Documentar en el cuaderno los pasos analíticos y el código de validación.

### **Configuración Inicial de SymPy**

Antes de comenzar, es una buena práctica definir los símbolos que usaremos a lo largo del cuaderno.
"""

# %%
import sympy as sp

# Definimos los símbolos que utilizaremos
# t para el tiempo, s para la frecuencia. Se asumen reales y positivos.
t, s = sp.symbols('t s', real=True, positive=True)
# a y b para constantes genéricas (usadas en el último ejercicio).
a, b = sp.symbols('a b', real=True, positive=True)

# Inicializamos la impresión bonita (para que las fórmulas se vean bien en Jupyter)
sp.init_printing()

# %% [markdown]
"""
---
### **1. Transformada de $f(t) = \operatorname{sen}^2 t$**

#### **a) Cálculo Analítico**

Para resolver esta transformada, primero aplicamos una identidad trigonométrica de reducción de potencia para simplificar la función.

$$
\mathcal{L}\{\operatorname{sen}^2 t\}
$$

Usamos la identidad $\operatorname{sen}^2 t = \frac{1 - \cos(2t)}{2}$:
$$
= \mathcal{L}\left\{\frac{1}{2} - \frac{1}{2}\cos(2t)\right\}
$$

Por la propiedad de linealidad de la transformada de Laplace:
$$
= \frac{1}{2}\mathcal{L}\{1\} - \frac{1}{2}\mathcal{L}\{\cos(2t)\}
$$

Usando las transformadas de tabla para $\mathcal{L}\{1\} = \frac{1}{s}$ y $\mathcal{L}\{\cos(at)\} = \frac{s}{s^2+a^2}$:
$$
= \frac{1}{2} \cdot \frac{1}{s} - \frac{1}{2} \cdot \frac{s}{s^2 + 2^2}
$$
$$
= \frac{1}{2s} - \frac{s}{2(s^2+4)}
$$

Combinando las fracciones:
$$
= \frac{(s^2+4) - s^2}{2s(s^2+4)} = \frac{4}{2s(s^2+4)}
$$

$$
\mathcal{L}\{\operatorname{sen}^2 t\} = \frac{2}{s(s^2+4)}
$$

#### **b) Verificación con SymPy**
"""

# %%
f = sp.sin(t)**2
laplace_f = sp.laplace_transform(f, t, s, noconds=True)
print("La transformada de sen^2(t) es:")
laplace_f

# %% [markdown]
"""
---
### **2. Transformada de $f(t) = 1 + e^{4t}$**

#### **a) Cálculo Analítico**

Aplicamos la propiedad de linealidad directamente.
$$
\mathcal{L}\{1 + e^{4t}\} = \mathcal{L}\{1\} + \mathcal{L}\{e^{4t}\}
$$

Usando las transformadas de tabla para $\mathcal{L}\{1\} = \frac{1}{s}$ y $\mathcal{L}\{e^{at}\} = \frac{1}{s-a}$:
$$
= \frac{1}{s} + \frac{1}{s-4}
$$

Podemos combinar las fracciones (opcional):
$$
= \frac{(s-4) + s}{s(s-4)} = \frac{2s-4}{s(s-4)}
$$

$$
\mathcal{L}\{1 + e^{4t}\} = \frac{1}{s} + \frac{1}{s-4}
$$

#### **b) Verificación con SymPy**
"""

# %%
f = 1 + sp.exp(4*t)
laplace_f = sp.laplace_transform(f, t, s, noconds=True)
print("La transformada de 1 + e^(4t) es:")
laplace_f

# %% [markdown]
"""
---
### **3. Transformada de $f(t) = \cos^2 t$**

#### **a) Cálculo Analítico**

Similar al primer ejercicio, usamos una identidad de reducción de potencia: $\cos^2 t = \frac{1 + \cos(2t)}{2}$.
$$
\mathcal{L}\{\cos^2 t\} = \mathcal{L}\left\{\frac{1}{2} + \frac{1}{2}\cos(2t)\right\}
$$
$$
= \frac{1}{2}\mathcal{L}\{1\} + \frac{1}{2}\mathcal{L}\{\cos(2t)\}
$$
$$
= \frac{1}{2} \cdot \frac{1}{s} + \frac{1}{2} \cdot \frac{s}{s^2 + 4}
$$
$$
= \frac{(s^2+4) + s^2}{2s(s^2+4)} = \frac{2s^2+4}{2s(s^2+4)}
$$

$$
\mathcal{L}\{\cos^2 t\} = \frac{s^2+2}{s(s^2+4)}
$$

#### **b) Verificación con SymPy**
"""

# %%
f = sp.cos(t)**2
laplace_f = sp.laplace_transform(f, t, s, noconds=True)
print("La transformada de cos^2(t) es:")
laplace_f

# %% [markdown]
"""
---
### **4. Traslación en el eje s: $\mathcal{L}\{t(e^t + e^{2t})^2\}$**

#### **a) Cálculo Analítico**

Primero, expandimos la expresión algebraica de la función.
$$
f(t) = t(e^t + e^{2t})^2 = t(e^{2t} + 2e^{3t} + e^{4t}) = te^{2t} + 2te^{3t} + te^{4t}
$$

Aplicamos la linealidad:
$$
\mathcal{L}\{f(t)\} = \mathcal{L}\{te^{2t}\} + 2\mathcal{L}\{te^{3t}\} + \mathcal{L}\{te^{4t}\}
$$

Usamos el **Primer Teorema de Traslación**: $\mathcal{L}\{e^{at}g(t)\} = G(s-a)$, donde $G(s) = \mathcal{L}\{g(t)\}$.
En este caso, la función base es $g(t) = t$, cuya transformada es $G(s) = \mathcal{L}\{t\} = \frac{1}{s^2}$.

Aplicamos el teorema a cada término:
*   Para $\mathcal{L}\{te^{2t}\}$, $a=2$, entonces la transformada es $G(s-2) = \frac{1}{(s-2)^2}$.
*   Para $\mathcal{L}\{te^{3t}\}$, $a=3$, entonces la transformada es $G(s-3) = \frac{1}{(s-3)^2}$.
*   Para $\mathcal{L}\{te^{4t}\}$, $a=4$, entonces la transformada es $G(s-4) = \frac{1}{(s-4)^2}$.

Combinando los resultados:
$$
\mathcal{L}\{f(t)\} = \frac{1}{(s-2)^2} + \frac{2}{(s-3)^2} + \frac{1}{(s-4)^2}
$$

#### **b) Verificación con SymPy**
"""

# %%
f = t * (sp.exp(t) + sp.exp(2*t))**2
laplace_f = sp.laplace_transform(f, t, s, noconds=True)
print("La transformada de t(e^t + e^(2t))^2 es:")
laplace_f

# %% [markdown]
"""
---
### **5. Traslación en el eje t: $\mathcal{L}\{t \cdot \mathcal{U}(t-2)\}$**

#### **a) Cálculo Analítico**

Usamos el **Segundo Teorema de Traslación**: $\mathcal{L}\{g(t-a)\mathcal{U}(t-a)\} = e^{-as}G(s)$, donde $G(s) = \mathcal{L}\{g(t)\}$.

Nuestra función es $t\mathcal{U}(t-2)$. No está en la forma requerida. Debemos reescribir $t$ en términos de $(t-2)$.
$$
t = (t-2) + 2
$$
Entonces, la función es:
$$
f(t) = ((t-2) + 2)\mathcal{U}(t-2)
$$
Esto corresponde a una función $g(t-2)$ donde $g(t) = t+2$.

Ahora, calculamos la transformada de $g(t)$:
$$
G(s) = \mathcal{L}\{g(t)\} = \mathcal{L}\{t+2\} = \mathcal{L}\{t\} + \mathcal{L}\{2\} = \frac{1}{s^2} + \frac{2}{s}
$$

Finalmente, aplicamos el teorema con $a=2$:
$$
\mathcal{L}\{t \mathcal{U}(t-2)\} = e^{-2s} G(s) = e^{-2s} \left(\frac{1}{s^2} + \frac{2}{s}\right)
$$

#### **b) Verificación con SymPy**
"""

# %%
# sp.Heaviside es la función escalón unitario U(t)
f = t * sp.Heaviside(t-2)
laplace_f = sp.laplace_transform(f, t, s, noconds=True)
print("La transformada de t*U(t-2) es:")
laplace_f

# %% [markdown]
"""
---
### **6. Función Escalonada**

#### **a) Cálculo Analítico**

La función es:
$$
f(t) = \begin{cases} 2, & 0 \le t < 3 \\ -2, & t \ge 3 \end{cases}
$$

**Paso 1: Escribir $f(t)$ en términos de la función escalón unitario $\mathcal{U}(t)$.**
La función "comienza" con un valor de 2. En $t=3$, "salta" de 2 a -2, lo que es un cambio de -4.
$$
f(t) = 2\mathcal{U}(t-0) - 4\mathcal{U}(t-3) = 2 - 4\mathcal{U}(t-3)
$$

**Paso 2: Aplicar la transformada de Laplace.**
$$
\mathcal{L}\{f(t)\} = \mathcal{L}\{2\} - 4\mathcal{L}\{\mathcal{U}(t-3)\}
$$
Usando las transformadas de tabla $\mathcal{L}\{c\} = \frac{c}{s}$ y $\mathcal{L}\{\mathcal{U}(t-a)\} = \frac{e^{-as}}{s}$:
$$
= \frac{2}{s} - 4 \frac{e^{-3s}}{s} = \frac{2(1-2e^{-3s})}{s}
$$

#### **b) Verificación con SymPy**
"""

# %%
# Usamos sp.Piecewise para definir la función a trozos
f = sp.Piecewise((2, t < 3), (-2, t >= 3))
laplace_f = sp.laplace_transform(f, t, s, noconds=True)
print("La transformada de la función escalonada es:")
laplace_f

# %% [markdown]
"""
---
### **7. Derivada de la Transformada: $\mathcal{L}\{t \cos(2t)\}$**

#### **a) Cálculo Analítico**

Usamos la propiedad de la **derivada de la transformada**:
$$
\mathcal{L}\{t^n f(t)\} = (-1)^n \frac{d^n}{ds^n} F(s)
$$
En nuestro caso, $n=1$ y $f(t) = \cos(2t)$.

**Paso 1: Encontrar $F(s) = \mathcal{L}\{\cos(2t)\}$.**
$$
F(s) = \frac{s}{s^2+4}
$$

**Paso 2: Aplicar la propiedad (derivar y multiplicar por -1).**
$$
\mathcal{L}\{t \cos(2t)\} = (-1)^1 \frac{d}{ds} \left(\frac{s}{s^2+4}\right)
$$
Usando la regla del cociente para la derivada:
$$
= - \left[ \frac{(1)(s^2+4) - (s)(2s)}{(s^2+4)^2} \right]
$$
$$
= - \left[ \frac{s^2+4 - 2s^2}{(s^2+4)^2} \right] = - \left[ \frac{4-s^2}{(s^2+4)^2} \right]
$$

$$
\mathcal{L}\{t \cos(2t)\} = \frac{s^2-4}{(s^2+4)^2}
$$

#### **b) Verificación con SymPy**
"""

# %%
f = t * sp.cos(2*t)
laplace_f = sp.laplace_transform(f, t, s, noconds=True)
print("La transformada de t*cos(2t) es:")
laplace_f

# %% [markdown]
"""
---
### **8. Transformada de Integrales (Convolución): $\mathcal{L}\{1 * t^3\}$**

#### **a) Cálculo Analítico**

El asterisco `*` denota la operación de convolución. Usamos el **Teorema de Convolución**:
$$
\mathcal{L}\{f(t) * g(t)\} = F(s) \cdot G(s)
$$
Aquí, $f(t) = 1$ y $g(t) = t^3$.

**Paso 1: Encontrar las transformadas individuales.**
*   $F(s) = \mathcal{L}\{1\} = \frac{1}{s}$
*   $G(s) = \mathcal{L}\{t^3\} = \frac{3!}{s^{3+1}} = \frac{6}{s^4}$

**Paso 2: Multiplicar las transformadas.**
$$
\mathcal{L}\{1 * t^3\} = F(s) \cdot G(s) = \left(\frac{1}{s}\right) \cdot \left(\frac{6}{s^4}\right) = \frac{6}{s^5}
$$

#### **b) Verificación con SymPy**
"""

# %%
# SymPy no tiene un operador de convolución directo en su función de transformada.
# Verificamos el teorema calculando las transformadas por separado y multiplicándolas.
f1 = 1
f2 = t**3

L_f1 = sp.laplace_transform(f1, t, s, noconds=True)
L_f2 = sp.laplace_transform(f2, t, s, noconds=True)

# El resultado de la convolución en el dominio de s es el producto
L_conv = L_f1 * L_f2
print("La transformada de 1 * t^3 es:")
L_conv

# %% [markdown]
"""
---
### **9. Transformada de una Función Periódica**

#### **a) Cálculo Analítico**

La función es una onda de diente de sierra.
*   **Periodo:** $T = b$
*   **Función en el primer periodo ($0 \le t < b$):** Es una recta que pasa por (0,0) y (b,a). Su ecuación es $f_1(t) = \frac{a}{b}t$.

La fórmula para la transformada de una función periódica es:
$$
\mathcal{L}\{f(t)\} = \frac{1}{1 - e^{-sT}} \int_0^T e^{-st} f_1(t) \,dt
$$
Sustituyendo nuestros valores:
$$
\mathcal{L}\{f(t)\} = \frac{1}{1 - e^{-sb}} \int_0^b e^{-st} \left(\frac{a}{b}t\right) \,dt
$$

Resolvemos la integral por partes: $\int u \,dv = uv - \int v \,du$.
*   $u = \frac{a}{b}t \implies du = \frac{a}{b}dt$
*   $dv = e^{-st}dt \implies v = -\frac{1}{s}e^{-st}$

$$
\int_0^b e^{-st} \left(\frac{a}{b}t\right) \,dt = \left[-\frac{at}{bs}e^{-st}\right]_0^b - \int_0^b \left(-\frac{1}{s}e^{-st}\right)\left(\frac{a}{b}\right)dt
$$
$$
= \left(-\frac{ab}{bs}e^{-sb} - 0\right) + \frac{a}{bs}\int_0^b e^{-st}dt
$$
$$
= -\frac{a}{s}e^{-sb} + \frac{a}{bs}\left[-\frac{1}{s}e^{-st}\right]_0^b
$$
$$
= -\frac{a}{s}e^{-sb} + \frac{a}{bs}\left(-\frac{1}{s}e^{-sb} - (-\frac{1}{s})\right)
$$
$$
= -\frac{a}{s}e^{-sb} - \frac{a}{bs^2}e^{-sb} + \frac{a}{bs^2}
$$

Ahora, multiplicamos por el factor $\frac{1}{1 - e^{-sb}}$:
$$
\mathcal{L}\{f(t)\} = \frac{1}{1 - e^{-sb}} \left[ \frac{a}{bs^2} - \frac{a}{s}e^{-sb} - \frac{a}{bs^2}e^{-sb} \right]
$$

#### **b) Verificación con SymPy**
"""

# %%
# Definimos la función en el primer periodo
f1 = (a/b) * t

# Calculamos la integral sobre el primer periodo
integral_part = sp.integrate(f1 * sp.exp(-s*t), (t, 0, b))

# Aplicamos la fórmula completa para funciones periódicas
laplace_f = (1 / (1 - sp.exp(-s*b))) * integral_part

print("La transformada de la función periódica es:")
# Usamos sp.simplify() para obtener una forma más compacta
sp.simplify(laplace_f)

2) Creación de un Banco de Transformadas
a) Cada grupo debe crear un mini banco de transformadas de Laplace en Python:
b) Definir una función en Python mi_laplace(f) que calcule la transformada de una función
simbólica.
c) Documentar al menos 5 funciones relevantes.
d) Incluir ejemplos de verificación numérica con lambdify y gráficos comparativos.
En el caso de incluir al sexto participante (IA) deberá presentar las interacciones realizadas para la
realización del ejercicio.
3)Actividad de investigación:
a) Investigar sobre el origen, concepto y propiedades de la función Delta de Dirac.
b) Definir la trasformada de Laplace para esta ecuación y ejemplificar.
c) Resolver lo ejemplificado con código de validación en Python.

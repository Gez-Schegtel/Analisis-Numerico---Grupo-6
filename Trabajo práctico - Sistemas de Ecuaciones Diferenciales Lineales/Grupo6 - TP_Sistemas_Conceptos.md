---
title: "Análisis Numérico: Sistemas de Ecuaciones Diferenciales y Estabilidad"
author:
  - Ariel
  - Tincho
  - Rodri
  - Axel
  - Juancho
date: \today
geometry: margin=1.6in
colorlinks: true
header-includes:
  - \usepackage{fvextra}
  - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
  - \usepackage{graphicx}
  - \setkeys{Gin}{width=0.75\textwidth}
  - \usepackage{float}
  - \floatplacement{figure}{H}
  - \usepackage{tabularx}
  - \usepackage{array}
  - \renewcommand{\arraystretch}{1.5}
  
  # neutralizamos tightlist y ajustamos espaciado de listas
  - \let\tightlist\relax
  - \usepackage{enumitem}
  - \setlist[itemize,enumerate]{itemsep=1\baselineskip, topsep=1\baselineskip}
  
  # estilo rosado pálido con fuente aclarada
  - \usepackage[most]{tcolorbox}
  - |
    \newtcolorbox{noteBox}{
      colback=red!5!white,
      colframe=red!30!black,
      coltext=black!70,        % color del texto menos saturado
      arc=4pt,
      left=6pt, right=6pt, top=4pt, bottom=4pt,
      boxrule=0.5pt,
      breakable
    }
  - |
    \renewenvironment{quote}{\begin{noteBox}}{\end{noteBox}}

  # --- Caption sin numeración para figuras ---
  - \usepackage{caption}
  - \captionsetup[figure]{labelformat=empty}
---

# Etapa 1: Investigación del marco conceptual

## 1. Explicá con tus palabras la función principal de la Transformada de Laplace en el análisis de sistemas dinámicos.

La función principal de la Transformada de Laplace es convertir problemas de cálculo (ecuaciones diferenciales) en problemas de álgebra (ecuaciones polinómicas).

Esto es tan útil en sistemas dinámicos porque:

### 1. El Problema Original (Cálculo)
Los sistemas dinámicos (como un circuito eléctrico, un sistema masa-resorte, o la suspensión de un auto) se describen por cómo cambian en el tiempo ($t$).

Matemáticamente, esto casi siempre se representa con Ecuaciones Diferenciales Ordinarias (EDOs). Estas ecuaciones incluyen derivadas (como $\frac{dy}{dt}$) e integrales, y resolverlas puede ser muy complicado.

### 2. La "Traducción" Mágica (Álgebra)
Aquí entra Laplace. La transformada toma la ecuación diferencial en el dominio del tiempo ($t$) y la "traduce" a una ecuación algebraica en un nuevo dominio, llamado el dominio de Laplace ($s$).

La magia está en que:

*   La derivación ($\frac{d}{dt}$) se convierte en una multiplicación (por $s$).
    $$
    \mathcal{L}\{f'(t)\} \approx sF(s)
    $$
*   La integración ($\int dt$) se convierte en una división (entre $s$).
    $$
    \mathcal{L}\left\{\int_{0}^{t} f(\tau)d\tau\right\} = \frac{F(s)}{s}
    $$

De repente, esa ecuación diferencial complicada se transforma en una ecuación algebraica que podemos resolver despejando la variable.

### 3. La Solución y el Regreso
Una vez que resolvemos la ecuación fácil en el dominio $s$, simplemente usamos la Transformada Inversa de Laplace para "traducir" la solución de vuelta al dominio del tiempo ($t$).

## 2. Definí qué es un punto de equilibrio en un sistema de EDOs y cómo se determina.

En un sistema de Ecuaciones Diferenciales Ordinarias (EDOs), un punto de equilibrio es una solución constante del sistema.

Dicho de forma más intuitiva: es un estado en el que el sistema no cambia en el tiempo. Si el sistema comienza exactamente en un punto de equilibrio, permanecerá allí indefinidamente.

Matemáticamente, si tienes un sistema autónomo (donde el tiempo $t$ no aparece explícitamente en las funciones) escrito en forma vectorial:

$$
x' = f(x)
$$

Un punto $x^*$ es un punto de equilibrio si cumple que $f(x^*) = 0$. Es decir, es un punto donde todas las tasas de cambio (derivadas) son simultáneamente cero.

A estos puntos también se les suele llamar puntos críticos, puntos estacionarios o puntos fijos.

### ¿Cómo se Determinan?

El procedimiento para encontrar los puntos de equilibrio es puramente algebraico:

1.  **Igualar todas las derivadas a cero**: Tomas cada ecuación diferencial del sistema y haces que su derivada sea igual a cero.
2.  **Resolver el sistema algebraico resultante**: Al hacer esto, el sistema de EDOs se convierte en un sistema de ecuaciones algebraicas (generalmente no lineales).
3.  **Las soluciones son los puntos**: Cada solución que encuentres para ese sistema algebraico corresponde a las coordenadas de un punto de equilibrio.

## 3. Analizá cómo los autovalores y autovectores permiten caracterizar soluciones y estabilidad en sistemas lineales homogéneos.

Entender el rol de los autovalores y autovectores es, literalmente, la **clave** para descifrar el comportamiento de cualquier sistema lineal homogéneo. Son como el "ADN" del sistema: contienen toda la información sobre cómo evolucionará en el tiempo.

Vamos a desglosar su significado y función.

---

### **El Problema: $\mathbf{X}' = \mathbf{A}\mathbf{X}$**

Recordemos que estamos tratando de resolver un sistema donde la **velocidad de cambio ($\mathbf{X}'$)** en cualquier punto del espacio es determinada por la matriz $\mathbf{A}$ multiplicada por la **posición actual ($\mathbf{X}$)**.

La pregunta fundamental es: ¿Existen "caminos" o "direcciones" especiales en este espacio donde el movimiento sea particularmente simple? La respuesta es sí, y esas direcciones son los **autovectores**.

---

### **1. Autovectores: Las "Autopistas" del Sistema**

*   **Definición Intuitiva:** Un **autovector** de la matriz $\mathbf{A}$ es una **dirección** en el espacio de estados. Si el sistema comienza en un punto a lo largo de esta dirección, **se moverá a lo largo de esa misma dirección para siempre**, sin desviarse. Es como una "autopista" rectilínea en el plano de fases.

*   **Definición Matemática:** Un vector no nulo $\mathbf{v}$ es un autovector de $\mathbf{A}$ si, al multiplicar $\mathbf{A}$ por $\mathbf{v}$, el resultado es simplemente el mismo vector $\mathbf{v}$ escalado por un número $\lambda$.
    $$ \mathbf{A}\mathbf{v} = \lambda\mathbf{v} $$

*   **Conexión con el Sistema:** Si una solución $\mathbf{X}(t)$ está en la dirección del autovector $\mathbf{v}$, podemos escribirla como $\mathbf{X}(t) = f(t)\mathbf{v}$, donde $f(t)$ es una función escalar del tiempo. Al sustituir esto en la ecuación $\mathbf{X}' = \mathbf{A}\mathbf{X}$, obtenemos:
    $$ (f(t)\mathbf{v})' = \mathbf{A}(f(t)\mathbf{v}) $$
    $$ f'(t)\mathbf{v} = f(t)(\mathbf{A}\mathbf{v}) $$
    Usando la definición de autovector, $\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$:
    $$ f'(t)\mathbf{v} = f(t)(\lambda\mathbf{v}) $$
    $$ f'(t) = \lambda f(t) $$
    Esta es la ecuación diferencial más simple que existe, y su solución es una exponencial: $f(t) = c e^{\lambda t}$.

*   **La Gran Conclusión:** A lo largo de la "autopista" definida por un autovector $\mathbf{v}$, la solución es increíblemente simple:
    $$ \mathbf{X}(t) = \mathbf{v} e^{\lambda t} $$

---

### **2. Autovalores: La "Velocidad y Comportamiento" en las Autopistas**

*   **Definición Intuitiva:** El **autovalor** $\lambda$ asociado a un autovector $\mathbf{v}$ te dice **cómo se mueve el sistema a lo largo de esa "autopista"**. Es el "límite de velocidad" y la "dirección del tráfico" en esa ruta.

*   **Conexión con la Estabilidad:** El signo y la naturaleza (real o compleja) del autovalor determinan el comportamiento y la estabilidad del sistema.

#### **Caso 1: Autovalores Reales**

*   **Si $\lambda > 0$ (Positivo):** El término $e^{\lambda t}$ **crece exponencialmente al infinito**. A lo largo de la dirección del autovector, las soluciones **se alejan del origen**. Esto es un comportamiento **inestable**.
*   **Si $\lambda < 0$ (Negativo):** El término $e^{\lambda t}$ **decae exponencialmente a cero**. A lo largo de la dirección del autovector, las soluciones **se acercan al origen**. Esto es un comportamiento **estable**.

#### **Caso 2: Autovalores Complejos Conjugados ($\lambda = \alpha \pm i\beta$)**

*   **La Parte Real ($\alpha$):** Determina la **estabilidad** del movimiento.
    *   **Si $\alpha > 0$:** El término $e^{\alpha t}$ crece. Las soluciones se alejan del origen en **espirales hacia afuera**. Comportamiento **inestable (foco inestable)**.
    *   **Si $\alpha < 0$:** El término $e^{\alpha t}$ decae. Las soluciones se mueven hacia el origen en **espirales hacia adentro**. Comportamiento **estable (foco estable)**.
    *   **Si $\alpha = 0$:** El término $e^{\alpha t}$ es 1. Las soluciones **orbitan perpetuamente** alrededor del origen en elipses, sin acercarse ni alejarse. Comportamiento **marginalmente estable (centro)**.

*   **La Parte Imaginaria ($\beta$):** Determina la **velocidad de oscilación**. Un valor más grande de $\beta$ significa que las espirales u órbitas son más "rápidas" o "apretadas".

---

### **3. La Solución General: Combinando las Autopistas**

El **Principio de Superposición** nos dice que la solución general del sistema es una **combinación lineal** de las soluciones simples que encontramos a lo largo de cada "autopista" (autovector).

*   **Si tienes dos autovalores reales distintos $\lambda_1, \lambda_2$ con autovectores $\mathbf{v}_1, \mathbf{v}_2$:**
    Cualquier solución del sistema es una mezcla de movimientos a lo largo de esas dos direcciones.
    $$ \mathbf{X}(t) = c_1 \mathbf{v}_1 e^{\lambda_1 t} + c_2 \mathbf{v}_2 e^{\lambda_2 t} $$
    El comportamiento a largo plazo estará dominado por el autovalor con la parte real más grande.

### **Resumen: El ADN del Sistema**

| Componente | Rol Geométrico | Rol en la Solución | Rol en la Estabilidad |
| :--- | :--- | :--- | :--- |
| **Autovectores ($\mathbf{v}$)** | Definen las **"autopistas"** o direcciones de movimiento simple en el plano de fases. | Proporcionan la **dirección vectorial** de cada componente de la solución. | Definen los ejes de atracción/repulsión. |
| **Autovalores ($\lambda$)** | Definen la **"velocidad" y el "sentido"** del movimiento a lo largo de las autopistas. | Proporcionan el **comportamiento temporal** ($e^{\lambda t}$) de cada componente. | **Determinan completamente la estabilidad** del sistema. |

En esencia, al encontrar los autovalores y autovectores, estás "descomponiendo" un sistema complejo en sus movimientos más fundamentales y predecibles.

## 4. Compará las soluciones de un sistema lineal homogéneo con uno no homogéneo.

### Diferencia entre Sistemas Homogéneos y No Homogéneos

La diferencia fundamental radica en la **presencia de una entrada o "fuerza" externa**.

*   **Sistema Homogéneo:** $$\mathbf{x}' = A\mathbf{x}$$
    *   Describe la **respuesta natural** del sistema, es decir, cómo evoluciona por sí mismo basándose únicamente en sus condiciones iniciales (como soltar un péndulo o dejar que un circuito RC se descargue).

*   **Sistema No Homogéneo:** $$\mathbf{x}' = A\mathbf{x} + \mathbf{f}(t)$$
    *   Describe la **respuesta forzada**. El término $\mathbf{f}(t)$ es una entrada externa que "empuja" o "alimenta" al sistema (como empujar un columpio o aplicar un voltaje senoidal a un circuito).

La solución del sistema no homogéneo se construye usando la solución del homogéneo.

---

### Una Analogía: El Columpio

Imagina que un columpio es tu sistema dinámico.

**1. Sistema Homogéneo (Respuesta Natural)**
Llevas el columpio hacia atrás (esta es la *condición inicial*) y lo sueltas. El columpio oscilará a su propia frecuencia natural, perdiendo altura gradualmente debido a la fricción, hasta detenerse en el punto de equilibrio. Esa oscilación amortiguada es la **solución homogénea ($\mathbf{x}_h$)**.

**2. Sistema No Homogéneo (Respuesta Forzada)**
El columpio está quieto, y tú empiezas a empujarlo rítmicamente (esta es la *fuerza externa $\mathbf{f}(t)$*).

*   **Fase Transitoria:** Al principio, el movimiento será caótico. El columpio intentará oscilar a su frecuencia natural ($\mathbf{x}_h$) y a la frecuencia de tus empujones ($\mathbf{x}_p$) al mismo tiempo. Pasado un rato, el movimiento natural de "bamboleo" inicial (la parte homogénea) desaparece.
*   **Fase Estacionaria:** El columpio se sincroniza contigo y oscila *exactamente* a la frecuencia de tus empujones. Este movimiento final y sostenido es la **solución particular ($\mathbf{x}_p$)**.

---

### Comparación Detallada de las Soluciones

Aquí está la comparación en un formato de lista:

#### 1. Sistema Homogéneo ($\mathbf{x}' = A\mathbf{x}$)
*   **Estructura de la Solución:**
    $$\mathbf{x}(t) = \mathbf{x}_h(t)$$
*   **Significado Físico:** Representa la **Respuesta Natural** o Transitoria del sistema.
*   **Comportamiento:** Describe cómo el sistema vuelve al equilibrio (si es estable) basándose únicamente en sus condiciones iniciales.
*   **Rol de $\mathbf{x}(0)$:** Determina directamente las constantes $c_i$ de la solución $\mathbf{x}_h(t)$.
*   **Comportamiento a Largo Plazo:** (Si es estable) El sistema siempre tiende al origen ($\mathbf{0}$).

#### 2. Sistema No Homogéneo ($\mathbf{x}' = A\mathbf{x} + \mathbf{f}(t)$)
*   **Estructura de la Solución:**
    $$\mathbf{x}(t) = \mathbf{x}_h(t) + \mathbf{x}_p(t)$$
*   **Significado Físico:** Representa la **Respuesta Total** del sistema.
*   **Comportamiento:** Es la suma de dos partes:
    *   **$\mathbf{x}_h(t)$ (Solución Homogénea):** Es la parte **transitoria**. Generalmente, $\mathbf{x}_h(t) \to \mathbf{0}$ con el tiempo (si el sistema es estable).
    *   **$\mathbf{x}_p(t)$ (Solución Particular):** Es la parte de **estado estacionario**. Describe el comportamiento a largo plazo del sistema, "arrastrado" por la fuerza externa $\mathbf{f}(t)$.
*   **Rol de $\mathbf{x}(0)$:** Determina las constantes $c_i$ de la parte $\mathbf{x}_h(t)$ para asegurar que la solución total cumpla la condición inicial: $\mathbf{x}_h(0) + \mathbf{x}_p(0) = \mathbf{x}(0)$.
*   **Comportamiento a Largo Plazo:** (Si es estable) El sistema tiende a la solución particular $\mathbf{x}_p(t)$.

---

### El Rol Clave de la Solución Homogénea ($\mathbf{x}_h$)

> **Pregunta:** Si la solución homogénea $\mathbf{x}_h$ tiende a cero, ¿por qué la calculamos en el caso no homogéneo?
>
> **Respuesta:** Porque $\mathbf{x}_h(t)$ es la única parte de la solución que tiene constantes arbitrarias ($c_1, c_2, \dots$), las cuales son necesarias para satisfacer la condición inicial.

El proceso es el siguiente:
1.  Encontramos una **solución particular $\mathbf{x}_p(t)$** que funcione. Esta solución no tiene constantes libres y está completamente determinada por la fuerza externa $\mathbf{f}(t)$.
2.  Al sumarle la **solución homogénea $\mathbf{x}_h(t)$**, le agregamos "flexibilidad" a la solución total.
3.  Usamos esa flexibilidad (ajustando las constantes $c_i$ de $\mathbf{x}_h(t)$) para cumplir con la **condición inicial $\mathbf{x}(0)$**.

#### En resumen:
*   $\mathbf{x}_p(t)$ dicta el comportamiento a **largo plazo** (el estado estacionario).
*   $\mathbf{x}_h(t)$ dicta el comportamiento a **corto plazo** (la transición) y ajusta la solución para que comience en el lugar correcto $\mathbf{x}(0)$.


## 5. Elaborá un diagrama de flujo del algoritmo de resolución de sistemas homogéneos y no homogéneos (utilizando Laplace).

## 6. Diseñá un esquema visual que clasifique los tipos de puntos de equilibrio y la estabilidad asociada.


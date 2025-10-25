---
title: "Análisis Numérico"
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

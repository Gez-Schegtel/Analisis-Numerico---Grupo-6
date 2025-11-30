---
geometry: "margin=1in, landscape"
header-includes:
  - \usepackage{amsmath}
  - \usepackage{array}
  # 1. Espacio Vertical: Separa las filas (3.2 veces el tamaño normal)
  - \renewcommand{\arraystretch}{3.2}
  # 2. Espacio Horizontal: Margen a los costados dentro de la celda
  - \setlength{\tabcolsep}{15pt}
---

# Tabla de Diferencias Divididas

\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{x} & \textbf{f(x)} & \textbf{Dif. de orden 1} & \textbf{Dif. de orden 2} & \textbf{Dif. De orden 3} \\ \hline
$x_0$ & $f(x_0)$ & & & \\ \hline
& & $\displaystyle f[x_0, x_1] = \frac{f[x_1]-f[x_0]}{x_1 - x_0}$ & & \\ \hline
$x_1$ & $f(x_1)$ & & $\displaystyle f[x_0, x_1, x_2] = \frac{f[x_1, x_2]-f[x_0, x_1]}{x_2 - x_0}$ & \\ \hline
& & $\displaystyle f[x_1, x_2] = \frac{f[x_2]-f[x_1]}{x_2 - x_1}$ & & $\displaystyle f[x_0, \dots, x_3] = \frac{f[x_1, x_2, x_3]-f[x_0, x_1, x_2]}{x_3 - x_0}$ \\ \hline
$x_2$ & $f(x_2)$ & & $\displaystyle f[x_1, x_2, x_3] = \frac{f[x_2, x_3]-f[x_1, x_2]}{x_3 - x_1}$ & \\ \hline
& & $\displaystyle f[x_2, x_3] = \frac{f[x_3]-f[x_2]}{x_3 - x_2}$ & & \\ \hline
$x_3$ & $f(x_3)$ & & & \\ \hline
\end{tabular}
\end{table}

# Comparativa de Tiempos de Ejecución: Método Iterativo vs. Recursivo

Este documento presenta los resultados obtenidos al comparar los tiempos de ejecución de dos métodos para reconstrucción de señales: uno **iterativo** y otro **recursivo**.

## Resultados

| N  | Iterativo (s) | Recursivo (s) |
|----|----------------|----------------|
| 5  | 0.016041       | 0.000000       |
| 10 | 0.005207       | 0.002478       |
| 20 | 0.002659       | 0.001051       |
| 50 | 0.005576       | 0.001894       |

## Análisis

Según la tabla, el método recursivo muestra tiempos de ejecución más bajos que el iterativo para los valores de N = 5, 10, 20 y 50. Esto sugiere que, en estos rangos, la recursión es más rápida para reconstruir la señal.

Sin embargo, es importante considerar que el método recursivo **no es necesariamente más eficiente en general**. Su desempeño puede verse limitado por la **profundidad de recursión**, lo cual puede generar errores o afectar negativamente el rendimiento para valores altos de N.

Por el contrario, el método iterativo, aunque ligeramente más lento en estos casos específicos, es:

- Más **estable**
- Más **escalable**
- Más **fácil de mantener**

Por estas razones, sigue siendo la opción más segura y eficiente a largo plazo.

## Conclusión

Ambos métodos tienen ventajas y desventajas. La elección entre uno u otro dependerá del tamaño del problema, los recursos disponibles y la importancia de la mantenibilidad del código.

Resultado de los tiempos de ejecución 


 	Tiempos
N	Iterativo(s)	Recursivo(s)
5	0.016041	0.000000
10	0.005207	0.002478
20	0.002659	0.001051
50	0.005576	0.001894

Según la tabla, el método recursivo muestra tiempos de ejecución más bajos que el iterativo para los valores de N=5,10,20,50, lo que sugiere que, en estos rangos, es más rápido al momento de reconstruir la señal. Sin embargo, este método no es necesariamente más eficiente en general, ya que su desempeño se ve limitado por la profundidad de recursión, lo que puede causar errores o bajo rendimiento para valores altos de N. En cambio, el método iterativo, aunque ligeramente más lento en estos casos, es más estable, escalable y fácil de mantener, por lo que sigue siendo la opción más segura y eficiente a largo plazo.

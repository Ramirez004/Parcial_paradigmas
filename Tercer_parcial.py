import numpy as np
import time

T = 2 * np.pi
t = np.linspace(0, T, 1000)
f = np.sign(np.sin(t))

def calcular_serie_fourier_iterativa(f, t, T, N):
    a, b = [], []
    for n in range(N + 1):
        a_n = (2 / T) * np.trapz(f * np.cos(n * 2 * np.pi * t / T), t)
        b_n = (2 / T) * np.trapz(f * np.sin(n * 2 * np.pi * t / T), t)
        a.append(a_n)
        b.append(b_n)
    return a, b

def calcular_serie_fourier_recursiva(a, b, t, T, n=0):
    if n == len(a):
        return np.zeros_like(t)
    suma = a[n] * np.cos(n * 2 * np.pi * t / T) + b[n] * np.sin(n * 2 * np.pi * t / T)
    return suma + calcular_serie_fourier_recursiva(a, b, t, T, n + 1)

N = 5

inicio1 = time.time()
a, b = calcular_serie_fourier_iterativa(f, t, T, N)
fin1 = time.time()

inicio2 = time.time()
f_aprox = calcular_serie_fourier_recursiva(a, b, t, T)
fin2 = time.time()

print(f"Tiempo iterativo: {fin1 - inicio1:.8f}")
print(f"Tiempo recursivo: {fin2 - inicio2:.40f}")



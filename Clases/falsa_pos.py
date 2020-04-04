##
# 1
import numpy as np

def f1(x):
    return -np.sqrt(3 * x) ** (2.0 / 5.0) + (x ** 3) * np.cos(3 * x) + 4 * x ** 2 - 7

x0 = 1.
x1 = 2.

tolx = 10 ** -10
tolf = tolx

x2_prev = x1

iter = 0
while True:
    iter += 1

    x2 = x1 - (f1(x1) * (x1 - x0) / (f1(x1) - f1(x0)))

    if np.abs(x2 - x2_prev) <= tolx:
        break
    if np.abs(f1(x2)) <= tolf:
        break

    if f1(x2)*f1(x0) < 0:
        x1 = x2
    else:
        x0 = x2

    x2_prev = x2

print(f"Falsa posicion - La raiz es: {x2}")
print(f"Falsa posicion - Numero de iteraciones: {iter}")

##
# 2

import numpy as np

def f1(x):
    return -x ** 0.25 + np.sin(3.5 * x) + 4 * np.sqrt(x) + 2 * x - 5

x0 = 1.
x1 = 2.

tolx = 10 ** -5
tolf = tolx

x2_prev = x1

iter = 0
while True:
    iter += 1

    x2 = x1 - (f1(x1) * (x1 - x0) / (f1(x1) - f1(x0)))

    if np.abs(x2 - x2_prev) <= tolx:
        break
    if np.abs(f1(x2)) <= tolf:
        break

    if f1(x2)*f1(x0) < 0:
        x1 = x2
    else:
        x0 = x2

    x2_prev = x2

print(f"Falsa posicion - La raiz es: {x2}")
print(f"Falsa posicion - Numero de iteraciones: {iter}")

##
# 3

import numpy as np

def f1(x):
    return -x ** 0.25 + np.sin(3.5 * x) + 4 * np.sqrt(x) + 2 * x - 5

x0 = -1.
x1 = 2.

tolx = 10 ** -10
tolf = tolx

x2_prev = x1

iter = 0
while True:
    iter += 1

    x2 = x1 - (f1(x1) * (x1 - x0) / (f1(x1) - f1(x0)))

    if np.abs(x2 - x2_prev) <= tolx:
        break
    if np.abs(f1(x2)) <= tolf:
        break

    if f1(x2)*f1(x0) < 0:
        x1 = x2
    else:
        x0 = x2

    x2_prev = x2

print(f"Falsa posicion - La raiz es: {x2}")
print(f"Falsa posicion - Numero de iteraciones: {iter}")
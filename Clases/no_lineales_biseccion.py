""" 1. Estas ecuaciones son no lineales porque hay un termino de x
 que tiene un exponente distinto de 1. Puede ser mayor, menor o puede ser decimal"""

##
# 2
import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return -x ** 0.25 + np.sin(3.5 * x) + 4 * np.sqrt(x) + 2 * x - 5

plt.figure()
xf = np.arange(0, 2, 0.00001)
indadmin = np.argmin(np.abs(f1(xf)))
print(f"Solucion: {xf[indadmin]}")

plt.plot(xf, f1(xf), "-")
plt.plot(xf[indadmin], f1(xf[indadmin]), "or")
plt.grid(linestyle="--")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

##
# 3.
import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return -np.sqrt(3*x)**(2.0/5.0) + (x**3) * np.cos(3 * x) + 4 * x**2 - 7

x0 = 1.
x1 = 2.

tolx = 10 ** -10
tolf = tolx

x2_prev = x1

iter = 0

while True:
    iter += 1
    x2 = (x0 + x1) / 2.

    # Criterio de tolerancia en X
    if np.abs(x2 - x2_prev) <= tolx:
        break
    # Criterio de tolerancia en F
    if np.abs(f1(x2)) <= tolf:
        break
    if f1(x2)*f1(x0) < 0:
        x1 = x2
    else:
        x0 = x2

print(f"La raiz es: {x2}")
print(f"La iteracion es: {iter}")

##
# 4.
import numpy as np

def f1(x):
    return -x ** 0.25 + np.sin(3.5 * x) + 4 * np.sqrt(x) + 2 * x - 5

x0 = 1.
x1 = 2.

tolx = 10 ** -10
tolf = tolx

x2_prev = x1

iter = 0

while True:
    iter += 1
    x2 = (x0 + x1) / 2.

    # Criterio de tolerancia en X
    if np.abs(x2 - x2_prev) <= tolx:
        break
    # Criterio de tolerancia en F
    if np.abs(f1(x2)) <= tolf:
        break
    if f1(x2)*f1(x0) < 0:
        x1 = x2
    else:
        x0 = x2

print(f"La raiz es: {x2}")
print(f"La iteracion es: {iter}")

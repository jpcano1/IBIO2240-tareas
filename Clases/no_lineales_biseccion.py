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

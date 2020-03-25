import numpy as np
import matplotlib.pyplot as plt

# Estas ecuaciones son no lineales porque hay un termino de x
# que tiene un exponente distinto de 1.
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



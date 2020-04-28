import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

def polynom_coeff(pX, pY):
    A = np.vander(pX)
    b = pY
    coeffs = np.linalg.solve(A, b)
    return coeffs

def lagrange_coeff(pX, pY):
    polynom = lagrange(pX, pY)
    coeffs = Polynomial(polynom).coef
    return coeffs

def new_values(coeffs, pX):
    N = len(coeffs)
    y_salida = np.zeros(len(pX))
    for i in range(len(pX)):
        for j in range(N):
            y_salida[i] += (coeffs[j] * (pX[i] ** (N - j - 1)))
    return y_salida

def plot_interpolation(pPoints, pObtained, pNew, pOption):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(pObtained.loc[:, "x"], pObtained.loc[:, "y"], "b", label="Polinomio Obtenido")
    ax.plot(pPoints.loc[:, "x"], pPoints.loc[:, "y"], "rs", label="Puntos Iniciales")
    ax.plot(pPoints.loc[:, "x"], pPoints.loc[:, "y"], "--", color="0.5")
    ax.plot(pNew.loc[:, "x"], pNew.loc[:, "y"], "g^", label="Puntos estimados")
    ax.grid(linestyle="--")
    ax.legend(loc="best")
    title = "Interpolación por matriz de Vandermonde" if pOption == 1 else "Interpolación por polinomio de Lagrange"
    ax.set_title(title)
    ax.set_ylabel("y")
    ax.set_xlabel("x")
    plt.show()

def generate_interpolation_frames(pOption):
    rand_x = np.sort(np.random.rand(10) * 10)
    rand_y = np.random.rand(10) * 5
    points = pd.DataFrame({"x": rand_x, "y": rand_y})
    # Coefficients
    coef = polynom_coeff(points.loc[:, "x"], points.loc[:, "y"]) if pOption == 1 else lagrange_coeff(points.loc[:, "x"], points.loc[:, "y"])
    # Valores obtenidos
    sample = np.arange(points.iloc[0, 0], points.iloc[-1, 0], 0.01)
    y_obtained = new_values(coef, sample)
    obtained = pd.DataFrame(zip(sample, y_obtained), columns=["x", "y"])
    # Valores estimados
    random_data = np.sort(np.random.rand(10) * 10)
    y_estimated = new_values(coef, random_data)
    new = pd.DataFrame(zip(random_data, y_estimated), columns=["x", "y"])
    return points, obtained, new

def print_menu():
    print("--------Laboratorio 9----------")
    print("Escoja la opcion: ")
    print("1. Interpolación por metodo matricial")
    print("2. Interpolación por polinomio de Lagrange")
    print("3. Tabla")

if __name__ == "__main__":
    finished = False

    while not finished:
        print_menu()
        option = int(input())

        if option == 1:
            df, df_obtained, df_new = generate_interpolation_frames(1)
            plot_interpolation(df, df_obtained, df_new, 1)
        elif option == 2:
            df, df_obtained, df_new = generate_interpolation_frames(2)
            plot_interpolation(df, df_obtained, df_new, 2)
        elif option == 3:
            pass
        else:
            finished = True
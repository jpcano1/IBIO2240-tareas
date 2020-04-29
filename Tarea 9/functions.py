import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline
from numpy.polynomial.polynomial import Polynomial
import struct as st

def polynom_coeff(pX, pY):
    A = np.vander(pX)
    b = pY
    coeffs = np.linalg.solve(A, b)
    return coeffs

def lagrange_coeff(pX, pY):
    polynom = lagrange(pX, pY)
    coeffs = Polynomial(polynom).coef
    return coeffs

def spline_coeff(pX, pY, method="not-a-knot"):
    return CubicSpline(pX, pY, bc_type=method)

def new_values(coeffs, pX):
    N = len(coeffs)
    y_salida = np.zeros(len(pX))
    for i in range(len(pX)):
        for j in range(N):
            y_salida[i] += (coeffs[j] * (pX[i] ** (N - j - 1)))
    return y_salida

def read_data():
    file = open("x_obs.bin", "rb")
    var1 = file.read()
    x_data = st.unpack("d" * int(len(var1) / 8), var1)
    file.close()
    file = open("y_obs.bin", "rb")
    var1 = file.read()
    y_data = st.unpack("d" * int(len(var1) / 8), var1)
    return pd.DataFrame({"x": x_data, "y": y_data})

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
    print("3. Tabla del 3 punto")
    print("4. Tabla del 4 punto")
    print("5. Tabla del 5 punto")

if __name__ == "__main__":
    finished = False
    new_points = np.array([78.12, 0.98, 67.59, 8.69, 55.69, 48.12, 13.24, 97.56, 25.69, 1.26])

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
            df = read_data()
            # Coeficientes
            c_vandermonde = polynom_coeff(df.loc[:, "x"], df.loc[:, "y"])
            c_lagrange = lagrange_coeff(df.loc[:, "x"], df.loc[:, "y"])
            c_poly = np.polyfit(df.loc[:, "x"], df.loc[:, "y"], np.size(df.loc[:, "x"]) - 1)

            y_vandermonde = new_values(c_vandermonde, new_points)
            y_lagrange = new_values(c_lagrange, new_points)
            y_poly = new_values(c_poly, new_points)

            new_df = pd.DataFrame({"x_new": new_points,
                                   "Polinomial": y_vandermonde,
                                   "Lagrange": y_lagrange,
                                   "Numpy": y_poly})
            print(new_df.head())

        elif option == 4:
            pass

        elif option == 5:
            df = read_data()
            f_spline = spline_coeff(df.loc[:, "x"], df.loc[:, "y"])
            y_spline = f_spline(new_points)
            new_df = pd.DataFrame({"x_new": new_points,
                                   "y_new": y_spline})
            new_df.to_excel("Valores.xlsx", sheet_name="spline_coeff")
        else:
            finished = True
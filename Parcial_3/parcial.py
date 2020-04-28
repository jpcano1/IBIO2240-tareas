import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

# funciones
def f(y, z=1):
    return y**2 * np.log(y**2) + 371.093 * y**2 + 12800. * (y**2 - 1) * z - 2874.3785

def f_rcrit(y):
    return y * 0.00055

def graph(f):
    y = np.arange(0.5, 12., 0.001)
    z = np.arange(0.001, 0.101, 0.01)
    fig = plt.figure(figsize=(5, 5))

    ax = fig.add_subplot(111)
    for index in z:
        ax.plot(y, f(y, index), "--",label=f"z={index:4f}")
    ax.grid(1)
    ax.legend(loc="best")
    ax.set_xlabel("$y$")
    ax.set_ylabel("$f(y)$")
    plt.show()
    return

def biseccion(f, x0, x1, tolx, tolf, z):
    x2_prev = x1

    results = []
    index = 0
    while True:
        index += 1
        x2 = (x0 + x1) / 2.
        results.append(x2)

        if np.abs(x2 - x2_prev) <= tolx:
            break

        if np.abs(f(x2, z=z)) <= tolf:
            break

        if f(x2, z=z) * f(x0, z=z) < 0:
            x1 = x2
        else:
            x0 = x2
    results = np.array(results)
    return results, index, f_rcrit(results)

def falsa_posicion(f, x0, x1, tolx, tolf, z):
    x2_prev = x1

    results = []
    index = 0
    while True:
        index += 1
        x2 = x1 - (f(x1, z=z) * (x1 - x0) / (f(x1, z=z) - f(x0, z=z)))

        results.append(x2)
        if np.abs(x2 - x2_prev) <= tolx:
            break
        if np.abs(f(x2, z=z)) <= tolf:
            break

        if f(x2, z=z) * f(x0, z=z) < 0:
            x1 = x2
        else:
            x0 = x2

        x2_prev = x2

    results = np.array(results)
    return results, index, f_rcrit(results)

def newton_raphson(f, x1, tolx, tolf, z):
    x2_prev = x1
    results = []

    x = np.linspace(0.01, 10, 50)
    func = InterpolatedUnivariateSpline(x, f(x, z=z))
    dfdx = func.derivative()

    index = 0
    while True:
        index += 1

        d1_eval = dfdx(x1)
        x2 = x1 - (f(x1, z=z) / d1_eval)
        results.append(x2)

        if np.abs(x2 - x2_prev) <= tolx:
            break

        if np.abs(f(x2, z=z)) <= tolf:
            break

        x1 = x2
        x2_prev = x2

    results = np.array(results)
    return results, index, f_rcrit(results)

def graph_frame(frame1, frame2, frame3):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    #Frame 1
    z = frame1.loc[:, "Z"]
    y = frame1.loc[:, "Y"]
    r_crit = frame1.loc[:, "r_crit"]
    ax.plot(y, z, "rs--", label="Y biseccion")
    ax.plot(r_crit, z, "r*--", label="$r_{crit}$ biseccion")

    # Frame 2
    z = frame2.loc[:, "Z"]
    y = frame2.loc[:, "Y"]
    r_crit = frame2.loc[:, "r_crit"]
    ax.plot(y, z, "go--", label="Y Newton", alpha=0.5)
    ax.plot(r_crit, z, "gv--", label="$r_{crit}$ Newton", alpha=0.5)

    # Frame 3
    z = frame3.loc[:, "Z"]
    y = frame3.loc[:, "Y"]
    r_crit = frame3.loc[:, "r_crit"]
    ax.plot(y, z, "bp--", label="Y falsa posicion", alpha=0.3)
    ax.plot(r_crit, z, "bP--", label="$r_{crit}$ falsa posicion", alpha=0.3)

    ax.grid(1)
    ax.legend(loc="best")
    ax.set_ylabel("Z")
    plt.show()

def execute_method(method, z, fun=f, x0=1., x1=12., tolx=10 ** -5, tolf=10 ** -5):
    if method == "NR":
        results, iterations, rcrit = newton_raphson(fun, x1, tolx, tolf, z)
    else:
        if method == "BI":
            results, iterations, rcrit = biseccion(fun, x0, x1, tolx, tolf, z)
        else:
            results, iterations, rcrit = falsa_posicion(fun, x0, x1, tolx, tolf, z)
    return results, iterations, rcrit

def print_menu():
    print("----------Parcial 3----------")
    print("Escoja la opcion: ")
    print("1. Grafica de la funcion para valores de 'z' e 'y'")
    print("2. Metodo de la biseccion")
    print("3. Metodo de Newton-raphson")
    print("4. Metodo de falsa posicion")
    print("5. Grafica de z")
    print("6. Salir")
    return

def print_list(lista, z, method):
    frame = []
    for t, z_value in zip(lista, z):
        res, ite, rcrits = t
        frame.append((z_value, ite, res[-1], rcrits[-1]))
        print(f"Z: {z_value} iterations: {ite} root: {res[-1]}, rcrit: {rcrits[-1]}")
    frame = pd.DataFrame(frame, columns=["Z", "Iteraciones", "Y", "r_crit"])
    # graph_frame(frame, method)
    # frame.to_excel(f"{method}.xlsx")
    return frame

if __name__ == "__main__":
    finished = False
    frames = []
    while not finished:
        print_menu()
        option = int(input())

        if option == 1:
            graph(f)
        elif option == 2:
            tuples = list()
            valores_z = np.arange(0.001, 0.111, 0.01)
            for i in valores_z:
                tuples.append(execute_method("BI", i))
            df = print_list(tuples, valores_z, "BI")
            frames.append(df)
        elif option == 3:
            tuples = list()
            valores_z = np.arange(0.001, 0.111, 0.01)
            for i in valores_z:
                tuples.append(execute_method("NR", i))
            df = print_list(tuples, valores_z, "NR")
            frames.append(df)
        elif option == 4:
            tuples = list()
            valores_z = np.arange(0.001, 0.111, 0.01)
            for i in valores_z:
                tuples.append(execute_method("FP", i))
            df = print_list(tuples, valores_z, "FP")
            frames.append(df)
        elif option == 5:
            graph_frame(frames[0], frames[1], frames[2])
        elif option == 6:
            finished = True
        else:
            print("Opcion no valida")
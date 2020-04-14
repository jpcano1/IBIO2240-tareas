import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt

def plot_function(f, c="#e60000", low=0.01, high=5.):
    """
    @param f:
    @param c:
    @param low:
    @param high:
    @return:
    """
    colors = [c]
    plt.style.use("dark_background")
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey

    fig, ax = plt.subplots()
    ax.axhline(y=0, color="#1E1F3C")

    x = np.linspace(low, high, 1000)
    ax.plot(x, f(x), '-', color=colors[0])

    n_shades = 10
    diff_linewidth = 1.05
    alpha_value = 0.3 / n_shades

    for n in range(1, n_shades + 1):
        ax.plot(x, f(x), '-', color=colors[0],
                linewidth=2+(diff_linewidth*n), alpha=alpha_value)

    df = pd.DataFrame({'function': f(x)}, index=x)
    for column, color in zip(df, colors):
        ax.fill_between(color=color,
                        x=df.index,
                        y1=df[column].values,
                        y2=[0] * len(df),
                        alpha=0.1)
    ax.grid(color='#2A3459')
    plt.show()
    return

def biseccion(f, x0, x1, tolx, tolf):
    """
    @param f:
    @param x0:
    @param x1:
    @param tolx:
    @param tolf:
    @return:
    """
    x2_prev = x1

    results = []
    while True:
        x2 = (x0 + x1) / 2.
        results.append(x2)

        if np.abs(x2 - x2_prev) <= tolx:
            break

        if np.abs(f(x2)) <= tolf:
            break

        if f(x2) * f(x0) < 0:
            x1 = x2
        else:
            x0 = x2

    return np.array(results)

def falsa_posicion(f, x0, x1, tolx, tolf):
    """
    @param f:
    @param x0:
    @param x1:
    @param tolx:
    @param tolf:
    @return:
    """
    x2_prev = x1

    results = []
    while True:
        x2 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))

        results.append(x2)
        if np.abs(x2 - x2_prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break

        if f(x2) * f(x0) < 0:
            x1 = x2
        else:
            x0 = x2

        x2_prev = x2

    return np.array(results)

def punto_fijo(f, g, x1, tolx, tolf):
    pass

def newton_raphson(f, x1, tolx, tolf):
    x2_prev = x1
    results = []

    x = np.linspace(0.01, 10, 50)
    func = InterpolatedUnivariateSpline(x, f(x))
    dfdx = func.derivative()

    while True:
        d1_eval = dfdx(x1)
        x2 = x1 - (f(x1) / d1_eval)
        results.append(x2)

        if np.abs(x2 - x2_prev) <= tolx:
            break

        if np.abs(f(x2)) <= tolf:
            break

        x1 = x2
        x2_prev = x2

    return np.array(results)

def secante(f, x0, x1, tolx, tolf):
    x2_prev = x1
    results = []

    while True:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        results.append(x2)

        if np.abs(x2 - x2_prev) <= tolx:
            break

        if f(x2) <= tolf:
            break

        x0, x1, x2_prev = x1, x2, x2

    return np.array(results)

def convergencia(f, x0, points):
    root_true = opt.fsolve(f, x0)

    est_arr = np.abs(points - root_true)

    r_arr = (np.log10(est_arr[1: np.size(est_arr) - 1] /
                      est_arr[2: np.size(est_arr)]) /
             np.log10(est_arr[0: np.size(est_arr) - 2] /
                      est_arr[1: np.size(est_arr) - 1]))
    return r_arr

def print_menu():
    """
        Prints menu on the main method
    """
    print("----------Laboratorio 7----------")
    print("Escoja la opcion: ")
    print("1. Metodo de la biseccion")
    print("2. Metodo de falsa posicion")
    print("3. Metodo del punto fijo")
    print("4. Metodo de Newton-raphson")
    print("5. Metodo de la secante")
    print("6. Tasa de convergencia de una funcion")
    print("7. Graficar funcion")
    print("8. Salir")

def print_list(a):
    print(f"Numero de iteraciones {len(a)}")
    for item in a:
        print(f"Aproximacion: {item}")
    return

def transform(cadena):
    partes = cadena.split("**")
    base = float(partes[0])
    expo = float(partes[1])
    return base ** expo

def pick_color():
    colors = [
        ('#08F7FE', "teal cyan"),
        ('#FE53BB', "savage pink"),
        ('#F5D300', "yellow"),
        ('#00ff41', "matrix letter"),
        ("#3b064d", "neon purple"),
        ("#8105d8", "party violet"),
        ("#ed0cef", "Rebel Fucsia"),
        ("#fe59d7", "kinky pinky"),
        ("#ff3503", "mandarin orange"),
        ("#08ff08", "glow green"),
        ("#00fdff", "heaven Turquoise"),
        ("#e60000", "electric red")
    ]
    print("Pick a color, if you can: ")
    i = 1

    for color in colors:
        print(f"{i}. {color[1]}")
        i += 1
    print(f"{i}. None of them")

    col = int(input())

    if col == i:
        col = input("Insert your color, hexadecimal format. Ex: #000000: ")
        return col

    return colors[col-1][0]

if __name__ == "__main__":
    finished = False

    def f1(x):
        # func = x ** 2 - 7
        func = np.exp(-5. * x**2) - (x ** (3./4.)) + np.sin(4. * x) - 1
        return func

    def f2(x):
        return np.sin(4. * x) * np.sqrt(x ** 2) + x**5 + 6*x - 4

    def f3(x):
        h = np.pi / 2
        c = np.pi / 2
        func = -3.65 * np.log(x / 5.33) + np.sqrt(2) * np.exp(-c**2 - 4.25) + 10.54 * np.cos(x - 2.2) - h
        return func

    print("Escoja la funcion a utilizar durante la ejecucion: ")
    option = int(input("1. f1, 2. f2 o 3. f3"))
    func_1 = f1 if option == 1 else (f2 if option == 2 else f3)

    while not finished:
        print_menu()
        option = int(input())
        if option == 1:
            plot_function(func_1)
            print("Basado en la grafica, determine el rango de busqueda")
            a = float(input("Limite inferior del rango: "))
            b = float(input("Limite superior del rango: "))
            t = transform(input("Defina la toleracia: "))
            ans = biseccion(func_1, a, b, t, t)
            print_list(ans)
            print(f"{func_1(ans[-1])}")

        elif option == 2:
            plot_function(func_1)
            print("Basado en la funcion, determine el rango de busqueda")
            a = float(input("Limite inferior del rango: "))
            b = float(input("Limite superior del rango: "))
            t = transform(input("Defina la toleracia: "))
            ans = falsa_posicion(func_1, a, b, t, t)
            print_list(ans)
            print(f"{func_1(ans[-1])}")

        elif option == 3:
            print("Hola")

        elif option == 4:
            plot_function(func_1)
            print("Basado en la funcion, determine un punto cercano a la raiz")
            a = float(input("Punto cercano: "))
            t = transform(input("Defina la toleracia: "))
            ans = newton_raphson(func_1, a, t, t)
            print_list(ans)
            print(f"y: {func_1(ans[-1])}")

        elif option == 5:
            plot_function(func_1)
            print("Basado en la funcion, determine el rango de busqueda")
            a = float(input("Limite inferior del rango: "))
            b = float(input("Limite superior del rango: "))
            t = transform(input("Defina la toleracia: "))
            ans = secante(func_1, a, b, t, t)
            print_list(ans)
            print(f"{func_1(ans[-1])}")

        elif option == 6:
            print("Hola")

        elif option == 7:
            a = pick_color()
            plot_function(func_1, a)

        elif option == 8:
            finished = True

        else:
            print("Opcion no valida")

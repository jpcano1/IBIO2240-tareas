import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt
import pandas as pd

def plot_function(f, c="#e60000"):
    colors = [c]
    plt.style.use("dark_background")
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey

    fig, ax = plt.subplots()

    x = np.linspace(-5, 5, 1000)
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
    ax.axhline(y=0, color="#1E1F3C")
    plt.show()
    return

def biseccion(f, x0, x1, tolx, tolf):
    x2_prev = x1

    i = 0
    results = []
    while True:
        i += 1
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

    return results

def falsa_posicion(f, x0, x1, tolx, tolf):
    x2_prev = x1

    i = 0
    results = []
    while True:
        i += 1
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

    return results

def punto_fijo(f, g, x1, tolx, tolf):
    pass

def newton_raphson(f, x1, tolx, tolf):
    x2_prev = x1
    i = 0
    results = []
    while True:
        i += 1
        d1_eval = derivative(f, x1)
        x2 = x1 - (f(x1) / d1_eval)
        results.append(x2)

        if np.abs(x2 - x2_prev) <= tolx:
            break

        if np.abs(f(x2)) <= tolf:
            break

        x1 = x2
        x2_prev = x2

    return results

def secante(f, x0, x1, tolx, tolf):
    pass

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

def print_list(a: list):
    for item in a:
        print(f"Aproximacion: {item}")
    return

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
    t = 10**-10

    def f1(x):
        func = x ** 4
        return func

    x0 = -1.
    x1 = 4
    while not finished:
        print_menu()
        option = int(input())
        if option == 1:
            ans = biseccion(f1, x0, x1, t, t)
            print_list(ans)

        elif option == 2:
            ans = falsa_posicion(f1, x0, x1, t, t)
            print_list(ans)

        elif option == 3:
            print("Hola")

        elif option == 4:
            ans = newton_raphson(f1, x1, t, t)
            print_list(ans)

        elif option == 5:
            print("Hola")

        elif option == 6:
            print("Hola")

        elif option == 7:
            a = pick_color()
            plot_function(f1, a)

        elif option == 8:
            finished = True

        else:
            print("Opcion no valida")

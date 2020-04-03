import numpy as np
from sympy import *

def biseccion(f, x0, x1, tolx, tolf):
    x2_prev = x1

    i = 0
    results = []
    while True:
        i += 1
        x2 = (x0 + x1) / 2
        results.append(x2)

        if np.abs(x2 - x2_prev) <= tolx:
            break

        if np.abs(f(x2)) <= tolf:
            break

        if f1(x2) * f1(x0) < 0:
            x1 = x2
        else:
            x0 = x2
    return results

def false_posicion():
    pass

def newton_raphson(f, x1, tolx, toly):
    x = Symbol('x')
    func = f(x)
    d1_func = func.diff(x)
    func = lambdify(x, func)
    d1_func = lambdify(x, d1_func)

    x2_prev = x1

    i = 0
    results = []
    while True:
        i += 1
        x2 = x1 - (func(x1) / d1_func(x1))
        results.append(x2)

        if np.abs(x2 - x2_prev) <= tolx:
            break

        if np.abs(func(x2)) <= toly:
            break

        x1 = x2
        x2_prev = x2

    return results

def print_menu():
    """
        Prints menu on the main method
    """
    print("----------Laboratorio 7----------")
    print("Escoja la opcion: ")
    print("1. Metodo de la biseccion")
    print("2. Metodo de Newton-raphson")
    print("3. Salir")

def print_list(a: list):
    for item in a:
        print(f"Aproximacion: {item}")
    return

if __name__ == "__main__":
    finished = False
    t = 10**-10

    def f1(x):
        func = x ** 2
        return func

    x0 = 0.
    x1 = 1.
    while not finished:
        print_menu()
        option = int(input())
        if option == 1:
            ans = biseccion(f1, x0, x1, t, t)
            print_list(ans)

        elif option == 2:
            ans = newton_raphson(f1, x1, t, t)
            print_list(ans)

        elif option == 3:
            break

import numpy as np
from scipy.misc import derivative

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
    print("7. Salir")

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
            finished = True

        else:
            print("Opcion no valida")

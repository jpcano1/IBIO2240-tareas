import numpy as np
import matplotlib.pyplot as plt

def f3(x1, x2):
    """
    Funcion 1
    @param x1: Primer parametro de la funcion
    @param x2: Segundo parametro de la funcion
    @return: calculo de la funcion en x1 y x2
    """
    return x1 ** 2. + x2 -3.

def f4(x1, x2):
    """
    Funcion 2
    @param x1: Primer parametro de la funcion
    @param x2: Segundo parametro de la funcion
    @return: calculo de la funcion en x1 y x2
    """
    return (x1 - 2.) ** 2. + (x2 + 3.) ** 2. - 4

def plot_function(f1, f2):
    """
    Grafica el contorno de la funcion en dos dimensiones
    @param f1: Primera funcion a ser graficada
    @param f2: Segunda funcion a ser graficada
    @return:
    """
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    x1 = np.linspace(-6, 6, 1000); x2 = np.linspace(-6, 6, 1000)
    x, y = np.meshgrid(x1, x2)
    ax.contour(x, y, f1(x, y), [0])
    ax.contour(x, y, f2(x, y), [1])
    ax.grid(1)
    ax.set(xlim=(-6, 6), ylim=(-6, 6))
    plt.show()

def jacobian_2(x1, x2):
    a = np.zeros((2, 2))
    a[0, 0] = 2 * x1
    a[0, 1] = 1
    a[1, 0] = 2 * (x1 - 2)
    a[1, 1] = 2 * (x2 + 3)
    return a

def root(f1, f2, jacob, x1_0, x2_0):
    """
    Funcion que encuentra las raices de las funciones que entran por parametro.
    @param f1: primera funcion
    @param f2: segunda funcion
    @param jacob: el jacobiano de la funcion
    @param x1_0: el punto de partida en x1
    @param x2_0: el punto de partida en x2
    @return: la raiz de las funciones f1 y f2
    """
    tolx = 10 ** -10
    tolf = tolx

    i = 0

    while True:
        i += 1
        # Calculamos el jacobiano en el punto X0 X1
        A = jacob(x1_0, x2_0)
        b = np.zeros((2, 1))
        b[0] = -f1(x1_0, x2_0)
        b[1] = -f2(x1_0, x2_0)

        # Calculamos el delta.
        delta_x = np.linalg.solve(A, b)

        x1 = np.float(x1_0 + delta_x[0])
        x2 = np.float(x2_0 + delta_x[1])

        # Calculamos la diferencia en las tolerancias para x0 y x1
        if np.abs(x1 - x1_0) <= tolx and np.abs(x2 - x2_0) <= tolx:
            break

        # Calculamos las tolerancias en f(x0, x1)
        if np.abs(f1(x1, x2)) <= tolf and np.abs(f2(x1, x2)) <= tolf:
            break

        x1_0 = x1
        x2_0 = x2

    return x1, x2, i

def print_menu():
    """
    Imprime el menu
    """
    print("----------Laboratorio 8----------")
    print("Escoja la opcion: ")
    print("1. Ejecutar la funcion de intervalo")
    print("2. Salir")

if __name__ == "__main__":
    finished = False

    while not finished:
        print_menu()
        option = int(input())
        if option == 1:
            plot_function(f3, f4)
            inic = float(input("Ingrese un punto: "))
            fin = float(input("Ingrese otro punto: "))
            print(root(f3, f4, jacobian_2, inic, fin))
        elif option == 2:
            finished = True
        else:
            print("Opcion no valida")
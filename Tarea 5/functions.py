import numpy as np
import math
import matplotlib.pyplot as plt

def gauss(matrix, b):
    """
    Auxiliar - Method that calculates the triangular matrix
    through the gaussian method
    @param matrix: the matrix to be computed
    @param b: the vector of the equation system
    @return: the triangular matrix
    """
    matrix = np.concatenate((matrix, b), axis=1)
    n = np.size(matrix, 0)

    for i in range(0, n):
        # We get the 'pivot'
        pivot = matrix[i, i]
        for j in range(i + 1, n):
            # This loop is used to eliminate all the numbers below
            # the pivot without updating the pivot
            fila_aux = (1 / pivot) * matrix[j, i]
            fila_aux = -fila_aux * matrix[i, :]
            # The substraction
            matrix[j, :] += fila_aux
    return matrix

def gauss_backpropagation(matrix, b):
    """
    1 - Method that solves the equation system
    through backpropagation to the gaussian matrix
    @param matrix: the matrix to be computed
    @param b: the vector of the equation system
    @return: the solution vector
    """
    # We get the gaussian matrix
    matrix = gauss(matrix, b)

    n = np.size(matrix, 0)

    # We have this empty array to insert the
    # solution values
    c  = np.zeros((n, 1))
    cont = np.size(matrix[0]) - 1
    for i in range(n-1, -1, -1):
        # We execute this loop to the backpropagation
        x = matrix[i, cont]
        # This dot product is used to eliminate all the numbers we don't have yet
        # (0, 0, 0) * (x1, x2, x3) for each iteration
        y = (x - np.dot(matrix[i][:-1], c)) / matrix[i, i]
        c[i] = y
    return c

def pivots(matrix):
    """
    Auxiliar - Method that allows me to compute the pivots of a matrix
    @param matrix: the matrix to be computed
    @return: the matrix with its pivots
    """
    for i in range(len(matrix)):
        pivote = matrix[i, i]
        matrix[i, :] /= pivote
    return matrix

def gauss_jordan(matrix, b):
    """
    2 - Method that calculates the solution of a equation system
    through the Gauss-Jordan Method
    @param matrix: The matrix to be computed
    @param b: the vector of the equation system
    @return: the vector/matrix of the solution
    """
    # We calculate the gaussian matrix
    matrix = gauss(matrix, b)
    # We calculate the pivots of a matrix
    matrix = pivots(matrix)

    n = np.size(matrix, 0)

    # We execute this loops to eliminate the numbers
    # below and above each pivot in the joint matrix
    for i in range(n - 1, -1, -1):
        # Begins the elimination
        for j in range(i - 1, -1, -1):
            num = matrix[j, i] * matrix[i, :]
            matrix[j, :] -= num
    return matrix[:, n:]

def solution(a):
    """
    Auxiliar - Computes the solution to find the coefficients
    @param a: the array with the points to concatenate
    @return: the solution to the system
    """

    # Creates empty arrays
    matrix = list()
    vector = list()


    for t in a:
        matrix.append(t[0])
        vector.append(t[1])

    matrix = np.array(matrix, dtype=float)
    vector = np.array(vector, dtype=float)

    print("Solucion por medio de gauss-jordan: ")
    a = gauss_jordan(matrix, vector)
    print(a)
    input("Presione intro para continuar...")
    print("Solucion por medio de gauss y backpropagation: ")
    print(gauss_backpropagation(matrix, vector))
    input("Presione intro para continuar...")
    print("Aquí esta la respuesta del paquete linalg: ")
    print(np.linalg.solve(matrix, vector))

    return a

def circle_solution():
    """
    4 - Computes the solution for the points in the circle
    @return: the data needed to plot the circle
    """
    def circle_eq(x, y):
        return [x, y, 1], [-(x ** 2 + y ** 2)]

    a = [circle_eq(-2, 0), circle_eq(-7, 1), circle_eq(5, -1)]

    return solution(a)

def circle_graph(a, b, c):
    """
    4 - Plots the circle given the coefficients
    @param a: the first coefficient calculated
    @param b: the second coefficient
    @param c: the third coefficient
    """
    # We find the radius r
    r = math.sqrt((a / 2)**2 + (b / 2)**2 - c)
    # We find the center i, j
    i, j = -a/2, -b/2

    # Generate the samples
    x = np.linspace(i - r, i + r, 50)
    y = np.linspace(j - r, j + r, 50)

    # Generates coordinates
    X, Y = np.meshgrid(x, y)

    # Defines the function
    F = (X - i) ** 2 + (Y - j) ** 2 - r**2

    # Creates the plot
    fig, ax = plt.subplots(figsize=(8, 8))

    # Graphs the plot
    ax.contour(X, Y, F, [0], colors=["r"])
    ax.set_aspect(1)

    # Generates angles for polar coordinates
    theta = np.linspace(0, 2*np.pi, 50)

    # Generates polar coordinates based on parameter functions
    x = r * np.cos(theta) + i
    y = r * np.sin(theta) + j

    # Plots the points
    ax.plot(x, y, 'o', color="b")

    # Sets the title
    plt.title('Circle graph')

    # The graph's limits
    plt.xlim(-105, 140)
    plt.ylim(-10, 230)

    plt.grid(linestyle='--')
    plt.axvline(x=0, color='grey')
    plt.axhline(y=0, color='grey')

    plt.show()

def polinom_solution():
    """
    5 - Computes the solution for the points in the polinom
    @return: the data needed to plot the polinom
    """
    def polinom_eq(x, y):
        return [x ** 4, x ** 3, x ** 2, x, 1], [y]
    a = [polinom_eq(-2.68, 0),
         polinom_eq(-3.25, 1.15),
         polinom_eq(-4.45, -1.56),
         polinom_eq(-6.25, -2.84),
         polinom_eq(-8.15, 0.23)]

    return solution(a)

def polinom_graph(a, b, c, d, e):
    """
    Plots the polinom given the coefficients
    @param a: first coefficient
    @param b: second coefficient
    @param c: third coefficient
    @param d: fourth coefficient
    @param e: fifth coefficient
    """
    # Creates the data
    x = np.arange(start=-8.15, stop=-2.68, step=0.1, dtype=float)
    f = a * x**4 + b * x**3 + c * x**2 + d * x + e

    # Plots the curve
    plt.plot(x, f, '-', color="r")
    # Plots the points
    plt.plot(x, f, 'o', color="b")
    plt.grid(linestyle="--")

    plt.axvline(x=0, color='grey')
    plt.axhline(y=0, color='grey')

    plt.title('Polinom graph')
    plt.show()

def print_menu():
    """
    Prints menu on the main method
    """
    print("----------Laboratorio 5----------")
    print("Escoja la opcion: ")
    print("1. Método de Gauss")
    print("2. Método de Gauss-Jordan")
    print("3. Justificacion de las soluciones de una matriz")
    print("4. Grafica y resolucion del círculo")
    print("5. Grafica y resolucion del polinomio")
    print("6. Salir")

def generate_mat_vec():
    """
    Generates the respective random matrix and vector
    """
    rango = int(input("Ingrese un numero de rango para la matriz aleatoria y para el vector: "))
    print("Generando matriz aleatoria: ")
    matrix = np.random.rand(3, 3) * rango
    print("Matriz generada: ")
    print(matrix)
    vector = np.random.rand(3, 1) * rango
    print("Vector generado: ")
    print(vector)
    input("Presione intro para continuar...")
    return matrix, vector

if __name__ == '__main__':
    finished = False
    while not finished:
        print_menu()
        option = int(input())

        if option == 1:
            mat, vec = generate_mat_vec()
            print("Solucion por medio de la funcion creada: ")
            print(gauss_backpropagation(mat, vec))
            print("Aquí esta la respuesta del paquete linalg: ")
            print(np.linalg.solve(mat, vec))
        elif option == 2:
            mat, vec = generate_mat_vec()
            print("Solucion por medio de la funcion creada: ")
            print(gauss_jordan(mat, vec))
            print("Aquí esta la respuesta del paquete linalg: ")
            print(np.linalg.solve(mat, vec))
            input("Presione intro para continuar...")
            print("Inversa de la matriz por medio de la funcion creada: ")
            print(gauss_jordan(mat, np.identity(3)))
            print("Aquí esta la respuesta del paquete linalg: ")
            print(np.linalg.inv(mat))
        elif option == 3:
            print("Aqui va la solucion")
        elif option == 4:
            a, b, c = circle_solution()
            input("Presione intro para continuar...")
            circle_graph(a, b, c)
        elif option == 5:
            a, b, c, d, e = polinom_solution()
            input("Presione intro para continuar...")
            polinom_graph(a, b, c, d, e)
        elif option == 6:
            finished = True
        else:
            print("Opcion no valida")

    print("Hasta pronto")

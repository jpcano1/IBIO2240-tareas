import numpy as np

def gauss(matrix, b):
    """
    Method that calculates the triangular matrix
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
    Method that solves the equation system
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
    Method that allows me to compute the pivots of a matrix
    @param matrix: the matrix to be computed
    @return: the matrix with its pivots
    """
    for i in range(len(matrix)):
        pivote = matrix[i, i]
        matrix[i, :] /= pivote
    return matrix

def gauss_jordan(matrix, b):
    """
    Method that calculates the solution of a equation system
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

def circle_eq(x, y):
    return [x, y, 1], -(x ** 2 + y ** 2)

def circle_solution():
    matrix = list()
    vector = list()

    a = [circle_eq(-2, 0), circle_eq(-7, 1), circle_eq(5, -1)]
    for t in a:
        matrix.append(t[0])
        vector.append(t[1])

    matrix = np.array(matrix, dtype=float)
    vector = np.array([vector], dtype=float).T

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

def circle_points(coefficients):
    """"""

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
            circle_solution()

        elif option == 6:
            finished = True
        else:
            print("Opcion no valida")

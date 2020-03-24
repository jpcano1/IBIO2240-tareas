import numpy as np
import matplotlib.pyplot as plt
import struct as st

def gauss_jordan(matrix, b):
    """
    1 - Method that calculates the solution of a equation system
    through the Gauss-Jordan Method
    @param matrix: The matrix to be computed
    @param b: the vector of the equation system
    @return: the vector/matrix of the solution
    """
    def gauss(mat, b):
        """
        Auxiliar - Method that calculates the triangular matrix
        through the gaussian method
        @param mat: the matrix to be computed
        @param b: the vector of the equation system
        @return: the triangular matrix
        """
        mat = np.concatenate((mat, b), axis=1)
        n = np.size(mat, 0)

        for i in range(0, n):
            # We get the 'pivot'
            pivot = mat[i, i]
            for j in range(i + 1, n):
                # This loop is used to eliminate all the numbers below
                # the pivot without updating the pivot
                fila_aux = (1 / pivot) * mat[j, i]
                fila_aux = -fila_aux * mat[i, :]
                # The substraction
                mat[j, :] += fila_aux
        return mat

    def pivots(mat):
        """
        Auxiliar - Method that allows me to compute the pivots of a matrix
        @param mat: the matrix to be computed
        @return: the matrix with its pivots
        """
        for i in range(len(mat)):
            pivote = mat[i, i]
            mat[i, :] /= pivote
        return mat

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


def estimate_b0_b1(x, y):
    """
    Estimates the values b_0 and b_0 from the linear regression
    @param x:
    @param y:
    @return:
    """
    n = np.size(x)

    # Obtenemos los promedios de x y de y
    m_x, m_y = np.mean(x), np.mean(y)

    # Calcular sumatoria de XY y mi sumatoria de XX
    sumatoria_xy = np.sum((x - m_x) * (y - m_y))
    sumatoria_xx = np.sum((x - m_x) ** 2)

    # Coeficientes de regresión
    b_1 = sumatoria_xy / sumatoria_xx
    b_0 = m_y - b_1 * m_x

    return b_0, b_1

def read_files():
    file = open("Lab-Reg-X.bin", "rb")
    var1 = file.read()
    x = st.unpack("d"*int(len(var1)/8), var1)
    file.close()
    file = open("Lab-Reg-Y.bin", "rb")
    var1 = file.read()
    y = st.unpack("d"*int(len(var1)/8), var1)
    x = np.array(x)
    y = np.array(y)
    return x, y

def plot_regression():
    x, y = read_files()

    b = estimate_b0_b1(x, y)

    plt.plot(x, y, "or")

    y_prediction = b[0] + b[1] * x

    plt.plot(x, y_prediction, "-")

    # Etiquetado
    plt.xlabel("x, Variable independiente")
    plt.ylabel("y, Variable dependiente")
    plt.axvline(x=0, color="grey")
    plt.axhline(y=0, color="grey")
    plt.grid(linestyle="--")
    plt.show()

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

def print_menu():
    """
    Prints menu on the main method
    """
    print("----------Laboratorio 5----------")
    print("Escoja la opcion: ")
    print("1. Método de Gauss-Jordan")
    print("2. Justificacion de las soluciones de la regresion lineal")
    print("3. Grafica y resolucion de la regresion lineal")
    print("4. Ejercicio del libro.")
    print("5. Salir")

if __name__ == "__main__":
    finished = False

    while not finished:
        print_menu()
        option = int(input())

        if option == 1:
            a, b = generate_mat_vec()
            print("Solucion por medio de la funcion creada: ")
            print(gauss_jordan(a, b))
            print("Aquí esta la respuesta del paquete linalg: ")
            print(np.linalg.solve(a, b))
            input("Presione intro para continuar...")
            print("Inversa de la matriz por medio de la funcio  n creada: ")
            print(gauss_jordan(a, np.identity(3)))
            print("Aquí esta la respuesta del paquete linalg: ")
            print(np.linalg.inv(a))

        elif option == 2:
            print("Justificacion")

        elif option == 3:
            plot_regression()

        elif option == 4:
            print("Punto 4")

        elif option == 5:
            finished = True

        else:
            print("Opcion no valida")

    print("Hasta pronto")



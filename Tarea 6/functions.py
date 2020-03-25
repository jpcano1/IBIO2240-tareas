import numpy as np
import matplotlib.pyplot as plt
import struct as st
import pandas as pd

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

    return b_1, b_0

def read_excel_files():
    file = pd.read_excel("clean_data.xlsx")
    data_men = np.array(file.iloc[:, :2].dropna())
    data_women = np.array(file.iloc[:, ::2].dropna())
    return (data_men[:, 0],
            data_men[:, 1],
            data_women[:, 0],
            data_women[:, 1])

def read_binary_files():
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

def plot_data_competition(x1, y1, x2, y2):
    b_1, b_0 = estimate_b0_b1(x1, y1)
    xf = np.arange(x1[0], 2160, 0.1)
    y_prediction = b_1 * xf + b_0
    plt.plot(x1, y1, "or")
    plt.plot(xf, y_prediction, "-r", label="Men")

    b_1, b_0 = estimate_b0_b1(x2, y2)
    y_prediction = b_1 * xf + b_0
    plt.plot(x2, y2, "ob")
    plt.plot(xf, y_prediction, "-b", label="Women")
    plt.legend(loc='upper right')
    plt.show()

def plot_regression(x, y, x_lim=21, y_lim=150, x_title="X, variable independiente", y_title="Y, variable dependiente"):
    fig, ax = plt.subplots(nrows=2)
    fig.tight_layout(pad=3)

    xf = np.arange(x[0], x[-1], 0.1)
    b_1, b_0 = estimate_b0_b1(x, y)

    y_prediction = b_1 * xf + b_0
    ax[0].plot(x, y, "or")
    ax[0].plot(xf, y_prediction, "-")
    ax[0].set_title("Regresion sin Polyfit")

    p = np.polyfit(x, y, 1)
    y_prediction = p[0] * xf + p[1]
    ax[1].plot(x, y, "og")
    ax[1].plot(xf, y_prediction, "-")
    ax[1].set_title("Regresion con Polyfit")

    for axis in ax:
        axis.grid(linestyle="--")
        axis.set_ylabel(y_title)
        axis.set_xlabel(x_title)
        axis.set_xlim(0, x_lim)
        axis.set_ylim(0, y_lim)

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
            data_x, data_y = read_binary_files()
            print("Leyendo los datos binarios")
            input("Presione intro para continuar...")
            plot_regression(data_x, data_y)

        elif option == 4:
            x1, y1, x2, y2 = read_excel_files()
            plot_data_competition(x1, y1, x2, y2)

        elif option == 5:
            finished = True

        else:
            print("Opcion no valida")

    print("Hasta pronto")
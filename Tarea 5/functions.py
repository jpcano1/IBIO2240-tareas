import numpy as np

def gauss(matrix, b):
    matrix = np.concatenate((matrix, b), axis=1)
    n = np.size(matrix, 0)

    for i in range(0, n):
        pivot = matrix[i, i]
        for j in range(i + 1, n):
            fila_aux = (1 / pivot) * matrix[j, i]
            fila_aux = -fila_aux * matrix[i, :]
            matrix[j, :] += fila_aux
    return matrix

def gauss_backpropagation(matrix, b):
    matrix = gauss(matrix, b)

    n = np.size(matrix, 0)

    c  = np.zeros((n, 1))
    cont = np.size(matrix[0])-1
    for i in range(n-1, -1, -1):
        x = matrix[i, cont]
        y = (x - np.dot(matrix[i][:-1], c))/matrix[i, i]
        c[i] = y

    return c

def pivots(matrix):
    for i in range(len(matrix)):
        pivote = matrix[i, i]
        matrix[i, :] /= pivote
    return matrix

def gauss_jordan(matrix, b):
    matrix = gauss(matrix, b)
    matrix = pivots(matrix)

    n = np.size(matrix, 0)

    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            num = matrix[j, i] * matrix[i, :]
            matrix[j, :] -= num
    return matrix[:, n:]

def print_menu():
    print("----------Laboratorio 5----------")
    print("Escoja la opcion: ")
    print("1. Método de Gauss")
    print("2. Método de Gauss-Jordan")
    print("6. Salir")

def generate_mat_vec():
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
        elif option == 6:
            finished = True
        else:
            print("Opcion no valida")

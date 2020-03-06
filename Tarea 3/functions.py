##
# Primero
def productory(a):
    """
    Calculates the productory of an array
    @param a: the array
    @return: the multiplication of the elements
    """
    result = 1
    for i in a:
        result *= i
    return result
##
# Segundo
##
# Tercero
def is_prime(num):
    """
    Verifies if a number is prime
    @param num: the number to be verified
    @return: the verification
    """
    prime = False
    if (num % 2 != 0
        and num % 3 != 0
        and num % 5 != 0
        and num % 7 != 0
        and num != 1) or (num in [2, 3, 5, 7]) :
        prime = True

    return prime

##
# Cuarto
def palindrome(number):
    """
    Verifies if a number is palidrome
    @param number: the number to be verified
    @return: the verification of the number
    """
    number = str(number)
    pali = True
    i = 0
    aux = (len(number) / 2) - 1 if len(number) % 2 == 0 else (len(number) - 1) / 2
    while pali and i <= aux:
        if number[i] != number[-i-1]:
            pali = False
        i += 1
    return pali
##
# Quinto
def is_fibonacci(num):
    """
    Verifies if a number belongs to the fibonacci series
    @param num: the number to be operated
    @return: the verification of the number
    """
    if num == 0:
        return True
    a = 0
    b = 1
    c = a + b
    is_fib = False

    while num >= c:
        if num == c:
            is_fib = True
        a = b
        b = c
        c = a + b

    return is_fib
##
# Sexto
def mean_matrix(matrix, mode: int):
    """
    Computes the mean of a matrix by row or by column
    @param matrix: the matrix to be operated
    @param mode: whith this, we know
    if we have to calculate a row or a column
    @return: an array with the mean per row/column
    @type: list
    """
    means = list()
    if mode == 1:
        for row in matrix:
            means.append(sum(elem for elem in row)/len(row))
    elif mode == 2:
        for i in range(len(matrix[0])):
            suma = 0
            for j in range(len(matrix)):
                suma += matrix[j][i]
            means.append(suma / len(matrix))
    return means

print(mean_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], 1))
##
# Septimo
def max_matrix(matrix, mode):
    """
    Computes the max number of a matrix by row or by column
    @param matrix: the matrix to be operated
    @param mode: whith this, we know
    if we have to calculate a row or a column
    @return: an array with the max per row/column
    @type: list
    """
    maxes = list()
    if mode == 1:
        for row in matrix:
            maxes.append(max(elem for elem in row))
    elif mode == 2:
        for i in range(len(matrix[0])):
            aux = 0
            for j in range(len(matrix)):
                if matrix[j][i] > aux:
                    aux = matrix[j][i]
            maxes.append(aux)
    return maxes
print(max_matrix([[1, 2, 3], [7, 9, 1], [4, 1, 4], [3, 4, 1]], 2))
##
# Octavo
def min_matrix(matrix, mode):
    """
    Computes the min of a matrix by row or by column
    @param matrix: the matrix to be operated
    @param mode: whith this, we know
    if we have to calculate a row or a column
    @return: an array with the min per row/column
    @type: list
    """
    mins = list()
    if mode == 1:
        for row in matrix:
            mins.append(min(elem for elem in row))
    elif mode == 2:
        for i in range(len(matrix[0])):
            aux = matrix[0][i]
            for j in range(len(matrix)):
                if matrix[j][i] < aux:
                    aux = matrix[j][i]
            mins.append(aux)
    return mins
print(min_matrix([[1, 2, 3], [7, 9, 1], [4, 1, 4], [3, 4, 1]], 1))
##
# noveno
def sum_matrix(mat1, mat2):
    """
    Computes the sum element by element of two matrixes
    @param mat1: the first matrix to be summated
    @param mat2: the second matrix to be summated
    @return: the summation of both matrixes
    """
    result_mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        result_mat.append(row)
    return result_mat
##
# Decimo
def prod_matrix(mat1, mat2):
    """
    Computes the multiplication element by element of two matrixes
    @param mat1: the first matrix to be multiplied
    @param mat2: the second matrix to be multiplied
    @return: the product of both matrixes
    """
    result_mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] * mat2[i][j])
        result_mat.append(row)
    return result_mat

##
# 11
import numpy as np
def mean_array(matrix, mode):
    """
    Computes the mean of a matrix by row or by column using numpy
    @param matrix: the matrix to be computed
    @param mode: with this we know if we have to compute
    by row or by column
    @return: the mean of the array
    """
    if mode == 0:
        return np.mean(a=matrix, axis=0)
    else:
        return np.mean(a=matrix, axis=1)

def max_array(matrix, mode):
    """
    Computes the max number of a matrix by row or by column using numpy
    @param matrix: the matrix to be operated
    @param mode: whith this, we know
    if we have to calculate a row or a column
    @return: an array with the max per row/column
    @type: list
    """
    if mode == 0:
        return np.max(a=matrix, axis=0)
    else:
        return np.max(a=matrix, axis=1)

def min_array(matrix, mode):
    """
    Computes the min number of a matrix by row or by column using numpy
    @param matrix: the matrix to be operated
    @param mode: whith this, we know
    if we have to calculate a row or a column
    @return: an array with the min per row/column
    @type: list
    """
    if mode == 0:
        return np.min(a=matrix, axis=0)
    else:
        return np.min(a=matrix, axis=1)

def sum_array(matrix1, matrix2):
    """
    Computes the sum element by element of two matrixesusing numpy
    @param matrix1: the first matrix to be summated
    @param matrix2: the second matrix to be summated
    @return: the summation of both matrixes
    """
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    return matrix1 + matrix2

def multiply_array(matrix1, matrix2):
    """
    Computes the multiplication element by element of two matrixes
    using numpy
    @param matrix1: the first matrix to be multiplied
    @param matrix2: the second matrix to be multiplied
    @return: the product of both matrixes
    """
    return np.array(matrix1) * np.array(matrix2)

##
import numpy as np
import matplotlib.pyplot as plt

def sinusoidal_functions():
    """
    Calulates the sin function with numpy changing its frequency
    then, it graphs it using subplots
    @return: None
    """
    x = np.linspace(0, 10, num=1000)
    fig, ax = plt.subplots(nrows=10, figsize=(10, 30))
    fig.tight_layout(pad=2)
    for i in range(10):
        ax[i].plot(x, np.sin(2*np.pi*(i+1)*x))
        ax[i].set_title(f"Función con {i+1} hz")
        ax[i].grid(True)
    plt.show()
    return

sinusoidal_functions()
##
import numpy as np
import matplotlib.pyplot as plt

def histogram_uniform():
    """
    Creates an array with random values on an uniform distribution
    and graphs them to se their behavior
    @return: None
    """
    array = np.random.rand(10000)
    fig, ax = plt.subplots(5, figsize=(5, 20))
    fig.tight_layout(pad=2)
    for i in range(5):
        ax[i].hist(array, bins=(i+1)*10, color="g")
        ax[i].set_title(f"Histogram for {(i+1)*10} partitions")
    plt.show()
    return

histogram_uniform()
##
import numpy as np
import matplotlib.pyplot as plt

def histogram_normal():
    """
    Creates an array with random values on a normal distribution
    and graphs them to se their behavior
    @return: None
    """
    array = np.random.normal(size=10000)
    fig, ax = plt.subplots(5, figsize=(5, 20))
    fig.tight_layout(pad=2)
    for i in range(5):
        ax[i].hist(array, bins=(i+1)*10, color="r")
        ax[i].set_title(f"Histogram for {(i+1)*10} partitions")
    plt.show()
    return

histogram_normal()
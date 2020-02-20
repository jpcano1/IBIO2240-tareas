##
# Primero
def productory(a: list):
    result = 1
    for i in a:
        result *= i
    return result
##
# Segundo
def factorial(x: int):
    if x < 0:
        raise Exception("Not a positive number")
    if x == 1 or x == 0:
        return 1
    else:
        return x*factorial(x-1)

print(factorial(10))
##
# Tercero
def is_prime(num):
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
def mean_matrix(matrix, mode):
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
    result_mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        result_mat.append(row)
    return result_mat

##
# 11
import numpy as np
def mean_array(matrix, mode):
    if mode == 0:
        return np.mean(a=matrix, axis=0)
    else:
        return np.mean(a=matrix, axis=1)
def max_array(matrix, mode):
    if mode == 0:
        return np.max(a=matrix, axis=0)
    else:
        return np.max(a=matrix, axis=1)

def min_array(matrix, mode):
    if mode == 0:
        return np.min(a=matrix, axis=0)
    else:
        return np.min(a=matrix, axis=1)

def sum_array(matrix1, matrix2):
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    return matrix1 + matrix2
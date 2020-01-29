from datetime import datetime as dt

##############
def absolute(x):
    """
        Calculates the absolute value of a variable
        :param x: the variable to be calculated
        :return: The abs value
    """
    if x < 0:
        return -x
    return x

#################
import math

def circle_radius(radius) -> float:
    """
        1. Calculates the circle area
        :param radius: the radius of a circle
        :return: the circle's area
    """
    return math.pi * (radius**2)

############
def inverted_name(name) -> str:
    """
        2 - Prints the inverted name
        :param name: the name to be inverted
        :return: the inverted name
    """
    lengthName = len(name)
    slicedString = lengthName[lengthName::-1]
    return slicedString

##############
def terms(num):
    """
        3 - Calculates num + num*num + num*num*num
        :param num: The number tranform
        :return: The calculated number
    """
    return num + num**2 + num**3

# Cuarto punto pendiente
def dates_difference(date_1, date_2=dt.now()):
    pass

###########
def volume(radius):
    """
        5 - Calculates the volume of an sphere
        :param radius: the radius of the sphere
        :return: the sphere's volume
    """
    return (math.pi*radius**3)*4/3

###########
def difference(num) -> float:
    """
        6 - Returns the difference of the num with 12
        :param num: the num to be substracted
        :return: the result of the substraction
    """
    sub = 12 - num

    if sub < 0:
        return math.fabs(sub)
    else:
        return sub

###########
def verification(num):
    """
        7 - Return tghe verification of a number
        :param num: The number to be verified
    """
    if num < 100:
        return "El número es menor que 100"
    elif num in range(100, 1001):
        return "El numero esta entre 100 y 1000"
    elif num in range(1000, 2001):
        return "El numero está entre 1000 y 2000"
    elif num > 2000:
        return "El numero es mayor a 2000"

#######
def pair_verification(num):
    """
        8 - Verifies if a number is an odd or and even number
        :param num: The number to be verified
    """
    if num % 2 == 0:
        return "The number is even"
    else:
        return "the number is odd"

############
def num_in_array(num, array):
    """
        9 - Method that looks for the number of times
        a number appears on an array
        :param array: the array to be analyzed
        :param num: The num to looked for
        :return: The number of times the number appears
    """
    cont = 0
    for i in range(len(array)):
        if num == array[i]:
            cont+=1
    return cont

c = []
b = input("Ingrese un número, cuando no quiera meter más números, escriba 'parar': ")
while b != "parar":
    b = float(b)
    c.append(b)
    b = input()

b = float("Ingrese el número que quiere buscar: ")
print(num_in_array(b, c))

########
def last_n_numbers(num, word="Hola mundo"):
    """
        10 - method that returns the last n characters in of an array
        :param num: the last n characters in the array
        :param word: The character to be cut
        :return: the string cut
    """
    return word[num: len(word)]

word = input("Escriba una palabra: ")
last = int(input("Escriba el número de las últimas n letras que desea ver: "))
print(last_n_numbers(last, word))

##############
def sumation(num1, num2, num3):
    """
        11 - Function that calculates the sum of three numbers
        :param num1: the first number
        :param num2: the second number
        :param num3: the third number
        :return: the sum
    """
    if (num1==num2) and (num2==num3):
        return 0
    return num1 + num2 + num3

#########
def prime_numbers(num):
    """
        16 - Looks for the n prime numbers
        :param num: The number of primes we want to show
        :return: an array of primes
    """

##############
def minimum(array):
    """
        19 - Finds the minimum in an array
        :param array: the array to be examined
        :return: the minimum in the array
    """
    a = array[0]
    for i in array:
        if i < a:
            a = i
    return a

c = []
b = input("Ingrese un número, cuando no quiera meter más números, escriba 'parar': ")
while b != "parar":
    b = float(b)
    c.append(b)
    b = input()

print(minimum(c))

#####################
def average(array):
    """
        20 - Calculates the average in an array
        :param array: the array to be examined
        :return: the average in the array
    """
    cont = 0
    for i in array:
        cont += i
    return cont / len(array)

def desv_est(array):
    """
        21 - Calculates the varianze of an array
        :param array: the array to be examined
        :return: the variance of the array
    """
    a = average(array)
    cont = 0
    for i in array:
        cont += (i - a)**2
    return (cont / len(array))**(1/2)

c = []
b = input("Ingrese un número, cuando no quiera meter más números, escriba 'parar': ")
while b != "parar":
    b = float(b)
    c.append(b)
    b = input()

#############
def numbers_in_array_7(array):
    """
        25 - Calculates the number on numbers that are multiples of 7 in a array
        :param array: the array to be examined
        :return: the number of numbers
    """
    cont = 0
    for i in array:
        if i % 7 == 0:
            cont += 1

c = []
b = input("Ingrese un número, cuando no quiera meter más números, escriba 'parar': ")
while b != "parar":
    b = float(b)
    c.append(b)
    b = input()

###########
def transpose_matrix(matrix):
    """
        30 - Method that allows me to transpose a matrix
        without using any library
        :param matrix: the matrix to be transposed
        :return: the matrix transposed
    """
    for i in range(len(matrix) - 1):
        for j in range(1, len(matrix) - i):
            a = matrix[i][i + j]
            matrix[i][j + i], matrix[i + j][i] = matrix[i + j][i], a
    return matrix
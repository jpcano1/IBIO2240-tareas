from datetime import datetime as dt

##############
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

def to_int(array):
    cadena = []
    for i in array:
        cadena.append(int(i))
    return cadena

def dates_difference(date_1, date_2):
    """
        4 - Calculates the difference (in days) between two dates
        :param date_1: the first date
        :param date_2: the second date
        :return: the difference between the dates
    """
    date_1 = to_int(date_1.split('-'))
    date_2 = to_int(date_2.split('-'))
    days_1 = (date_1[2]*12 + date_1[1])*30 + date_1[0]
    days_2 = (date_2[2]*12 + date_2[1])*30 + date_2[0]
    diff = days_2 - days_1
    return absolute(diff)

print(dates_difference(date_1="1-1-2020", date_2="30-1-2019"))

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
def summation(num1, num2, num3):
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
def summation_2(num1, num2):
    """
        12 - Function that calculates the sum of two numbers
        :param num1: First number to be summated
        :param num2: Second number to be summated
        :return: The summation of te two numbers
    """
    a = num1 + num2

    if a in range(15, 21):
        return 20
    return a

###########
def operation(num1, num2):
    """
        13 - Function that returns a certain operation between
        two numbers
        :param num1: The first number to be operated
        :param num2: the second number to be operated
        :return: the operation between the numbers
    """
    return (num1 + num2)**2

##########
def euclidean_distance(x1, y1, x2, y2):
    """
        14 - This function calculates the euclidean function
        for two points
        :param x1: x coordinate of the first point
        :param y1: y coordinate of the first point
        :param x2: x coordinate of the second point
        :param y2: y coordinate of the second point
        :return: The distance of between the two points
    """
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    return (x + y)**(1/2)

#########
def seconds_to_date(number):
    """
        15 - Function that allows me to convert a number of seconds to a date
        :param number: the seconds to convert
        :return: the seconds converted
    """
    secs = int(number % 60)
    number = (number-secs) / 60
    mins = int(number % 60)
    number = (number - mins) / 60
    hours = int(number % 24)
    days = int((number - hours) / 24)
    return days, hours, mins, secs

num = int(input("Ingrese un número de segundos"))
print(seconds_to_date(num))

#########
def prime_numbers(num):
    """
        16 - Looks for the n prime numbers
        :param num: The limit of primes we want to show
        :return: an array of primes
    """
    array = []
    if num >= 2:
        array.append(2)

        for i in range(2, num+1):
            root = int(i**(1/2))
            j = 0
            while array[j] < root and (i % array[j] != 0 or array[j] == 1):
                j += 1
            if i % array[j] != 0 or array[j] == 1:
                array.append(i)
    return array

print(prime_numbers(1000))

###########
def summation_3(n):
    """
        17 - Function that allows me to sum all the number from 1 to n
        :param n: the last number to be summated
        :return: the sum of all those numbers
    """
    cont = 1
    for i in (n+1):
        cont += i
    return cont

###############
def maximum(array):
    """
        18 - Finds the maximum in an array
        :param array: the array to be examined
        :return: the maximum in the array
    """
    a = array[0]
    for i in array:
        if i > a:
            a = i
    return a

c = []
b = input("Ingrese un número, cuando no quiera meter más números, escriba 'parar': ")
while b != "parar":
    b = float(b)
    c.append(b)
    b = input()

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
    cont = sum(num for i in array)
    return float(cont / len(array))

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

############
def bubbleSort(array):
    """
        Orders an array ascendently
        :param array: The array to be ordered
        :return: the order array
    """
    n = len(array)
    contador = 0
    for i in reversed(range(1, n + 1)):
        for j in range(0, i - 1):
            contador += 1
            c1 = array[j]
            c2 = array[j + 1]
            if c1 > c2:
                array[j] = c2
                array[j + 1] = c1
    return array

def median(array):
    """
        22 - Finds the median of an array
        :param array: the array to be examined
        :return: the median of the array
    """
    ordered_array = bubbleSort(array)
    if len(ordered_array) % 2 != 0:
        index = int((len(ordered_array)-1)/2)
        return ordered_array[index]
    else:
        index1 = int((len(ordered_array)-1)/2)
        index2 = int((len(ordered_array)+1)/2)
        result = (ordered_array[index1] + ordered_array[index2]) / 2
        return result

###########
def mode(array):
    """
        23 - Function that allows me to calculate the mode of an array of numbers
    :param array: the array to be examined
    :return:
    """
    result = array.count(array[0])
    for i in array:
        if array.count(i) > result:
            result = i
    return int(result)

c = []
b = input("Ingrese un número, cuando no quiera meter más números, escriba 'parar': ")
while b != "parar":
    b = float(b)
    c.append(b)
    b = input()
print(mode(c))

############
def sort(array):
    """
        24 - Function that allows me to order an array
        from the maximum to the minimum using the Insert Sort Algorithm
        :param array: the array to be ordered
        :return: the array sorted
    """
    n = len(array)
    contador = 0
    for i in range(1, n):
        nuevo = array[i]
        for j in reversed(range(1, i + 1)):
            contador += 1
            otro = array[j - 1]
            if otro < nuevo:
                array[j] = otro
                array[j - 1] = nuevo
    return array
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
def assign_numbers(rows, columns, n):
    """
        26 - Assigns a number to a matrix of dimentions rown*columns
        :param rows: the rows of the matrix
        :param columns: the columns of the matrix
        :param n: the number to be assigned
        :return: the resulting matrix
    """
    a = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(n)
        a.append(row)
    return a

###########
def sum_primary_diagonal(matrix):
    """
        27 - Calculates the elements of the primary diagonal
        :param matrix: the matrix that's going to be examined
        :return: the sum of the elements of the primary diagonal
    """
    cont = 0
    for i in range(len(matrix)):
        cont += matrix[i][i]
    return cont

############
def sum_secondary_diagonal(matrix):
    """
        28 - Calculates the elements of the secondary diagonal
        :param matrix: the matrix that's going to be examined
        :return: the sum of the elements of the secondary diagonal
    """
    cont = 0
    i = 0
    j = len(matrix) - 1
    while i < len(matrix) and j >= 0:
        cont += matrix[i][j]
        i += 1
        j -= 1
    return cont

###########
def sum_matrix(mat1, mat2):
    """
        29 - Function that allows me to sum two matrixes of NxN
        :param mat1: the first matrix to be summated
        :param mat2: the second matrix to be summated
        :return: the resulting matrix of the sum
    """
    result_mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        result_mat.append(row)
    return result_mat

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
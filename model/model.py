import math
from datetime import datetime as dt

class Functions:

    def __init__(self):
        pass

    @staticmethod
    def circle_radius(radius) -> float:
        """
            1. Calculates the circle area
            :param radius: the radius of a circle
            :return: the circle's area
        """
        return math.pi * radius**2

    @staticmethod
    def inverted_name(name) -> str:
        """
            2 - Prints the inverted name
            :param name: the name to be inverted
            :return: the inverted name
        """
        lengthName = len(name)
        slicedString = lengthName[lengthName::-1]
        return slicedString

    @staticmethod
    def terms(num):
        """
            3 - Calculates num + num*num + num*num*num
            :param num: The number tranform
            :return: The calculated number
        """
        return num + num**2 + num**3

    # Cuarto punto pendiente
    @staticmethod
    def dates_difference(date_1, date_2=dt.now()):
        pass

    @staticmethod
    def volume(radius):
        """
            5 - Calculates the volume of an sphere
            :param radius: the radius of the sphere
            :return: the sphere's volume
        """
        return (math.pi*radius**3)*4/3

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def pair_verification(num):
        """
            8 - Verifies if a number is an odd or and even number
            :param num: The number to be verified
        """
        if num % 2 == 0:
            return "The number is even"
        else:
            return "the number is odd"

    @staticmethod
    def num_in_array(num):
        # Pendiente
        pass

    @staticmethod
    def last_n_numbers(num):
        """  """
        

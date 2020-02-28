##
# Primero
def _is_fib_aux(num, fib1, fib2):
    """
    Auxiliar recursive function for fibonacci's verification
    @param num: the number to be verified
    @param fib1: the fibonacci number
    @param fib2: the fibonacci number
    @return: a boolean with the verification of the number
    @rtype: bool
    """
    c = fib1 + fib2
    if num == fib1 or num == fib2 or num == c:
        return True
    elif c > num:
        return False
    else:
        return _is_fib_aux(num, fib2, c)

def is_fib(num):
    """
    Validates a number belongs to the fibonacci series
    @param num: the number to be verified
    @return: the verification of the number
    @rtype: bool
    """
    return _is_fib_aux(num, 0, 1)
##
# Segundo

##
# Tercero
import math
def taylor_expo(x, n):
    if n == 0:
        return 1
    else:
        a = x**n/(math.factorial(n))
        b = taylor_expo(x, n-1)
        return a + b

taylor_expo(7, 100)
##
# Cuarto
import math
import numpy as np

def taylor_sin(x, n):
    if n == 0:
        return x
    else:
        a = ((-1)**n)/(math.factorial(2*n+1))
        b = x**(2*n+1)
        c = a*b
        return c + taylor_sin(x, n-1)
taylor_sin(np.pi/2, 100)
##
# Quinto
import math
import numpy as np

def taylor_cos(x, n):
    if n == 0:
        return 1
    else:
        a = ((-1)**n)/(math.factorial(2*n))
        b = x**(2*n)
        c = a*b
        return c + taylor_cos(x, n-1)

taylor_cos(np.pi, 50)
##
# Sexto

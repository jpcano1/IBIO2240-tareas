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

##
# Noveno
import numpy as np
import struct as st
var1 = np.random.randint(low=-10, high=10, size=1000)
file = open("FileBinInt16.bin", "wb")
var2 = st.pack("h"*int(len(var1)), *var1)
var3 = file.write(var2)
file.close()
##
# Decimo
import struct as st
import matplotlib.pyplot as plt
file = open("FileBinInt16.bin", "rb")
var1 = file.read()
var2 = st.unpack("h"*int(len(var1)/2), var1)
file.close()
plt.hist(var2, bins=30)
plt.show()
##
# 11
import numpy as np
import struct as st
var1 = np.random.uniform(-1, 1, 1000)
file = open("FileBinDouble.bin", "wb")
var2 = st.pack("d"*int(len(var1)), *var1)
var3 = file.write(var2)
file.close()
##
# 12
import struct as st
import matplotlib.pyplot as plt
file = open("FileBinDouble.bin", "rb")
var1 = file.read()
var2 = st.unpack("d"*int(len(var1)/8), var1)
file.close()
plt.hist(var2, bins=30)
plt.show()

##
# 13
import struct as st
import numpy as np

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

def read_data():
    file = open("File-214.bin", "rb")
    var1 = file.read()
    var2 = st.unpack("I"*int(len(var1)/4), var1)
    file.close()
    return var2

def write_data(data):
    file = open("File-214.bin", "wb")
    var1 = st.pack("Q"*int(len([data])), *[data])
    var2 = file.write(var1)
    file.close()
    return
i = 0
for num in read_data():
    if is_fib(num):
        i += 1
write_data(i)
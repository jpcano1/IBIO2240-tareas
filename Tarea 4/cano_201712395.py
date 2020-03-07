##
# Primero
def is_fib(num):
    """
    Validates a number belongs to the fibonacci series
    @param num: the number to be verified
    @return: the verification of the number
    @rtype: bool
    """

    def _is_fib_aux(x, fib1, fib2):
        """
        Auxiliar recursive function for fibonacci's verification
        @param x: the number to be verified
        @param fib1: the fibonacci number
        @param fib2: the fibonacci number
        @return: a boolean with the verification of the number
        @rtype: bool
        """
        c = fib1 + fib2
        if x == fib1 or x == fib2 or x == c:
            return True
        elif c > x:
            return False
        else:
            return _is_fib_aux(x, fib2, c)

    return _is_fib_aux(num, 0, 1)
##
# Segundo

def is_square(x):
    """
    Validates a number belongs to the quadratic series
    @param x: the number to be verified
    @return: the verification of the number
    @rtype: bool
    """

    def is_square_aux(x, square):
        """
        Auxiliar recursive function for quadratic's verification
        @param x: the number to be verified
        @param square: the quadratic number
        @return: a boolean with the verification of the number
        @rtype: bool
        """
        if square ** 2 == x:
            return True
        elif square ** 2 > x:
            return False
        else:
            return is_square_aux(x, square + 1)

    return is_square_aux(x, 0)
##
# Tercero

def taylor_expo(x, n):
    """
    Computes the taylor series for the exponential function
    @param x: The number whose exponential it's gonna be computed
    @param n: The number of iterations
    @return: the aproximation for the exponential of 'x'
    """

    def factorial(x: int):
        """
        Calculates the factorial of an integer
        @param x: the integer to be operated
        @return: the factorial of the number
        """
        if x < 0:
            raise Exception("Not a positive number")
        if x == 1 or x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    if n == 0:
        return 1
    else:
        a = x**n/(factorial(n))
        b = taylor_expo(x, n-1)
        return a + b
##
# Cuarto
def taylor_sin(x, n):
    """
    Computes the taylor series for the sine function
    @param x: The number whose sine it's gonna be computed
    @param n: The number of iterations
    @return: the aproximation for the sine of 'x'
    """

    def factorial(x: int):
        """
        Calculates the factorial of an integer
        @param x: the integer to be operated
        @return: the factorial of the number
        """
        if x < 0:
            raise Exception("Not a positive number")
        if x == 1 or x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    if n == 0:
        return x
    else:
        a = ((-1)**n) / (factorial(2 * n + 1))
        b = x**(2 * n + 1)
        c = a * b
        return c + taylor_sin(x, n - 1)

##
# Quinto
def taylor_cos(x, n):
    """
    Computes the taylor series for the cosine function
    @param x: The number whose cosine it's gonna be computed
    @param n: The number of iterations
    @return: the aproximation for the cosine of 'x'
    """

    def factorial(x: int):
        """
        Calculates the factorial of an integer
        @param x: the integer to be operated
        @return: the factorial of the number
        """
        if x < 0:
            raise Exception("Not a positive number")
        if x == 1 or x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    if n == 0:
        return 1
    else:
        a = ((-1)**n)/(factorial(2*n))
        b = x**(2*n)
        c = a*b
        return c + taylor_cos(x, n-1)

##
# Sexto
def plot_exp(x):
    """
    Plots the exponential of a number, its relative and absolute error
    @param x: the number to be plotted
    @return: None
    """
    import numpy as np
    import matplotlib.pyplot as plt
    a_range = np.arange(10, 701, 10)
    results = []
    absolute = []
    relative = []

    fig, ax = plt.subplots(ncols=3, nrows=1, figsize=(20, 5))
    fig.tight_layout(pad=2)

    for i in a_range:
        calculated = taylor_expo(x, i)
        e = np.abs(np.exp(x) - calculated)
        r = e/np.exp(x)
        results.append(calculated)
        absolute.append(e)
        relative.append(r)

    ax[0].plot(a_range, results, color='r')
    ax[1].plot(a_range, absolute, color='g')
    ax[2].plot(a_range, relative, color='b')

    for i in ax:
        i.grid(True)

    plt.show()
    return
##
# Septimo
def plot_sin(x):
    """
    Plots the sine of a number, its relative and absolute error
    @param x: the number to be plotted
    @return: None
    """
    import numpy as np
    import matplotlib.pyplot as plt
    a_range = np.arange(10, 701, 10)
    results = []
    absolute = []
    relative = []

    fig, ax = plt.subplots(ncols=3, nrows=1, figsize=(20, 5))
    fig.tight_layout(pad=2)

    for i in a_range:
        calculated = taylor_sin(x, i)
        e = np.abs(np.sin(x) - calculated)
        r = e/np.sin(x) if e >= 1e-10 else 0
        results.append(calculated)
        absolute.append(e)
        relative.append(r)

    ax[0].plot(a_range, results, color='r')
    ax[1].plot(a_range, absolute, color='g')
    ax[2].plot(a_range, relative, color='b')

    for i in ax:
        i.grid(True)
        i.set_ybound(-2, 2)

    plt.show()
    return
##
# Octavo
def plot_cosin(x):
    """
    Plots the cosine of a number, its relative and absolute error
    @param x: the number to be plotted
    @return: None
    """
    import numpy as np
    import matplotlib.pyplot as plt
    a_range = np.arange(10, 701, 10)
    results = []
    absolute = []
    relative = []

    fig, ax = plt.subplots(ncols=3, nrows=1, figsize=(20, 5))
    fig.tight_layout(pad=2)

    for i in a_range:
        calculated = taylor_cos(x, i)
        e = np.abs(np.cos(x) - calculated)
        r = e/np.sin(x) if e >= 1e-10 else 0
        results.append(calculated)
        absolute.append(e)
        relative.append(r)

    ax[0].plot(a_range, results, color='r')
    ax[1].plot(a_range, absolute, color='g')
    ax[2].plot(a_range, relative, color='b')

    for i in ax:
        i.grid(True)
        i.set_ybound(-2, 2)
    plt.show()
    return
##
# Noveno
def noveno():
    """
    Writes a batch of random numbers on a file
    """
    import numpy as np
    import struct as st
    # Generate random data
    var1 = np.random.randint(low=-10, high=10, size=1000)
    # Open file in Write binary mode
    file = open("FileBinInt16.bin", "wb")
    # Packs the data
    var2 = st.pack("h"*int(len(var1)), *var1)
    # Writes data
    file.write(var2)
    file.close()
##
# Decimo

def plot_data():
    """
    Reads all the data in the integer binaries file
    """
    import struct as st
    import matplotlib.pyplot as plt
    # Opens file in read binary mode
    file = open("FileBinInt16.bin", "rb")
    var1 = file.read()
    # Unpacks all the data
    var2 = st.unpack("h"*int(len(var1)/2), var1)
    file.close()
    # Plots the histogram
    plt.hist(var2, bins=30)
    plt.show()
##
# 11

def onceavo():
    """
    Writes a batch of float numbers
    """
    import numpy as np
    import struct as st
    # Generates data
    var1 = np.random.uniform(-1, 1, 1000)
    # Opens File
    file = open("FileBinDouble.bin", "wb")
    # Packs the set of numbers
    var2 = st.pack("d"*int(len(var1)), *var1)
    var3 = file.write(var2)
    file.close()

##
# 12

def plot_data_1():
    """
    Plots data from the float binary file
    """
    import struct as st
    import matplotlib.pyplot as plt
    # Opens file
    file = open("FileBinDouble.bin", "rb")
    var1 = file.read()
    # Unpacks file
    var2 = st.unpack("d"*int(len(var1)/8), var1)
    file.close()
    # Plots histogram
    plt.hist(var2, bins=30)
    plt.show()

##
# 13
def read_data():
    """
    Reads data from the file File-214.bin
    @return:
    @rtype:
    """
    import struct as st
    file = open("File-214.bin", "rb")
    var1 = file.read()
    var2 = st.unpack("I"*int(len(var1)/4), var1)
    file.close()
    return var2

##
# 14

def data_fib():
    """
    Determines the number of fibonacci numbers in the file
    """
    import struct as st
    def write_data(data):
        """
        Writes a file with data
        @param data: the data to be written
        """
        file = open("File-214.bin", "wb")
        var1 = st.pack("Q" * int(len([data])), *[data])
        file.write(var1)
        file.close()
        return

    file = open("File-214.bin", "rb")
    var1 = file.read()
    var2 = st.unpack("I" * int(len(var1) / 4), var1)
    file.close()
    index = 0
    for num in var2:
        if is_fib(num):
            index += 1
    write_data(index)

##
# 15

def data_sqt():
    """
    Determines the number of square numbers in the file
    """
    import struct as st
    def write_data(data):
        """
        Writes a file with data
        @param data: the data to be written
        """
        file = open("File-214.bin", "wb")
        var1 = st.pack("Q" * int(len([data])), *[data])
        file.write(var1)
        file.close()
        return

    file = open("File-214.bin", "rb")
    var1 = file.read()
    var2 = st.unpack("I" * int(len(var1) / 4), var1)
    file.close()

    index = 0
    for num in var2:
        if is_square(num):
            index += 1
    write_data(index)

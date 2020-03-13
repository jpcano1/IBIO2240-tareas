def concatenate_at_first(string, new_string):
    """
        Concatenates at first
        :param string:
        :param new_string:
        :return:
    """
    b = string
    string = new_string
    string += b
    return string

def mantissa_binary(mantissa):
    """

    :param mantissa:
    :return:
    """
    mantissa = abs(mantissa)
    a = []
    while mantissa != 1 and mantissa != 0:
        mantissa = mantissa * 2
        carac = str(mantissa).split(".")[0]
        a.append(carac)
        if carac == '1' and mantissa != 1:
            mantissa -= 1
    return "".join(a)


def to_binary(number):
    """

    :param number:
    :return:
    """

    if number == 0:
        return 0
    if type(number) == type(1.1):
        raise Exception("Not an integer")

    if number < 0:
        raise Exception("Negative number")
    a = ""

    while number != 1:
        residuo = int(number % 2)
        a = concatenate_at_first(a, str(residuo))
        number = number // 2
    a = concatenate_at_first(a, str(number))
    return a


def two_complement(number, bit_number):
    """

    :param number:
    :param bit_number:
    :return:
    """

    if number > 0:
        return to_binary(number)
    else:
        number = abs(number)

    a = to_binary(number)

    if len(a) > bit_number:
        raise Exception("Not enough bits, sorry bro")

    while len(a) < bit_number:
        a = concatenate_at_first(a, '0')

    binary = list(a)

    i = 1
    if '1' in binary:
        while binary[-i] != '1' and i <= len(binary):
            i += 1
        i += 1
        while i <= len(binary):
            binary[-i] = '0' if binary[-i] == '1' else '1'
            i += 1

    b = ''.join(binary)
    return b


def binary_offset(number, bit_number):
    number = two_complement(number, bit_number)

    if number[0] == '0':
        number = number.replace('0', '1', 1)
    elif number[0] == '1':
        number = number.replace('1', '0', 1)
    return number


def float_any(number, bits):
    """

    :param number:
    :param bits:
    :return:
    """

    a = []
    mantissa_len = 23 if bits == 32 else 52
    carac_len = 127 if bits == 32 else 1023

    if number < 0:
        a.append('1')
    else:
        a.append('0')

    carac = to_binary(abs(int(number)))
    mantissa = mantissa_binary(abs(number - int(number)))

    a.append(to_binary(carac_len + len(carac) - 1))

    carac = carac[1:]
    carac += mantissa

    if len(carac) > mantissa_len:
        raise Exception("Not enough bits for the mantissa bro")

    while len(carac) < mantissa_len:
        carac += "0"

    a.append(carac)
    return "".join(a)


def compare(a, b):
    return a == b


try:
    z = float_any(1000.39, 32)
    print(z)
    print(compare(z, "0100000010001111010000110001111010111000010100011110101110000101"))
except Exception as e:
    print(str(e))


def float_32(number):
    """

    :param number:
    :return:
    """

    a = []
    if number < 0:
        a.append('1')
    else:
        a.append('0')

    carac = to_binary(abs(int(number)))
    mantissa = mantissa_binary(abs(number - int(number)))

    a.append(to_binary(127 + len(carac) - 1))

    carac = carac[1:]
    carac += mantissa

    if len(carac) > 23:
        raise Exception("Not enough bits for the mantissa bro")

    while len(carac) < 23:
        carac += "0"

    a.append(carac)
    return ''.join(a)


def float_64(number):
    """

    :param number:
    :return:
    """

    a = []

    if number < 0:
        a.append('1')
    else:
        a.append('0')

    carac = to_binary(abs(int(number)))
    mantissa = mantissa_binary(abs(number - int(number)))

    a.append(to_binary(1023 + len(carac) - 1))

    carac = carac[1:]
    carac += mantissa

    if len(carac) > 52:
        raise Exception("Not enough bits for the mantissa bro")

    while len(carac) < 52:
        carac += "0"

    a.append(carac)
    return "".join(a)

def print_menu():
    print("----------Laboratorio 5----------")
    print("Escoja la opcion: ")
    print("1. Traducir a binario")
    print("2. IEEE Coma flotante 32 bits")
    print("3. IEEE Coma flotante 64 bits")
    print("4. Salir")

if __name__ == '__main__':
    finished = False

    while not finished:
        print_menu()

        option = int(input())
        if option == 1:
            a = int(input("Ingrese un número a traducir: "))
            print(f"Este es el numero traducido: \n{to_binary(a)}")

        elif option == 2:
            a = float(input("Ingrese un número a traducir: "))
            print(f"Este es el numero traducido: \n{float_32(a)}")

        elif option == 3:
            a = float(input("Ingrese un número a traducir: "))
            print(f"Este es el numero traducido: \n{float_64(a)}")
        elif option == 4:
            finished = True
        else:
            print("Opcion no correcta")
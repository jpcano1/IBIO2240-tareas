###############
# Primer punto
a = int(input("Ingrese un número entero: "))

cadena = ""

"""
Se hacen las verificaciones necesarias para saber si el numero es
positivo, negativo o igual a cero
"""
if a < 0:
    print("El número debe ser mayor a 0")
elif a == 0:
    cadena = "0"
else:
    cadena = ""
    '''Se usa la funcion modulo para conseguir el residuo de nuestras divisiones'''
    while a != 1:
        residuo = int(a % 2)
        b = cadena
        cadena = str(residuo)
        cadena += b
        a = a // 2
    b = cadena
    cadena = str(a)
    cadena += b
'''Se retorna la cadena de caracteres correspondiente al numero binario'''
print(cadena)
########
# Segundo punto

a = int(input("Ingrese un número entero: "))
bit_num = int(input("Ingrese el número de bits a mostrar: "))

cadena = ""
'''Se hacen las verificaciones para saber si el numero es positivo o negativo o igual a cero'''
if a > 0:
    '''Si es positivo, se retorna el numero traducido a binario con el numero de bits correspondientes'''
    if a > (2**(bit_num-1)-1):
        print("Not enough bits")

    else:
        while a != 1:
            residuo = int(a % 2)
            b = cadena
            cadena = str(residuo)
            cadena += b
            a = a // 2
        b = cadena
        cadena = str(a)
        cadena += b
elif a == 0:
    cadena = "0"
else:
    '''Si es negativo se aplica el algoritmo para conseguir el complemento a 2 despues
    de traducir a binario'''
    a = abs(a)

    if a > 2**(bit_num-1):
        print("Not enough bits")

    else:
        while a != 1:
            residuo = int(a % 2)
            b = cadena
            cadena = str(residuo)
            cadena += b
            a = a // 2
        b = cadena
        cadena = str(a)
        cadena += b

        binary = list(cadena)

        i = 1
        '''Se consigue el complemento a 2'''
        if '1' in binary:
            while binary[-i] != '1' and i <= len(binary):
                i += 1
            i += 1
            while i <= len(binary):
                binary[-i] = '0' if binary[-i] == '1' else '1'
                i += 1
        cadena = "".join(binary)

while len(cadena) < bit_num:
    b = cadena
    cadena = '0'
    cadena += b
print(cadena)

######
# Tercer punto

a = int(input("Ingrese un número entero: "))
bit_num = int(input("Ingrese el número de bits a mostrar: "))

'''Se traduce el numero a binario para sacar el offset,
haciendo las respectivas verificaciones'''
cadena = ""
if a > 0:
    if a > (2**(bit_num-1)-1):
        print("Not enough bits")

    else:
        while a != 1:
            residuo = int(a % 2)
            b = cadena
            cadena = str(residuo)
            cadena += b
            a = a // 2
        b = cadena
        cadena = str(a)
        cadena += b
elif a == 0:
     cadena = "0"
else:
    a = abs(a)

    if a > 2**(bit_num-1):
        print("Not enough bits")

    else:
        while a != 1:
            residuo = int(a % 2)
            b = cadena
            cadena = str(residuo)
            cadena += b
            a = a // 2
        b = cadena
        cadena = str(a)
        cadena += b

        binary = list(cadena)

        '''Si el numero es negativo se saca el complemento a 2'''
        i = 1
        if '1' in binary:
            while binary[-i] != '1' and i <= len(binary):
                i += 1
            i += 1
            while i <= len(binary):
                binary[-i] = '0' if binary[-i] == '1' else '1'
                i += 1
        cadena = "".join(binary)

'''Se llena el numero con ceros hasta llegar al numero de bits deseado'''
while len(cadena) < bit_num:
    b = cadena
    cadena = '0'
    cadena += b

'''conseguimos el offset'''
if cadena[0] == '0':
    cadena = cadena.replace('0', '1', 1)
else:
    cadena = cadena.replace('1', '0', 1)

print(cadena)

#####
# Cuarto punto

number = float(input("Ingrese un número entero: "))

a = []
if number < 0:
    a.append('1')
else:
    a.append('0')

mantissa = abs(number - int(number))
number = abs(int(number))
carac = ""

'''Traducimos la caracteristica del numero a binario'''
if number > 0:
    while number != 1:
        residuo = int(number % 2)
        b = carac
        carac = str(residuo)
        carac += b
        number = number // 2
    b = carac
    carac = str(number)
    carac += b
elif number == 0:
    carac = "0"

'''Buscamos el exponente del numero en decimal'''
number = 127 + len(carac) - 1

cadena = ""

'''Traducimos el exponente a binario'''
while number != 1:
    residuo = int(number % 2)
    b = cadena
    cadena = str(residuo)
    cadena += b
    number = number // 2
b = cadena
cadena = str(number)
cadena += b

a.append(cadena)

array = []
'''Traducimos la mantisa del numero a binario'''
while mantissa != 1 and mantissa != 0:
    mantissa = mantissa * 2
    cadena = str(mantissa).split(".")[0]
    array.append(cadena)
    if cadena == '1' and mantissa != 1:
        mantissa -= 1

'''Normalizamos la mantisa'''
mantissa = "".join(array)
carac = carac[1:]
carac += mantissa

if len(carac) > 23:
    print("Not enough bits for the mantissa bro")
else:
    '''Agregamos ceros hasta llegar a los 23 bits'''
    while len(carac) < 23:
        carac += "0"

    a.append(carac)
    print("".join(a))

#####
# Punto 5

number = float(input("Ingrese un número entero: "))

a = []
if number < 0:
    a.append('1')
else:
    a.append('0')

mantissa = abs(number - int(number))
number = abs(int(number))
carac = ""

'''Traducimos la caracteristica del numero a binario'''
if number > 0:
    while number != 1:
        residuo = int(number % 2)
        b = carac
        carac = str(residuo)
        carac += b
        number = number // 2
    b = carac
    carac = str(number)
    carac += b
elif number == 0:
    carac = "0"

'''Buscamos el exponente del numero en decimal'''
number = 1023 + len(carac) - 1

cadena = ""

'''Traducimos el exponente a binario'''
while number != 1:
    residuo = int(number % 2)
    b = cadena
    cadena = str(residuo)
    cadena += b
    number = number // 2
b = cadena
cadena = str(number)
cadena += b

a.append(cadena)

array = []

'''Traducimos la mantisa del numero a binario'''
while mantissa != 1 and mantissa != 0:
    mantissa = mantissa * 2
    cadena = str(mantissa).split(".")[0]
    array.append(cadena)
    if cadena == '1' and mantissa != 1:
        mantissa -= 1

'''Normalizamos la mantisa'''
mantissa = "".join(array)
carac = carac[1:]
carac += mantissa

if len(carac) > 52:
    print("Not enough bits for the mantissa bro")
else:
    while len(carac) < 52:
        carac += "0"

    '''Agregamos ceros hasta llegar a los 23 bits'''
    a.append(carac)
    print("".join(a))
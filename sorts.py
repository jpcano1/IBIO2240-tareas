"""
Created on Thu May 24 11:33:53 2018

@author: Juan Pablo Cano

"""

lista2 = []
while True:
    b = input("Ingresa un número: ")
    if b == "Parar".lower():
        break
    else:
        print(b)
        lista2.append(int(b))
        print(lista2)


# Ordenamiento de selcción.
def selectionSort(lista):
    n = len(lista)
    contador = 0
    for i in range(n):
        menor = lista[i]
        menorIndice = i
        for j in range(i + 1, n):
            otro = lista[j]
            contador += 1
            if menor > otro:
                menor = otro
                menorIndice = j
        if menorIndice != i:
            nuevo = lista[i]
            lista[i] = menor
            lista[menorIndice] = nuevo

    print(contador)

# Ordenamiento de burbuja.
def bubbleSort(lista):
    n = len(lista)
    contador = 0
    for i in reversed(range(1, n + 1)):
        for j in range(0, i - 1):
            contador += 1
            c1 = lista[j]
            c2 = lista[j + 1]
            if c1 > c2:
                lista[j] = c2
                lista[j + 1] = c1
    print(contador)


# Otro ordenamiento de burbuja
def bubbleSort1(lista):
    n = len(lista)
    contenedor = 0

    for i in range(1, n):
        for j in range(n - i):
            contenedor += 1
            menor = lista[j]
            mayor = lista[j + 1]

            if menor > mayor:
                lista[j] = mayor
                lista[j + 1] = menor
    print(contenedor)
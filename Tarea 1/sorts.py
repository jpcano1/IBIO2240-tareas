"""
Created on Thu May 24 11:33:53 2018

@author: Juan Pablo Cano

"""

lista = []
while True:
    b = input("Ingresa un número: ")
    if b == "Parar".lower():
        break
    else:
        print(b)
        lista.append(int(b))
        print(lista)


# Ordenamiento de selcción.
def selectionSort(array):
    n = len(array)
    contador = 0
    for i in range(n):
        menor = array[i]
        menorIndice = i
        for j in range(i + 1, n):
            otro = array[j]
            contador += 1
            if menor > otro:
                menor = otro
                menorIndice = j
        if menorIndice != i:
            nuevo = array[i]
            array[i] = menor
            array[menorIndice] = nuevo

# Otro ordenamiento de burbuja
def bubbleSort1(refactor):
    n = len(refactor)
    contenedor = 0

    for i in range(1, n):
        for j in range(n - i):
            contenedor += 1
            menor = refactor[j]
            mayor = refactor[j + 1]

            if menor > mayor:
                refactor[j] = mayor
                refactor[j + 1] = menor
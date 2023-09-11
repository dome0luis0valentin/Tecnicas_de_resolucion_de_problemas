"""
Dados N pares de valores (P, Q), que son (peso, IQ), determinar cual es la
cadena más larga que se puede formar de pares, tal que:
Todo Pi < Pi+1
Todo Qi < Qi+1

Es decir P, va aumentando y Q se va decrementando

Para que sea un problema de Programación dinámica debe:
    -Solapamiento de subproblemns
    -Subproblema optimo

Pienso que se podrían hacer 2 Lis diferentes, uno para
peso y otro para IQ, crear todos los LIS posibles y con eso
compararlos a ver cual coinciden.

Otra, para cada elemento, lo comparo con el resto y los voy
comparando con el resto, y lo mismo para los otros


Otra,
    1- ordenar los pares por peso, siempre se va a dar que el
i-esimo esta antes que el i-esimo+x
    2- Usar lis para buscar la cadena máxima.
"""


import sys

def solucion(seq, indx):
    #Si ya se calculó el elis de esta posición no se calcula otra vezz
    if (resueltos[indx] != -1):
        return resueltos[indx]

    resueltos[indx] = 1
    prev[indx] = -1

    for i in range(indx+1):
        if ( resueltos[indx] < solucion(seq, i)+1):
            if (seq[i] < seq[indx] ):
                resueltos[indx] = solucion(seq, i) +1
                prev[indx] = i

    return resueltos[indx]

def calcular_max_LIS(seq, n):
    
    salida = solucion(seq, MAX_N-1)
    return (max(resueltos), prev)



line = sys.stdin.readline()
elementos = []
while line != "":
    peso, iq = map(int, line.split())
    elementos.append((peso, iq))
    line = sys.stdin.readline()

elementos.sort(key=lambda x: x[0])

elementos.sort()

IQs = [elemento[1] for elemento in elementos]

cant_punteros = ()

MAX_N  = len(IQs)

resueltos = [-1]*MAX_N
prev = [-1]*MAX_N

cant_punteros = calcular_max_LIS(IQs, MAX_N)

cant= cant_punteros[0]
punteros = cant_punteros[1]     
elefantes = []

def crear_lista_nueva(punteros, elementos):
    nueva_lista = []
    indice_actual = len(punteros)

    #me posicion en el ulitmo elemento
    while indice_actual > 0 and punteros[indice_actual] == -1 :
        indice_actual -= 1

    if (indice_actual > 0):
        
        #Agrego actual
        actual = elementos[indice_actual]
        nueva_lista.append(actual)
        
        while prox != -1:

            nueva_lista.append(elementos[indice_actual])

            #Apunto al siguiente
            prox = punteros[indice_actual]
            #Agrego actual

    return nueva_lista

elefantes = crear_lista_nueva(punteros, elementos)

sys.stdout.writelines(str(cant)+"\n")
for i in elefantes:
    sys.stdout.writelines(str(i[0])+" "+str(i[1])+"\n")






















    

"""
Basicamente:
Te llegan N casos, para cada caso:
    Tenes una secuencia de M enteros, cada uno representa una altitud.
    Tenes que responder la secuencia más larga, tal que solo puede ser estrictamente
creciente.

"""
import sys

def construir_lista(v1, prev):
    n = len(v1)
    result = []

    print("\n")
    print("Caso: ", v1)
    #Agrego el primero
    #Apunto al siguiente
    #Mientras el siguiente != -1
        #Agrego el siguiente
        #Apunto al siguinte

    i = n-1
    #print("Busco el primero")
    while i >= 0 and prev[i] == -1:
        #print(prev[i], ", ",i)
        i-= 1

    if (prev[i] == -1):
        return max(v1)
    primero = v1[i]
    result.append(primero)

    siguiente = prev[i]

    while (siguiente != -1):
        actual = v1[siguiente]
        result.append(actual)
        siguiente = prev[siguiente]
    return result



def lis(seq, n):
    global MAX_N
    global resueltos
    global prev

    MAX_N = n
    resueltos = [-1]*MAX_N
    prev = [-1]*MAX_N

    

    seq = seq

    salida = solucion(seq, MAX_N-1)
    salida = max(resueltos)

    return salida

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


casos = int(sys.stdin.readline())
blanco = sys.stdin.readline()
for caso in range(casos):
    
    alturas = []
    #Recolecto los datos
    
    linea = sys.stdin.readline()
    
    while linea != "\n":
        altura = int(linea)
        alturas.append(altura)
        linea = sys.stdin.readline()


    #Resuelvo el caso
    lis(alturas, len(alturas))

    respuesta = construir_lista(alturas, prev)

    #Muestro el resultado
    output = "Max hits: "+str(len(respuesta))+"\n"
    sys.stdout.writelines(output)
    for i in respuesta:
        sys.stdout.writelines(str(i)+"\n")



















import sys

long = int(sys.stdin.readline())
MAX_N  = long
seq = sys.stdin.readline()

seq = list(map(lambda x: int(x), seq.split()))

resueltos = [-1]*MAX_N
prev = [-1]*MAX_N

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


salida = solucion(seq, MAX_N-1)
salida = max(resueltos)


sys.stdout.write(str(salida)+"\n")

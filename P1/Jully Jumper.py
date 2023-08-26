import sys

def is_jolly(sequence):
    n = sequence[0]
    diferencias = set()

    for I in range(1, n):
        diff = abs(sequence[I] - sequence[I + 1])
        diferencias.add(diff)

    return diferencias == set(range(1, n))

# Lectura de entrada y procesamiento
line = sys.stdin.readline()
while (line):

    sequence = list(map(int, line.split()))
    if is_jolly(sequence):
        print("Jolly")
    else:
        print("Not jolly")
    line = sys.stdin.readline()

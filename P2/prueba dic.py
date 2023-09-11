nombre_archivo = "entrada.txt"  # Reemplaza esto con el nombre de tu archivo de entrada
lineas = []

# Leer las líneas del archivo de entrada y guardarlas en la lista 'lineas'
with open(nombre_archivo, 'r') as archivo:
    lineas = archivo.readlines()

idx = 0  # Índice para rastrear la posición actual en la lista de líneas

while idx < len(lineas):
    N, M = map(int, lineas[idx].split())
    idx += 1

    Jacks_cd = set()
    for _ in range(N):
        CD = lineas[idx].strip()
        Jacks_cd.add(CD)
        idx += 1

    cant_rep = 0
    for _ in range(M):
        CD = lineas[idx].strip()
        if CD in Jacks_cd:
            cant_rep += 1
        idx += 1

    print(cant_rep)

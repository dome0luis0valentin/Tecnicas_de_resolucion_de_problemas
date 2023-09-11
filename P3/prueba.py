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

# Ejemplos
v1_1 = [1, 2, 3, 4]
prev_1 = [-1, 0, 1, 2]
print(construir_lista(v1_1, prev_1))  # Resultado: [4, 3, 2, 1]

v1_2 = [5, 1, 2, 3, 4]
prev_2 = [-1, -1, 1, 2, 3]
print(construir_lista(v1_2, prev_2))  # Resultado: [4, 3, 2, 1]

v1_3 = [5, 1, 2, 3, 4, 0]
prev_3 = [-1, -1, 1, 2, 3, -1]
print(construir_lista(v1_3, prev_3))  # Resultado: [4, 3, 2, 1]

v1_4 = [3, 2, 1]
prev_4 = [-1, -1, -1]
print(construir_lista(v1_4, prev_4))  # Resultado: [1]

v1_5 = [1, 3, 2, 0]
prev_5 = [-1, 1, 0, -1]
print(construir_lista(v1_5, prev_5))  # Resultado: [2, 1]

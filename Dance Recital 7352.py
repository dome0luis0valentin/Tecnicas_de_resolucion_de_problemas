# %%
from itertools import permutations
import sys
import itertools

# %%
#Esta es la función que en teoría se debe de calcular la mínima cantidad de veces
def compare_str(current_dancers, next_dancers):
    current_dancers = set(current_dancers)
    next_dancers = set(next_dancers)
    return len(current_dancers.intersection(next_dancers))  

#%%
def armar_matriz(num_routines, routines):
    matriz_resultado = [[0] * cant_casos for _ in range(cant_casos)]
    lista_de_indices = list(range(0, num_routines))
    # print(num_routines)
    for perm in permutations(lista_de_indices, 2):
        # print(perm)
        index_current = perm[0]
        index_next = perm[1]
        
        quick_changes = compare_str(routines[index_current], routines[index_next])
        
        matriz_resultado[index_current][index_next] = quick_changes
        matriz_resultado[index_next ][index_current] = quick_changes
    
    return matriz_resultado


def calcular_costo(camino, grafo):
    costo = 0
    print("Matriz de costos: ")
    for f in grafo:
        print(f)
    for i in range(1, len(camino) ):
        print(f'Costo total = {costo}, más : costo de nodo {i} y nodo {i-1} = ( {grafo[camino[i]][camino[i-1]]} ) ')
        costo += grafo[camino[i]][camino[i-1]]
    return costo


def fuerza_bruta_hamiltoniano(grafo):
    n = len(grafo)
    nodos = list(range(n))
    mejores_camino = None
    mejor_costo = float('inf')

    for perm in itertools.permutations(nodos):
        costo_actual = calcular_costo(perm, grafo)
        if costo_actual < mejor_costo:
            mejor_costo = costo_actual
            mejores_camino = perm

    return mejores_camino, mejor_costo


#Calcular para cada test
def minimum_quick_changes(num_routines, routines):
    min_changes = float('inf')
    
    matriz_resultado = armar_matriz(num_routines, routines)
   
    # print("--- Matriz de costos armada ---")
    # for i in matriz_resultado:
    #     print(f'{str(i): >10}')
    
    #Con camino de hamilthon por fuerza bruta:
    return fuerza_bruta_hamiltoniano(matriz_resultado)

# # Leer la entrada usando sys.stdin
# lineas_entrada = sys.stdin.readlines()

# # Procesar las líneas de entrada
# indice = 0
# casos = []
# while indice < len(lineas_entrada):
#     # Obtener el número de listas
#     num_listas = int(lineas_entrada[indice].strip())
#     indice += 1

#     # Leer las listas
#     new_lista = [lineas_entrada[indice + i].strip() for i in range(num_listas)]
    
#     # new_lista = crear_diccionario(new_lista)
#     casos.append(new_lista)
#     indice += num_listas
    
# #Caso de ejemplo: 
# import random
caso1 = [ "ABC", "ABEF","DEF", "ABCDE", "FGH"]
casos = [caso1]
# random.shuffle(caso1)
# print(caso1)
# # casos =   [[ "XYZ", "XYZ","ABYZ", "Z"]]

for caso in casos:
    # print("Resultado",minimum_quick_changes(len(listas), listas))
    cant_casos = len(caso)
    res = minimum_quick_changes(cant_casos, caso)[1]
    sys.stdout.writelines(str(res)+"\n")
    

# %%

# %%

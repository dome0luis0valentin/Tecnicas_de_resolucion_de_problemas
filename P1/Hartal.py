import sys

def marcar_dias(hartal, semanas):
    for I in range(0,len(semanas), hartal):
        semanas[I] = True
    return semanas

def calcular_dias_con_paro(semanas, dias):
    dias = 0
    cant_semanas = int(len(semanas)/7)
    for I in range(cant_semanas):
        for J in range(5):
            if ( semanas[I*7+J]== True): 
                dias = dias + 1
    return dias

#Leo la cantidad de tests que hay que hacer.
line = sys.stdin.readline()
cant_casos = int(line)
while( line ):
    
    #para cada caso
    for caso in range(cant_casos):
        dias = int(sys.stdin.readline())
        cant_partes = int(sys.stdin.readline())

        semanas = [False] * dias

    #leo la cantidad de Hartal de cada parte
        for parte in range(cant_partes):
            hartal = int(sys.stdin.readline())
    #En un almanaque marco los días que hubo paro
            semanas = marcar_dias(hartal, semanas)

        dias_con_paro = calcular_dias_con_paro(semanas, dias)

        sys.stdout.write(dias_con_paro)
    

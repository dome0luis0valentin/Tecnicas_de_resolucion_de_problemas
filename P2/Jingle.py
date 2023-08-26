import sys
LINEA_VACIA = "\n"

notas = {
    'W':1,
    'H':0.5,
    'Q':0.25,
    'E':(1/8),
    'S':(1/16),
    'T':(1/32),
    'X':(1/64)
    }

"""
Cada linea que se lea va a tener el formato /medicion/...
donde medicion va a ser alguna de las notas mencionadas arriba
"""

linea = sys.stdin.readline()
while not(linea == LINEA_VACIA):
    mediciones = linea.split("/")[:-1]
    cant_med_correctas = 0

    for medicion in mediciones:
        duracion_med = 0
        for nota in medicion:
            duracion_med += notas[nota]
        if (duracion_med == 1):
            cant_med_correctas += 1
    sys.stdout.write(str(cant_med_correctas) + "\n")

    linea= sys.stdin.readline()

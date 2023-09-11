"""
Dado una entrada que solo puede tener puntos y numerales
Con N consultas, (l, m), donde en cada una:
        cuenta la cantidad de elementos iguales a vec[l], tal que el siguiente
        también es igual a vec[l]


Solución:

Crear 2 vectores adicionales:
    # = [ , , , , ]
    . = [ , , , , ]

Recorró vec, para cada elemento, que encuentro:
    -Para cada elemento marcó cuantos elementos cumplen esta condición, ej:
 # =   [####]  ===>>>  [1,1,1,0]
 # =   [##.##] ===>>>  [1,0,0,1,0]

 Y a partir de ahí calcular, otro vector:

 #_supremo: que cuenta para cada elemento i, cuantos elementos desde 0 hasta i,
 tienen un 1.
 Te quedaría algo como: 
         # =   [####]  ===>>>  [1,1,1,0]  -->  [1,2,3,3], por lo que consulta de:
         (1, 2) = vec[2]- vec[1]
         # =   [##.##] ===>>>  [1,0,0,1,0]

"""

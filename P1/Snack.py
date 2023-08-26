import sys 

precios = {
    1:4.00,
    2:4.50,
    3:5.00,
    4:2.00,
    5:1.50,
    }

entrada = sys.stdin.readline()

codigo = int(entrada.split()[0])
cantidad = int(entrada.split()[1])

print(f'Total: R${precios[codigo] * cantidad}') 

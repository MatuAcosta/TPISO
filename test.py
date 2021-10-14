from lista import lista 
import random

procesos = lista ()

for i in range (1,10):
    proceso = {
        'id': i, 
        'tamano': random.randint(1,250),
        'ta': i,
        'ti': i+1
    }
    procesos.insert(proceso)

procesos.imprimir()
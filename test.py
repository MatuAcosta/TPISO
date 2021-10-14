from lista import lista 
from nodo import nodo 

procesos = []
list = lista ()

for i in range (1,10):
    proceso = {
        'id': i, 
        'tamano': 150,
        'ta': i,
        'ti': i+1
    }
    procesos.append(proceso)

for proceso in procesos: 
    list.insert(proceso)


list.imprimir()
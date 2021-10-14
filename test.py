from lista import lista 
import random

particiones = lista ()
acum = 0

for i in range (1,5):
    if i == 1: 
        particion = { 
            'id': i,
            'tamano': 100,
            'dirInicio': 0
        }
    else:   
        particion = {
            'id': i, 
            'tamano': random.randint(1,250),
            'fragmentacion':0,
            'idproc': None,
            'dirInicio': acum,
            'estado': ''
        }
    acum += (particion['tamano']+1)
    particiones.insert(particion)

particiones.imprimir()
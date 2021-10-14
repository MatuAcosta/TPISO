from lista import lista 
import random

particiones = lista ()
acum = 1

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
            'ta': i,
            'ti': i+1,
            'dirInicio': acum,
            'estado': ''
        }
    acum += particion['tamano']
    particiones.insert(particion)

particiones.imprimir()
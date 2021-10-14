from lista import lista 
import random

particiones = lista ()


for i in range (1,10):
    particion = {
        'id': i, 
        'tamano': random.randint(1,250),
        'fragmentacion':0,
        'idproc': None,
        'ta': i,
        'ti': i+1,
        'dirInicio': 0,
        'estado': ''
    }
    particiones.insert(particion)

particiones.imprimir()
from lista import lista
from particion import Particion

class Memoria():
    def __init__(self):
        pass

    def crearParticiones(self):
        tamanos = [100,250,120,60]
        particiones = lista()
        acum = 0
        for i in range (4):
            if i == 0: 
                particion = Particion(i, tamanos[i], 0, 0, 'Ocupado por SO')
            else:   
                particion = Particion(i, tamanos[i], acum, 0)
            acum += (particion.getTamano() + 1)
            particiones.insert(particion)
        particiones.imprimir()
        return particiones
from proceso import Proceso
from particion import Particion

class Memoria():
    def __init__(self):
        self.particiones = self.crearParticiones()
        self.cola_listos = []

    def crearParticiones(self):
        particiones = []
        tamanos = [100,250,120,60]
        acum = 101
        particion = Particion(0, tamanos[0], 0, 0, 'RESERVADO PARA SO')
        particiones.append(particion)
        for i in range (1,4):
            particion = Particion(i, tamanos[i], acum, 0)
            acum += (particion.getTamaño() + 1)
            particiones.append(particion)
        return particiones
        
    
    
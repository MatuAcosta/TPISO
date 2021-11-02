
from particion import Particion

class Memoria():
    def __init__(self):
        self.particiones = self.crearParticiones()

    def crearParticiones(self):
        particiones = []
        tamanos = [100,250,120,60]
        acum = 0
        particion = Particion(0, tamanos[0], 0, 0, 'Ocupado por SO')
        particiones.append(particion)
        for i in range (1,4):
            particion = Particion(i, tamanos[i], acum, 0)
            acum += (particion.getTamaño() + 1)
            particiones.append(particion)
        return particiones
        
    def mostrarParticiones(self):
        for i in self.particiones:
            print(i.getData())
    

from particion import Particion 
from proceso import Proceso
from memoria import Memoria

def preguntar(atrib):
        return int(input(f"Ingrese {atrib} de proceso: "))

filename = 'files/procesos.txt'
class SistemaOperativo():
    def __init__(self):  
        self.memoria = Memoria()
        self.multiprogramacion = 10
        self.procesos = []
        self.cola_listos = []
        self.cola_nuevos = []
        self.instante = 0 

    # Creacion de procesos donde sus atributos son leidos desde un archivo
    def crearprocesos(self):
        with open(filename) as f_obj:
            lines = f_obj.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(' ')
            proceso = Proceso(int(line[0]),int(line[1]),int(line[2]),int(line[3]))
            self.procesos.append(proceso)

    def mostrarProcesos(self):
        for proceso in self.procesos:
            print(proceso.getData())

    def cargarNuevos(self):
        for proceso in self.procesos:    
            if self.instante == proceso.getTa():
                self.cola_nuevos.append(proceso)

    def mostrarNuevos(self):
        for proceso in self.cola_nuevos:
            print(proceso.getData())

    def bestFit(self):
        particiones = self.memoria.particiones
        pos = 0
        for proceso in self.cola_nuevos:  
            entro = False
            i = 0  
            minfrag = 250
            for particion in particiones:
                if (particion.proceso == None) and (proceso.getTamaño() <= particion.getTamaño() and i != 0):
                    if particion.getTamaño() - proceso.getTamaño() < minfrag:
                        minfrag = particion.getTamaño() - proceso.getTamaño() 
                        pos = i
                        entro = True
                i+=1
            if not entro:
                self.cargarDisco(proceso)
            else:
                particiones[pos].cargarProceso(proceso)
                self.cola_listos.append(proceso)
        self.cola_listos = sorted (self.cola_listos, key = lambda proc: proc.ti)       
                

    def cargarDisco(self, proceso):
        pass

    def colaListo(self):
        for proceso in self.cola_listos:
            print(proceso.getData())


prueba = SistemaOperativo()
memoria = prueba.memoria
memoria.crearParticiones()
memoria.mostrarParticiones()
print('-' * 50)
prueba.crearprocesos()
prueba.cargarNuevos()
prueba.bestFit()
prueba.mostrarNuevos()
print('-' * 50)
prueba.mostrarProcesos()
print('-' * 50)
memoria.mostrarParticiones()
print('-' * 50)
prueba.colaListo()


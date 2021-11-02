
from particion import Particion 
from proceso import Proceso
from memoria import Memoria

def preguntar(atrib):
        return int(input(f"Ingrese {atrib} de proceso: "))

class SistemaOperativo():
    def __init__(self):  
        self.memoria = Memoria()
        self.multiprogramacion = 10
        self.procesos = []
        self.cola_listos = []
        self.cola_nuevos = []
        self.instante = 0    

    def crearprocesos(self):
        for i in range (2):
            proceso = Proceso(i, preguntar("tamano"), preguntar("ta"), preguntar("ti"))
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
        minfrag = 1000
        pos = 0
        
        for proceso in self.cola_nuevos:  
            entro = False
            i = 0  
            for particion in particiones:
                if (particion.proceso == None) and (proceso.getTamaño() < particion.getTamaño()):
                    if particion.getTamaño() - proceso.getTamaño() < minfrag:
                        minfrag = particion.getTamaño() - proceso.getTamaño() < minfrag
                        pos = i
                        entro = True
                i+=1
            if not entro:
                self.cargarDisco(proceso)
            else:
                particiones[pos].cargarProceso(proceso)
                self.cola_listos.append(proceso)

    def cargarDisco(self, proceso):
        pass


prueba = SistemaOperativo()
memoria = prueba.memoria
memoria.crearParticiones()
memoria.mostrarParticiones()
print('-' * 50)
prueba.crearprocesos()
prueba.cargarNuevos()
prueba.bestFit()
prueba.mostrarNuevos()


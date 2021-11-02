from memSec import memoriaSec
from cpu import Cpu
from particion import Particion 
from proceso import Proceso
from memoria import Memoria

def preguntar(atrib):
        return int(input(f"Ingrese {atrib} de proceso: "))

filename = 'files/procesos.txt'
class SistemaOperativo():
    #Inicializar variables del Sistema Operativo
    def __init__(self):  
        self.memoria = Memoria()
        self.cpu = Cpu()
        self.disco = memoriaSec()
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
        carga = False #Se refiere a si se cargo almenos un proceso a memoria o no 
        nuevos = self.cola_nuevos
        for proceso in nuevos:  
            entro = False #Se refiere a si el proceso entro en memoria o no
            i = 0  
            minfrag = 250
            for particion in particiones:
                if (particion.proceso == None) and proceso.getTamaño() <= particion.getTamaño() and i != 0:
                    if particion.getTamaño() - proceso.getTamaño() < minfrag:
                        minfrag = particion.getTamaño() - proceso.getTamaño() 
                        pos = i
                        entro = True
                        carga = True
                i+=1
            if not entro:
                self.cargarDisco(proceso) #
            else:
                particiones[pos].cargarProceso(proceso)
                self.cola_nuevos.remove(proceso)
                self.cola_listos.append(proceso)
        if carga:
            self.cola_listos = sorted(self.cola_listos, key = lambda proc: proc.ti)
        else:
            return 0 
   
    def cargarDisco(self, proceso):
        self.disco.agregarProceso(proceso)

    def mostrarListos(self):
        for proceso in self.cola_listos:
            print(proceso.getData())

    def srtf(self):
        if (self.cpu.proceso == None):
            self.cpu.cargarProceso(self.cola_listos[0])

    def mostrarCpu(self):
        print(self.cpu.getData())

so = SistemaOperativo()
memoria = so.memoria
memoria.crearParticiones()
so.crearprocesos()
so.cargarNuevos()
so.mostrarNuevos()
so.bestFit()
print('-' * 50)
so.mostrarNuevos()
print('-' * 50)
so.colaListo()



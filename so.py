from memSec import memoriaSec
from cpu import Cpu
from particion import Particion
from planifCortoplazo import planifCorto
from planifMedianoPlazo import planifMediano 
from proceso import Proceso
from memoria import Memoria
from planifLargoPlazo import PlanifLargoPlazo

def preguntar(atrib):
        return int(input(f"Ingrese {atrib} de proceso: "))

filename = 'files/procesos.txt'
class SistemaOperativo ():
    #Inicializar variables del Sistema Operativo
    def __init__(self):  
        self.memoria = Memoria()
        self.cpu = Cpu()
        self.disco = memoriaSec()
        self.planifCorto = planifCorto()
        self.planifMediano = planifMediano ()
        self.planifLargo = PlanifLargoPlazo()
        self.multiprogramacion = 10
        self.procesos = []
        self.cola_nuevos = []
        
    # Creacion de procesos donde sus atributos son leidos desde un archivo
    def crearprocesos(self):
        with open(filename) as f_obj:
            lines = f_obj.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(' ')
            proceso = Proceso(int(line[0]),int(line[1]),int(line[2]),int(line[3]))
            self.procesos.append(proceso)

    # Mostrar datos del proceso por pantalla

    # Cargar proceso a la cola de nuevos
    def cargarNuevos(self, instante):
        for proceso in self.procesos:    
            if instante == proceso.getTa(): # Se pregunta si el instante es igual al tiempo de arribo del proceso
                self.cola_nuevos.append(proceso)
        self.cola_nuevos = sorted(self.cola_nuevos, key = lambda proc: proc.ti)
        
    def mostrarNuevos(self):
        for proceso in self.cola_nuevos:
            print(proceso.getData())

    


#Criterios de expropiación a tener en cuenta:
#1. Si un proceso está en ejecución y se admite en la cola de listos, un proceso nuevo con mayor prioridad de ejecución,  entonces se saca al proceso actual de CPU, sin suspenderlo, y se le asigna la CPU al proceso con mayor prioridad.
#2. En caso que el proceso con mayor prioridad haya ingresado a la cola de procesos listos y suspendidos, entonces podrá suspenderse un proceso ya asignado a memoria (utilizando swapout) para darle lugar en memoria al proceso con mayor prioridad. Para sacar un proceso de memoria, el criterio será el siguiente:
#a- Primero se intentará suspender un proceso que no esté en CPU.
#b- Si el proceso nuevo no cabe en ninguno de los bloques de los procesos que no están en CPU, y cabe en la partición del que está en la CPU, entonces se suspenderá al proceso que está CPU, para colocar el nuevo proceso (que tiene mayor prioridad) en su lugar de memoria.
#c- Luego se le asignará la CPU al nuevo proceso de mayor prioridad, que ahora sí se encuentra en estado de Listo.
#Luego se continúa con la ejecución del proceso nuevo, con mayor prioridad.
#Deberán definir ademas el funcionamiento y controles del planificador a mediano plazo, que es el que decide cuándo y mediante qué controles el proceso suspendido vuelve a la memoria (y, por ende, a la cola de Listos)


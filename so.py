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
    def __init__(self, memoria, disco, cpu):  
        self.memoria = memoria
        self.cpu = cpu
        self.disco = disco
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

    def cantProcesos (self):
        with open(filename) as f_obj:
            lines = f_obj.readlines()
        return len(lines)

    def tiProcesos (self):
        tiOrig = []
        with open(filename) as f_obj:
            lines = f_obj.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(' ')
            tiOrig.append(int(line[3]))
        return tiOrig
    # Mostrar datos del proceso por pantalla

    # Cargar proceso a la cola de nuevos
    def cargarNuevos(self, instante):
        for proceso in self.procesos:    
            if instante == proceso.getTa(): # Se pregunta si el instante es igual al tiempo de arribo del proceso
                self.cola_nuevos.append(proceso)
        self.cola_nuevos = sorted(self.cola_nuevos, key = lambda proc: proc.ti)
        

    


#Criterios de expropiaci??n a tener en cuenta:
#1. Si un proceso est?? en ejecuci??n y se admite en la cola de listos, un proceso nuevo con mayor prioridad de ejecuci??n,  entonces se saca al proceso actual de CPU, sin suspenderlo, y se le asigna la CPU al proceso con mayor prioridad.
#2. En caso que el proceso con mayor prioridad haya ingresado a la cola de procesos listos y suspendidos, entonces podr?? suspenderse un proceso ya asignado a memoria (utilizando swapout) para darle lugar en memoria al proceso con mayor prioridad. Para sacar un proceso de memoria, el criterio ser?? el siguiente:
#a- Primero se intentar?? suspender un proceso que no est?? en CPU.
#b- Si el proceso nuevo no cabe en ninguno de los bloques de los procesos que no est??n en CPU, y cabe en la partici??n del que est?? en la CPU, entonces se suspender?? al proceso que est?? CPU, para colocar el nuevo proceso (que tiene mayor prioridad) en su lugar de memoria.
#c- Luego se le asignar?? la CPU al nuevo proceso de mayor prioridad, que ahora s?? se encuentra en estado de Listo.
#Luego se contin??a con la ejecuci??n del proceso nuevo, con mayor prioridad.
#Deber??n definir ademas el funcionamiento y controles del planificador a mediano plazo, que es el que decide cu??ndo y mediante qu?? controles el proceso suspendido vuelve a la memoria (y, por ende, a la cola de Listos)



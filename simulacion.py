from so import SistemaOperativo
from memSec import memoriaSec
from cpu import Cpu
from particion import Particion 
from proceso import Proceso
from memoria import Memoria

reloj = 0 
so = SistemaOperativo ()
nuevos = so.cola_nuevos 
listos = so.memoria.cola_listos
disco = so.disco
memoria = so.memoria

def mostrarNuevos():
    for proceso in nuevos:
        print(proceso.getData(),'instante:',reloj)

def mostrarListos():
    for proceso in listos :
        print(proceso.getData(),'instante:',reloj)

def mostrarProcesos():
    for proceso in so.procesos:
        print(proceso.getData(),'instante:',reloj)


## Comenzamos creando los procesos 
so.crearprocesos()

## la simulacion ira hasta q las 3 colas esten vacias.
#nuevos.len != 0 or listos.len !=0 or disco.len !=0 esta deberia ser la condicion de fin 

while (reloj < 10):
    so.cargarNuevos()
    so.bestFit()
    if so.cola_nuevos:
        for proceso in so.cola_nuevos: 
            so.planifMediano.cargarDisco(so.disco,proceso)
    if so.disco.procSusp:
        for proceso in so.disco.procSusp: 
            if (so.planifMediano.swap (memoria,proceso,so.disco,'Listo')):
                pass
        else:
            if (so.planifMediano.swap(memoria,proceso,so.disco,'Ejecucion')):
                pass    
        memoria.cola_listos = sorted(memoria.cola_listos, key = lambda proc: proc.ti)
    
    so.planifCorto.srtf(so.memoria.cola_listos,so.cpu)
    print ('Listos')
    mostrarListos() 
    print ('EJECUTANDO')
    so.mostrarCpu()
    so.cpu.proceso.ti -=1
    reloj +=1



#print('-' * 50)
#so.mostrarNuevos()
#so.bestFit()
#print('-' * 50)
# so.mostrarNuevos()
#so.disco.mostrarDisco()
#print('-' * 50)
#print('Listos')
#so.mostrarListos()
#print('-' * 50)
#memoria.mostrarParticiones()
#print('-' * 50)
#so.srtf()
#so.mostrarCpu()
    
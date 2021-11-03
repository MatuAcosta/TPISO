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
    
    mostrarListos() 
    print ('reloj',reloj)
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
    
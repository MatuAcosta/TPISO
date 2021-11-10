from so import SistemaOperativo
from memSec import memoriaSec
from cpu import Cpu
from particion import Particion 
from proceso import Proceso
from memoria import Memoria

reloj = 0 
so = SistemaOperativo ()


def mostrarNuevos():
    for proceso in so.cola_nuevos:
        print(proceso.getData(),'instante:',reloj)

def mostrarListos(listos):
    for proceso in so.memoria.cola_listos:
        print(proceso.getData(),'instante:',reloj)

def mostrarProcesos():
    for proceso in so.procesos:
        print(proceso.getData(),'instante:',reloj)

def mostrarCpu():
        print(so.cpu.getData())

def mostrarDisco():
        mensaje = ""
        for proceso in so.disco.procSusp: 
            mensaje += str(proceso.id) + " "
        print(mensaje)

## Comenzamos creando los procesos 
so.crearprocesos()

## la simulacion ira hasta q las 3 colas esten vacias.
#nuevos.len != 0 or listos.len !=0 or disco.len !=0 esta deberia ser la condicion de fin 
so.cargarNuevos(reloj)
while (so.cola_nuevos or so.memoria.cola_listos):
    so.planifLargo.bestFit(so.memoria, so.cola_nuevos)
    print('Instante: ',reloj)
    print("NUEVOS")
    mostrarNuevos()
    nuevos2 = so.cola_nuevos.copy()
    if nuevos2:
        for proceso in nuevos2: 
            so.planifMediano.cargarDisco(so.disco,proceso, so.cola_nuevos)
    if so.disco.procSusp:
        for proceso in so.disco.procSusp: 
            swap = so.planifMediano.swap(so.memoria,proceso,so.disco,'Listo')
            if not swap: 
                so.planifMediano.swap(so.memoria,proceso,so.disco,'Ejecucion')
        so.memoria.cola_listos = sorted(so.memoria.cola_listos, key = lambda proc: proc.ti)
    so.planifCorto.srtf(so.memoria.cola_listos,so.cpu)

    print ('LISTOS')
    mostrarListos(so.memoria.cola_listos) 
    print ('EJECUTANDO')
    mostrarCpu()
    print("SUSPENDIDOS")
    mostrarDisco()
    print('-'*50)
    if so.cpu.proceso:
        so.cpu.proceso.ti -=1
    reloj +=1
    so.cargarNuevos(reloj)
    ban = False


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
    
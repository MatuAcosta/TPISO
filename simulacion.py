from memoria import Memoria
from so import SistemaOperativo
from memoria import Memoria
from cpu import Cpu
from memSec import memoriaSec

reloj = 0 
memoria = Memoria()
cpu = Cpu()
disco = memoriaSec()
so = SistemaOperativo(memoria, disco, cpu)



def mostrarNuevos():
    for proceso in so.cola_nuevos:
        print(proceso.getData(),'instante:',reloj)

def mostrarListos():
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
ban = True
while (reloj < 100 or ban):
    
    #En cada instante nuevo verificamos si llegan procesos nuevos.
    so.cargarNuevos(reloj)
    print("---NUEVOS----")
    mostrarNuevos()
    #Luego realizamos el algoritmo bestfit para ubicar los procesos en memoria.
    so.planifLargo.bestFit(so.memoria, so.cola_nuevos)
    
    nuevos2 = so.cola_nuevos.copy()
    #LOS PROCESOS QUE NO ENTRARON A MEMORIA VAN A LISTO Y SUSPENDIDO (DISCO)
    if nuevos2:
        for proceso in nuevos2: 
            so.planifMediano.cargarDisco(so.disco,proceso, so.cola_nuevos)
    #DISMINUIMOS EN UNO EL TIEMPO DE IRRUPCION DEL PROCESO EN MEMORIA Y CONTROLAMOS SI TERMINA. 
    if so.disco.procSusp:
        for proceso in so.disco.procSusp: 
            swap = so.planifMediano.swap(so.memoria,proceso,so.disco,'Listo')
            if not swap: 
                so.planifMediano.swap(so.memoria,proceso,so.disco,'Ejecucion')
        so.memoria.cola_listos = sorted(so.memoria.cola_listos, key = lambda proc: proc.ti) 
    if so.cpu.proceso:
        so.cpu.proceso.ti -=1
        termino = so.planifCorto.terminaProceso(so.cpu)
        if termino:
            so.planifLargo.quitarProceso(so.memoria,termino) 
    #REALIZAMOS SRTF 
    so.planifCorto.srtf(so.memoria.cola_listos,so.cpu)

    #NOS FIJAMOS EN LAS PARTICIONES SI ALGUNA ESTA LIBRE, DE SER ASI MIRAMOS EL DISCO Y COLOCAMOS.
    for particion in so.memoria.particiones: 
        if particion.estado == 'Libre':
            if so.disco.procSusp:
                proceso = so.disco.procSusp[0]
                if proceso: #verificamos que el proceso que estaba en disco entre en la particion
                    if particion.tamano >= proceso.tamano:
                        so.planifMediano.quitar(so.disco)
                        particion.cargarProceso(proceso)
                        so.memoria.cola_listos.append(proceso)
                        so.memoria.cola_listos = sorted(so.memoria.cola_listos, key = lambda proc: proc.ti)



    print ('----LISTOS----')
    mostrarListos() 
    print("----SUSPENDIDOS----")
    mostrarDisco()
    print ('--EJECUTANDO--')
    mostrarCpu()
    print ('--Particiones--')
    so.memoria.mostrarParticiones()
    reloj +=1
    ban = False





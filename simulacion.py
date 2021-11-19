from os import sep
from memoria import Memoria
from so import SistemaOperativo
from memoria import Memoria
from cpu import Cpu
from memSec import memoriaSec
from tabulate import tabulate

reloj = 0 
memoria = Memoria()
cpu = Cpu()
disco = memoriaSec()
so = SistemaOperativo(memoria, disco, cpu)


def menuInicial():
        print(
            """
            --------------------------------------------------------------
            SIMULADOR DE ASIGNACION DE MEMORIA Y PLANIFICACION DE PROCESOS
            --------------------------------------------------------------
            """
        )
        input("Enter para iniciar Simulacion...")

def mostrarProcesosCreados():
    print("******** PROCESO CREADOS ********\n")
    cabecera = ['id', 'tamaño', 'TA', 'TI']
    datos = []
    for proceso in so.procesos:
        datos.append([proceso.id, proceso.tamano, proceso.ta, proceso.ti])
    print(tabulate(datos, headers=cabecera, tablefmt='grid', stralign='center'))
    input("\nEnter para continuar")

def separador():
    print('\n','-'*155, '\n')

def mostrarNuevos():
    
    print("******** PROCESO NUEVOS ********\n")
    cabecera = ['id', 'tamaño', 'TA', 'TI', 'Instante']
    datos = []
    for proceso in so.cola_nuevos:
        datos.append([proceso.id, proceso.tamano, proceso.ta, proceso.ti])
    print(tabulate(datos, headers=cabecera, tablefmt='grid', stralign='center'))

def mostrarListos():
    print("******** PROCESO LISTOS ********\n")
    cabecera = ['id', 'tamaño', 'TA', 'TI', 'Instante']
    datos = []
    for proceso in so.memoria.cola_listos:
        datos.append([proceso.id, proceso.tamano, proceso.ta, proceso.ti])
    print(tabulate(datos, headers=cabecera, tablefmt='grid', stralign='center'))

def mostrarProcesos():
    for proceso in so.procesos:
        print(proceso.getData(),'instante:',reloj)

def mostrarCpu():
    print ('\n----PROCESO EJECUTANDO----\n')
    print(so.cpu.getData())

def mostrarDisco():
    print("\n----PROCESOS LISTOS Y SUSPENDIDOS----\n")
    if not so.disco.hayProceso():
        print("No hay procesos en disco")
        return
    cabecera = ['id']
    datos = []
    for proceso in so.disco.procSusp: 
        datos.append(str(proceso.id))
    print(tabulate(datos, headers=cabecera, tablefmt='grid', stralign='center'))

def mostrarParticiones():
    print ('\n----ESTADO DE PARTICIONES----\n')
    particiones = so.memoria.particiones
    cabecera = ['id', 'Tamaño', 'Inicio', 'Fragmentacion', 'Estado', 'Proceso']
    datos = []
    for i in particiones:
        if i.hayProceso():
            datos.append([i.id, i.tamano, i.dirInicio, i.fragmentacion, i.estado, str(i.proceso.id)])
        else:
            datos.append([i.id, i.tamano, i.dirInicio, i.fragmentacion, i.estado, "-"])
    print(tabulate(datos, headers=cabecera, tablefmt='grid', stralign='center'))

def mostrarEstado():
    mostrarListos() 
    mostrarDisco()
    mostrarCpu()
    mostrarParticiones()
   

## Comenzamos creando los procesos 

def simulacion(reloj):

    menuInicial()
    so.crearprocesos()
    mostrarProcesosCreados()
    ## la simulacion ira hasta q las 3 colas esten vacias.
    res = 's'
    so.cargarNuevos(reloj)
    while ((so.cola_nuevos or so.memoria.cola_listos or so.disco.procSusp or so.cpu.proceso) and res == 's'):
        
        #En cada instante nuevo verificamos si llegan procesos nuevos.
        separador()
        print('INSTANTE: ',reloj,'\n')
        mostrarNuevos()
        #Luego realizamos el algoritmo bestfit para ubicar los procesos en memoria.
        so.planifLargo.bestFit(so.memoria, so.cola_nuevos)
        
        nuevos2 = so.cola_nuevos.copy()
        #LOS PROCESOS QUE NO ENTRARON A MEMORIA VAN A LISTO Y SUSPENDIDO (DISCO)
        if nuevos2:
            for proceso in nuevos2: 
                so.planifMediano.cargarDisco(so.disco,proceso, so.cola_nuevos)
        if so.disco.procSusp:
            for proceso in so.disco.procSusp: 
                swap = so.planifMediano.swap(so.memoria,proceso,so.disco,'Listo')
                if not swap: 
                    so.planifMediano.swap(so.memoria,proceso,so.disco,'Ejecucion')
            so.memoria.cola_listos = sorted(so.memoria.cola_listos, key = lambda proc: proc.ti) 
        #DISMINUIMOS EN UNO EL TIEMPO DE IRRUPCION DEL PROCESO EN MEMORIA Y CONTROLAMOS SI TERMINA. 
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
                        #verificamos que el proceso que estaba en disco entre en la particion
                    if proceso: 
                        if particion.tamano >= proceso.tamano:
                            so.planifMediano.quitar(so.disco)
                            particion.cargarProceso(proceso)
                            so.memoria.cola_listos.append(proceso)
                            so.memoria.cola_listos = sorted(so.memoria.cola_listos, key = lambda proc: proc.ti)
        mostrarEstado()
        res = input('\nQuiere seguir? S --> SI O N--> NO:').lower()
        while(res != 's'):
            res = input('Ingrese nuevamente: S --> SI O N--> NO:').lower()
        reloj +=1
        so.cargarNuevos(reloj) 

simulacion(reloj)
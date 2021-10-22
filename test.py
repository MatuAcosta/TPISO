from lista import lista
from particion import Particion 
from proceso import Proceso
from memoria import Memoria
import random

def crearprocesos (cant):
    procesos = lista() 
    for i in range (cant):
        proceso = Proceso(i, preguntar("tamano"), preguntar("ta"), preguntar("ti"))
        procesos.insert(proceso)
    procesos.imprimir()
    return procesos

def preguntar(atrib):
        return int(input(f"Ingrese {atrib} de proceso: "))




memoria = Memoria()
memoria.crearParticiones()
#procesos = crearprocesos(5)
#particiones = crearparticiones()

# def asignarProcesos():
#     particiones = crearparticiones()
#     procesos = crearprocesos(5)
#     while particiones:
#         print(particiones.data)
#         particiones = particiones.next




#crearprocesos(2)
#crearparticiones()
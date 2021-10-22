from lista import lista 
import random

def crearprocesos (cant):
    procesos = lista() 
    for i in range (cant):
        proceso = { 
            'id': i,
            'tamano': preguntar('tamaño'),# random.randint(1,250), #podemos preguntar al usuario
            'ta':  preguntar('Tiempo de Arribo'), #podemos preguntar
            'ti':  preguntar('Tiempo de Irrupcion') #podemos preguntar
        }
        procesos.insert(proceso)
    procesos.imprimir()
    return procesos

def preguntar(atrib):
        return int(input(f"Ingrese {atrib} de proceso: "))

def crearparticiones ():
    tamanos = [100,250,120,60]
    particiones = lista ()
    acum = 0
    for i in range (4):
        if i == 0: 
            particion = { 
                'id': i,
                'tamano': tamanos[i],
                'dirInicio': 0
            }
        else:   
            particion = {
                'id': i, 
                'tamano': tamanos[i] ,
                'fragmentacion':0,
                'idproc': None,
                'dirInicio': acum,
                'estado': ''
            }
        acum += (particion['tamano']+1)
        particiones.insert(particion)
    particiones.imprimir()
    return particiones


#procesos = crearprocesos(5)
#particiones = crearparticiones()

# def asignarProcesos():
#     particiones = crearparticiones()
#     procesos = crearprocesos(5)
#     while particiones:
#         print(particiones.data)
#         particiones = particiones.next




#crearprocesos(5)
#crearparticiones()
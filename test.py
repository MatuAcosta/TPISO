from lista import lista 
import random

def crearproceso ():
    cantprocesos = 5 #podemos preguntarle al usuario
    procesos = lista ()  
    for i in range (cantprocesos):
        proceso = { 
            'id': i,
            'tamano': random.randint(1,250), #podemos preguntar al usuario
            'ta':  random.randint(1,250), #podemos preguntar
            'ti':  random.randint(1,250) #podemos preguntar
        }
        procesos.insert(proceso)

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


crearparticiones()
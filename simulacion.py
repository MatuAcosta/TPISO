from so import SistemaOperativo

reloj = 0 
so = SistemaOperativo ()
nuevos = so.cola_nuevos 
listos = so.cola_listos
disco = so.disco
## Comenzamos creando los procesos 

so.crearprocesos()

## la simulacion ira hasta q las 3 colas esten vacias.
#nuevos.len != 0 or listos.len !=0 or disco.len !=0 esta deberia ser la condicion de fin 
while (reloj < 10):
    so.cargarNuevos()
    so.bestFit()

 # if (self.disco.len < 6):
 #           self.disco.agregarProceso(proceso)
 #       particiones = self.memoria.particiones
 #       for i in range (len(particiones)): 
 #           if particiones[i].tamano >= proceso.tamano :
 #               for proc in self.cola_listos : 
 #                   if proceso.ti < proc.ti :
 #                       for j in range (len(particiones)-i)
    
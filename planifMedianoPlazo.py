from types import prepare_class


class planifMediano: 
    
    def cargarDisco(self,disco,proceso,nuevos):
        if (len(disco.procSusp) < 7):
            disco.agregarProceso(proceso)
            nuevos.remove(proceso)
            proceso.estado = "Suspendido"
            disco.procSusp = sorted(disco.procSusp, key = lambda proc: proc.ti)


    #quitamos el proceso del disco y lo retornamos.
    def quitar (self,disco): 
        if (disco.procSusp):
            proceso = disco.procSusp[0]
            disco.quitarProceso(proceso)
            disco.procSusp = sorted(disco.procSusp, key = lambda proc: proc.ti)
            return proceso
        


    def swap (self,memoria,proceso,disco,estado):
        min = 250
        i=0
        pos = None 
        particiones = memoria.particiones
        for particion in particiones: 
            if(particion.id != 0):
                if particion.estado == 'Ocupado':
                    if particion.tamano >= proceso.tamano:
                        if particion.proceso.estado == estado:
                            if particion.proceso.ti > proceso.ti and min > proceso.ti:
                                pos = i
                                min = proceso.ti

            i+=1          
        if pos: 
            fuera = memoria.particiones[pos].proceso
            if estado == 'Listo':
                for proc in memoria.cola_listos: 
                    if fuera == proc :
                        memoria.cola_listos.remove(fuera)
            memoria.cola_listos.append(proceso)
            disco.agregarProceso(fuera)
            disco.quitarProceso(proceso)
            particiones[pos].cargarProceso(proceso) 
            return True
        else:
            return False
class planifMediano: 
    def __init__(self):
        pass

    def cargarDisco(self,disco,proceso):
        if (len(disco.procSusp) < 7):
            disco.agregarProceso(proceso)
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
from types import prepare_class


class planifMediano: 
    def cargarDisco(self,disco,proceso,nuevos):
        if (len(disco.procSusp) < 7):
            disco.agregarProceso(proceso)
            nuevos.remove(proceso)
            proceso.estado = "Suspendido"
            disco.procSusp = sorted(disco.procSusp, key = lambda proc: proc.ti)


    #quitamos el proceso del disco y lo retornamos.
    def quitar (self,disco,proceso): 
            disco.quitarProceso(proceso)
            if (disco.procSusp):
                disco.procSusp = sorted(disco.procSusp, key = lambda proc: proc.ti)
            return proceso
        


    def swap (self,memoria,proceso,disco,estado):
        libre = False

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

    def partiLibres(self,memoria,disco):
        for particion in memoria.particiones: 
                if particion.estado == 'Libre':
                    if disco.procSusp:
                        for proceso in disco.procSusp:
                            #verificamos que el proceso que estaba en disco entre en la particion
                            if proceso: 
                                if particion.tamano >= proceso.tamano:
                                    self.quitar(disco,proceso)
                                    particion.cargarProceso(proceso)
                                    memoria.cola_listos.append(proceso)
                                    memoria.cola_listos = sorted(memoria.cola_listos, key = lambda proc: proc.ti)

                #else: 
                #    if particion.estado == 'Libre':
                #        if particion.tamano >= proceso.tamano:
                #                pos = i
                #                libre = True
                # else: 
                #memoria.cola_listos.append(proceso)
                #disco.quitarProceso(proceso)
                #particiones[pos].cargarProceso(proceso)

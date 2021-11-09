class PlanifLargoPlazo:

    def bestFit(self,memoria,colaNuevos):
        particiones = memoria.particiones
        pos = 0
        nuevos = colaNuevos.copy()
        for proceso in nuevos:  
            entro = False #Se refiere a si el proceso entro en memoria o no
            i = 0  
            minfrag = 250
            #ALGORITMO BEST FIT
            for particion in particiones:
                if (particion.proceso == None) and proceso.getTamaño() <= particion.getTamaño() and i != 0:
                    if particion.getTamaño() - proceso.getTamaño() < minfrag:
                        minfrag = particion.getTamaño() - proceso.getTamaño() 
                        pos = i
                        entro = True 
                i+=1
            if entro:
                particiones[pos].cargarProceso(proceso)
                memoria.cola_listos.append(proceso)
                #eliminamos el proceso de la cola de nuevos si se agrego a memoria.
                colaNuevos.remove(proceso)

        if memoria.cola_listos:
            memoria.cola_listos = sorted(memoria.cola_listos, key = lambda proc: proc.ti)

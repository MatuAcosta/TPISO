class planifCorto: 

    def terminaProceso (self,cpu): 
        if cpu.proceso:
            if cpu.proceso.ti == 0:
                proceso = cpu.proceso
                cpu.quitarProceso()
                return proceso
        return False


    def srtf(self,listos,cpu):
        if (cpu.proceso == None and listos):
            cpu.cargarProceso(listos[0])
            listos.pop(0)
        elif(listos):
            if(cpu.proceso.ti > listos[0].ti):
                listos.append(cpu.proceso)
                cpu.quitarProceso()
                cpu.cargarProceso(listos[0])   
                listos.pop(0)   
                #Agregar a listos el proceso saliente de la cpu
        listos = sorted(listos, key = lambda proc: proc.ti)
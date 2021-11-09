class planifCorto: 

    def srtf(self,listos,cpu):
        if cpu.proceso:
            if cpu.proceso.ti == 0:
                cpu.quitarProceso()
                # listos.pop(0)
                
        if (cpu.proceso == None and listos):
            cpu.cargarProceso(listos[0])
            listos.pop(0)

        elif(listos):
            if(cpu.proceso.ti > listos[0].ti):
                cpu.quitarProceso()
                cpu.cargarProceso(listos[0])   
                listos.pop(0)   
                #Agregar a listos el proceso saliente de la cpu
        listos = sorted(listos, key = lambda proc: proc.ti)
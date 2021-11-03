class planifCorto: 
    def __init__ (self):
        pass

    def srtf(self,listos,cpu):
        if cpu.proceso:
            if cpu.proceso.ti == 0:
                cpu.quitarProceso()
        if (cpu.proceso == None and listos):
            cpu.cargarProceso(listos[0])
        elif(listos):
            if(cpu.proceso.ti > listos[0].ti):
                cpu.quitarProceso()
                cpu.cargarProceso(listos[0])       
        if listos:
            listos.pop(0)
            listos = sorted(listos, key = lambda proc: proc.ti)

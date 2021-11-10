class Cpu():
    def __init__(self):
        self.proceso = None
    
    def cargarProceso(self, proceso):
        self.proceso = proceso
        proceso.estado = "Ejecutando"
    
    def quitarProceso(self):
        self.proceso = None

    def getData(self):
        if self.proceso:
            return f"Proceso en ejecucion--> id: {self.proceso.id} Tiempo de irrupcion: {self.proceso.ti}"
        else:
            return f"No hay proceso en ejecucion"
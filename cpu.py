class Cpu():
    def __init__(self):
        self.proceso = None
    
    def cargarProceso(self, proceso):
        self.proceso = proceso
    
    def getData(self):
        if self.proceso != None:
            return f"Proceso en ejecucion: {self.proceso}"
        else:
            return f"No hay proceso en ejecucion"
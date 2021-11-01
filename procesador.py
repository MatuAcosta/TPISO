class Procesador: 
    def __init__(self):
        self.proceso = None
        pass
    def getProceso (self):
        return self.proceso

    def agregarProceso (self,proceso): 
        if (self.proceso==None): 
            self.proceso = proceso
    def quitarProceso (self): 
        if (self.proceso!=None):
            self.proceso = None

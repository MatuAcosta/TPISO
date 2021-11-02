from proceso import Proceso
class Particion:
    def __init__(self, id, tamano, dirInicio, fragmentacion, estado = 'Libre'):
        self.id = id
        self.tamano = tamano
        self.dirInicio = dirInicio
        self.fragmentacion = fragmentacion
        self.estado = estado
        self.proceso = None
    
    def cargarProceso(self, proceso):
        self.proceso = proceso
        self.fragmentacion = self.tamano - proceso.getTamaño()
        self.estado= 'Ocupado'
        self.proceso.estado = "Listo"

    def getTamaño(self):
        return self.tamano

    def getData(self):
        if self.proceso == None:
            return f"idParticion: {self.id} Tamaño: {self.tamano}, dirInicio: {self.dirInicio}, Fragmentacion: {self.fragmentacion}, estado: {self.estado}, idProceso: Vacio"
        else:
            return f"idParticion: {self.id}, Tamaño: {self.tamano}, dirInicio: {self.dirInicio}, Fragmentacion: {self.fragmentacion}, estado: {self.estado}, idProceso: {self.proceso.getId()}"
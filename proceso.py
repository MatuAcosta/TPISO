class Proceso():
    def __init__(self, id, tamano, ta, ti):
        self.id = id
        self.tamano = tamano
        self.ta = ta
        self.ti = ti
        self.estado = "nuevo"

    def getEstado(self):
        return self.estado
    def getId(self):
        return self.id
    def getTamaño(self):
        return self.tamano
    def getTa(self):
        return self.ta    
    def getData(self):
        return  f'id: {str(self.id)} tamaño: {str(self.tamano)} ta: {str(self.ta)} ti: {self.ti}' 

    def calcTR(self,reloj):
        return reloj - self.ta 
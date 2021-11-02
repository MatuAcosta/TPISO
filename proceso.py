class Proceso():
    def __init__(self, id, tamano, ta, ti):
        self.id = id
        self.tamano = tamano
        self.ta = ta
        self.ti = ti
    
    def getId(self):
        return self.id
    def getTamaño(self):
        return self.tamano
    def getTa(self):
        return self.ta    
    def getData(self):
        return  f'id: {str(self.id)} tamaño: {str(self.tamano)} ta: {str(self.ta)} ti: {self.ti}' 


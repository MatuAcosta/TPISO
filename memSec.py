from proceso import Proceso 
class memoriaSec: 
    def __init__(self):
        self.procSusp = []

    def getProcesos (self):
        return self.procSusp

    def agregarProceso(self,proceso):
        self.procSusp.append(proceso)
        return self.procSusp

    def quitarProceso (self,proceso): 
        self.procSusp.remove(proceso)

    def hayProceso(self):
        if self.procSusp == []:
            return False
        else:
            return True

#---------PRUEBA-------
#disco = memoriaSec ()
#for x in range (5): 
#    proceso = Proceso (x,100,2,x+1)
#    disco.agregarProceso(proceso)

#disco.mostrarDisco()
#ti = 10000
#proc = disco.getProcesos()

#eliminar = None
#for proceso in proc: 
#    if (ti>proceso.ti): 
#        ti = proceso.ti
#        eliminar = proceso

#disco.quitarProceso(eliminar)
#disco.mostrarDisco()

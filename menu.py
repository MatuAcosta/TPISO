from so import SistemaOperativo

class Menu:
    def mostrarOpcionesCarga(self):
        print(
            """
            --------------------------------------------------------------
            SIMULADOR DE ASIGNACION DE MEMORIA Y PLANIFICACION DE PROCESOS
            --------------------------------------------------------------
                                CARGA DE PROCESOS

            1- Carga Manual
            2- Carga Aleatoria
            3- Salir
            """
        )
        opcion = int(input("Ingresar opcion: "))
        return opcion

    def mostrarProcesos(self, opcion):
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
    def cargaManual():
        file = open()
        cantprocesos = int(input("Ingresar cantidad de procesos a crear"))
        i = 0
        while cantprocesos > 0:
            id = i
            tamaño = int(input("Ingresar tamaño"))
            while(controlarTamaño(tamaño)):
                tamaño = int(input("Ingresar tamaño"))
            ta = int(input("Ingresar tiempo de arribo: "))
            ti = int(input("Ingresar tiempo de irrupcion"))
            cantprocesos -= 1

    def controlarTamaño(tamaño):
        if tamaño > 250:
            print("El tamaño del proceso es mayor al tamaño maximo (250)")
            return True
        return False
menu = Menu()
menu.mostrarOpciones()

from lista import lista 

procesos = lista ()

for i in range (1,10):
    proceso = {
        'id': i, 
        'tamano': 150,
        'ta': i,
        'ti': i+1
    }
    procesos.insert(proceso)


procesos.imprimir()
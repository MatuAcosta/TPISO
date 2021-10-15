from nodo import nodo

class lista: 
    def __init__(self):
        self.head = None
    
    # Método para agregar elementos al final de la linked list (cola)
    def insert(self, data):
        if not self.head:
            self.head = nodo(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = nodo(data)
    
    def imprimir(self):
        node = self.head
        while node != None:
            print( node.data)            
            node = node.next
        print('Null')
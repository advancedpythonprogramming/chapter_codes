class Nodo:
    def __init__(self, valor=None):
        self.siguiente = None
        self.valor = valor

class ListaLigada:
    def __init__(self):
        self.cola = None
        self.cabeza = None

    def agregar_nodo(self, valor):
        if not self.cabeza:
            self.cabeza = Nodo(valor)
            self.cola = self.cabeza
        else:
            self.cola.siguiente = Nodo(valor)
            self.cola = self.cola.siguiente

    def obtener(self, posicion):
        nodo = self.cabeza
        
        for i in range(posicion):
            if nodo:
                nodo = nodo.siguiente
        if not nodo:
            return "posicion no encontrada"
        else:
            return nodo.valor

    def __repr__(self):
        rep = ''
        nodo_actual = self.cabeza
        
        while nodo_actual:
            rep += '{0}->'.format(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        
        return rep
    
l = ListaLigada()
l.agregar_nodo(2)
l.agregar_nodo(4)
l.agregar_nodo(7)

print(l.obtener(2))
print(l.obtener(1))

print(l)
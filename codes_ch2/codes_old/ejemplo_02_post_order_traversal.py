class ArbolPostOrder(Arbol):
    # Heredamos de la clase original del Arbol e implementamos 
    # el PostOrder para el recorrido del arbol
    
    def __repr__(self):
        def recorrer_arbol(raiz):
            # primero recorremos recursivamente los hijos
            for hijo in raiz.hijos.values():
                recorrer_arbol(hijo)
            
            # Finalmente visitamos el nodo raíz
            string = "nodo_id: {}, id_padre: {} -> valor: {}\n"
            self.ret += string.format(raiz.id_nodo, raiz.id_padre, raiz.valor)
            return self

        self.ret = ''
        recorrer_arbol(self)
        return self.ret
    
# Poblamos el árbol usando los mismo datos que en el caso original
T = ArbolPostOrder(0, 10)
T.agregar_nodo(1, 8, 0)
T.agregar_nodo(2, 12, 0)
T.agregar_nodo(3, 4, 1)
T.agregar_nodo(4, 4, 1)
T.agregar_nodo(5, 1, 3)
T.agregar_nodo(6, 18, 2)

print(T)
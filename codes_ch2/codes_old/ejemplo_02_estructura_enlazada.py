

class Nodo:

    def __init__(self, valor, padre=None):
        self.valor = valor
        self.padre = padre
        self.hijo_izquierdo = None
        self.hijo_derecho = None

    def __repr__(self):
        return 'padre: {0}, valor: {1}'.format(self.padre, self.valor)


class ArbolBinario:

    def __init__(self, nodo_raiz=None):
        self.nodo_raiz = nodo_raiz

    def agregar_nodo(self, valor):
        if self.nodo_raiz == None:
            self.nodo_raiz = Nodo(valor)
        else:
            temp = self.nodo_raiz
            agregado = False

            while not agregado:
                if valor <= temp.valor:
                    if temp.hijo_izquierdo == None:
                        temp.hijo_izquierdo = Nodo(valor, temp.valor)
                        agregado = True

                    else:
                        temp = temp.hijo_izquierdo

                else:
                    if temp.hijo_derecho == None:
                        temp.hijo_derecho = Nodo(valor, temp.valor)
                        agregado = True

                    else:
                        temp = temp.hijo_derecho

    def __repr__(self):
        def recorrer(nodo, lado="r"):
            ret = ''

            if nodo != None:
                ret += '{0} -> {1}\n'.format(nodo, lado)
                ret += recorrer(nodo.hijo_izquierdo, 'i')
                ret += recorrer(nodo.hijo_derecho, 'd')

            return ret

        ret = recorrer(self.nodo_raiz)
        return ret


T = ArbolBinario()
T.agregar_nodo(4)
T.agregar_nodo(1)
T.agregar_nodo(5)
T.agregar_nodo(3)
T.agregar_nodo(20)

print(T)

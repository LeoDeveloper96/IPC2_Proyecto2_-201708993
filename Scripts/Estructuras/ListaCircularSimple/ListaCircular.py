from Scripts.Estructuras.ListaCircularSimple.Nodo import Nodo


class ListaCircular:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertarNodo(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
            nuevo.siguiente = nuevo
        else:
            tmp = self.ultimo
            if tmp is not None:
                tmp.siguiente = nuevo
                self.ultimo = nuevo
                nuevo.siguiente = self.primero

    def imprimirNodo(self):
        tmp = self.primero
        while True:
            print(' Dato: ', tmp.dato)
            tmp = tmp.siguiente
            if tmp == self.primero:
                break

    def getDato(self, dato):
        tmp = self.primero
        while True:
            if tmp.dato == dato:
                return tmp
            tmp = tmp.siguiente
            if tmp == self.primero:
                return None

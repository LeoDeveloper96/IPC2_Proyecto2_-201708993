from Scripts.Estructuras.ListaEnlazadaDoble.Nodo import Nodo


class ListaDobleEnlazada:

    def __init__(self):
        self.cabeza = None

    def append(self, datos):
        if self.cabeza is None:
            nuevo_nodo = Nodo(datos)
            nuevo_nodo.anterior = None
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo = Nodo(datos)
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            nuevo_nodo.siguiente = None

    def preppend(self, datos):
        if self.cabeza is None:
            nuevo_nodo = Nodo(datos)
            nuevo_nodo.anterior = None
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo = Nodo(datos)
            self.cabeza.anterior = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            nuevo_nodo.anterior = None

    def imprimir_Lista(self):
        actual = self.cabeza
        while actual:
            print(actual.datos)
            actual = actual.siguiente
from Scripts.Estructuras.ListaEnlazadaSimple.LESScript import ListaEnlazada


class Pila:

    def __init__(self):
        self.elementos = ListaEnlazada()

    def push(self, datos):
        self.elementos.preppend(datos)

    def pop(self):
        if self.elementos.cabeza is None:
            return
        contador = 0
        temp = self.elementos.cabeza
        while temp:
            if temp.siguiente is None:
                break
            contador += 1
            temp = temp.siguiente
        self.eliminar_pos(contador)
        return temp

    def clear(self):
        pass

    def size(self):
        contador = 0
        iterador = self.elementos.cabeza
        while iterador:
            contador += 1
            iterador = iterador.siguiente
        return contador

    def top(self):
        pass

    def es_vacia(self):
        return self.size() == 0

    def eliminar_pos(self, indice):
        if indice < 0 or indice > self.size():
            raise Exception("Indice invalido")
        if indice == 0:
            self.elementos.cabeza = self.elementos.cabeza.siguiente
            return
        conteo = 0
        iterador = self.elementos.cabeza
        while iterador:
            if conteo == indice - 1:
                iterador.siguiente = iterador.siguiente.siguiente
                break
            iterador = iterador.siguiente
            conteo += 1

class Archivo:

    def __init__(self,nombre,metodo):
        self.archivo = open(nombre, metodo)

    def __enter__(self):
        return self.archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{exc_type},{exc_val},{exc_tb}")
        self.archivo.close()
        if type == Exception:
            return True



from pip._vendor.distlib.compat import raw_input
import re
import copy

from Scripts.Utilidades.Archivo import Archivo


class Menu:

    def menu(self):
        print("\n")
        print("1 Cargar mapa 2D")
        print("2 Misiones de rescate")
        print("3 Misiones de extraccion")
        print("4 Listar unidades chapinRescue")
        print("5 Listar unidades chapinFighter")
        print("6 Salir")
        entrada = input("Ingrese un numero 1-6" + "\n")
        patron = "[1-6]{1}"
        # cláusula de guarda
        if not re.search(patron, entrada): return self.menu()

        if entrada == "1":
            pass
        elif entrada == "2":
            pass
        elif entrada == "3":
            pass
        elif entrada == "4":
            pass
        elif entrada == "5":
            pass
        elif entrada == "6":
            raw_input("Presione una tecla" + "\n")

import os
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET

from Scripts.Utilidades.ContextManager import ContextManager


class Archivo:

    def cargarXMl(self):
        root = tk.Tk()
        root.withdraw()
        ruta = os.getcwd() + "\\Archivos prueba"
        nombre_archivo = filedialog.askopenfilename(initialdir=ruta, title="Seleccionar un archivo",
                                                    filetypes=(("texto", "*.xml"), ("todos", "*.*")))
        with ContextManager(nombre_archivo, "r", encoding="utf8") as f:
            arbol = ET.parse(nombre_archivo, parser=ET.XMLParser(encoding='iso-8859-5'))
            raiz = arbol.getroot()

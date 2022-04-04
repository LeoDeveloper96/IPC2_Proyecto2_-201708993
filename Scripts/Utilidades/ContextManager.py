import os
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET


class ContextManager:

    def __init__(self, nombre, metodo, encoding):
        self.archivo = open(nombre, metodo, encoding)

    def __enter__(self):
        return self.archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{exc_type},{exc_val},{exc_tb}")
        self.archivo.close()
        if type == Exception:
            return True



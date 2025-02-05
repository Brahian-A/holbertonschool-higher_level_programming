#!/usr/bin/python3
""" Clase que hereda las referencias de los atributos de la lista de clases"""

class MyList(list):


    def print_sorted(self):
        """Método que imprime la lista ordenada"""
        sorted = self.copy()
        sorted.sort()
        print(sorted)
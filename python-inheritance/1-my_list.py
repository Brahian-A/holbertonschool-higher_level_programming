#!/usr/bin/python3
""" Clase que hereda las referencias de los atributos de la lista de clases"""


class MyList(list):

    """Método que imprime la lista ordenada"""
    def print_sorted(self):
        print(sorted(self))

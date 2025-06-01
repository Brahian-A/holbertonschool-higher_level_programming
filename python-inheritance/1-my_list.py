#!/usr/bin/python3
"""Modulo que contiene la clase MyList"""


class MyList(list):
    """Clase que hereda list y agrega un metodo para imprimir lista ordenada"""
    def print_sorted(self):
        "metodo que imprime una lista ordenada"
        print(sorted(self))

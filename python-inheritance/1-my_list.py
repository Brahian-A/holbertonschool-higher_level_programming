#!/usr/bin/python3
"""Modulo que contiene la clase MyList"""


class MyList(list):

    def print_sorted(self):
        "metodo que imprime una lista ordenada"
        print(sorted(self))

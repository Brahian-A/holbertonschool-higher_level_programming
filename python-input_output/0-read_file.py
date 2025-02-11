#!/usr/bin/python3
""" modulo que lee un archivo de texto"""


def read_file(filename=""):
    """funcion que abre y printea el contenido de un archivo UTF8"""
    with open(filename) as contenido:
        return (print(contenido.read()))

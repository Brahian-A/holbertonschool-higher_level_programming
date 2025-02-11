#!/usr/bin/python3
""" modulo que lee un archivo de texto"""


def read_file(filename=""):
    """funcion que abre y printea el contenido de un archivo UTF8"""
    with open(filename, 'r') as contenido:
        print(contenido.read())

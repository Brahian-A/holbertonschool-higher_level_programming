#!/usr/bin/python3
""""modulo que escribe en un archivio"""


def write_file(filename="", text=""):
    """funcion que escribe en un archivo y retorna el contenido"""
    with open(filename, 'w') as contenido:
        return contenido.write(text)

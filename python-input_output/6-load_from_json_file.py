#!/usr/bin/python3
"""modulo que carga un objeto desde un archivo json"""

import json


def load_from_json_file(filename):
    """funcion que lee un archivo json y devuelve contenido como un objeto"""
    with open(filename, encoding='utf-8') as contenido:
        return (json.loads(contenido.read()))

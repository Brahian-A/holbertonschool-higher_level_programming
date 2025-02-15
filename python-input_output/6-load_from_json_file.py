#!/usr/bin/python3
"""modulo"""

import json


def load_from_json_file(filename):
    """funcion"""
    with open(filename, encoding='utf-8') as contenido:
        return (json.loads(contenido.read()))

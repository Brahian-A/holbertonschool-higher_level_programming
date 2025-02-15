#!/usr/bin/python3
"""modulo"""

import json


def load_from_json_file(filename):
    """funcion"""
    with open (filename, 'r') as contenido:
        data = json.loads(contenido)
        return data

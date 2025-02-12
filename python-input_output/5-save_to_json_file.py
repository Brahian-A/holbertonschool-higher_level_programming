#!/usr/bin/python3
""" modulo """

import json


def save_to_json_file(my_obj, filename):
    """ funcion """
    with open(filename, mode='w', encoding="utf-8")as contenido:
        contenido.write(json.dumps(my_obj))

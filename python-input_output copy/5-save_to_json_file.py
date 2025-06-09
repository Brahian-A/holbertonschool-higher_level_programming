#!/usr/bin/python3
""" modulo que guarda un objeto en formato json"""
import json


def save_to_json_file(my_obj, filename):
    """ funcion que guarda un objeto en formato json"""
    with open(filename, mode='w', encoding="utf-8")as contenido:
        contenido.write(json.dumps(my_obj))

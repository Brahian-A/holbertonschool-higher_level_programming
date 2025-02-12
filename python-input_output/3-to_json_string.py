#!/usr/bin/python3
""" modulo que importa json strings"""

import json


def to_json_string(my_obj):
    """funcion que retorna un json string con dumps"""
    return json.dumps(my_obj)

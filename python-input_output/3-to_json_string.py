#!/usr/bin/python3
""" modulo que implementa json"""
import json


def to_json_string(my_obj):
    """funcion que retorna un string json"""
    return json.dumps(my_obj)

#!/usr/bin/python3
"""modulo que devueve un string json """
import json


def from_json_string(my_str):
    """funcion que retorna un json lods """
    return json.loads(my_str)

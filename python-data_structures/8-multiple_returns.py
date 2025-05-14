#!/usr/bin/python3

def multiple_returns(sentence):
    """funcion que devuelve una tupla con
    el largo del string y el primer caracter"""
    if len(sentence) == 0:
        return None
    return [len(sentence), sentence[0]]

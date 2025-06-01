#!/usr/bin/python3
"""Modulo que contiene la funcion is_same_class"""

def is_same_class(obj, a_class):
    """retorna True si obj es una instancia de a_class"""
    return type(obj) is a_class

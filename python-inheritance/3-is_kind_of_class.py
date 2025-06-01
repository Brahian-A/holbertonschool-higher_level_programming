#!/usr/bin/python3

"""Modulo que contiene la funcion is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """retorna obj es una instancia de a_class o de una clase"""
    return isinstance(obj, a_class)

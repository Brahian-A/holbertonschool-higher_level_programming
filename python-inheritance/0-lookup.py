#!/usr/bin/python3
""" Modulo que contiene la funcion lookup """

def lookup(obj):
    """retorna una lista con todos los metodos y atributos de un objeto"""
    return dir(obj)

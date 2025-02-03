#!/usr/bin/python3

""" definimos una funcion que busca los atributos de un objeto"""


def lookup(obj):
    """ retorna una lista con todos los atributos"""
    return (dir(obj))
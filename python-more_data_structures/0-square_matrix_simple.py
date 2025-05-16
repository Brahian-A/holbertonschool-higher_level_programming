#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nueva_matriz = []
    for fila in matrix:
        nueva_fila = []
        for i in fila:
            nueva_fila.append(i * i)
        nueva_matriz.append(nueva_fila)
    return nueva_matriz

#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    " Validación de que la matriz es una lista de listas"
    # y que cada elemento es un entero o un flotante
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(
            isinstance(elem, (int, float)) for elem in row
        ):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    # Validación de que cada fila tiene el mismo tamaño
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Validación de que el divisor es un entero o un flotante y no cero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # nueva matriz dividida por el divisor y se redondea a 2 decimales
    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)

    return new_matrix

#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        return (None)
    longitud = len(sentence)
    primer_c = sentence[0]
    return (longitud, primer_c)

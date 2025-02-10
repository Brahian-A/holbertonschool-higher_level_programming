#!/usr/bin/env python3

class CountedIterator():
    def __init__(self, object):
        self.__iter = iter(object)
        self.__counter = 0

    def get_count(self):
        return self.__counter
    
    def __next__(self):
        self.__counter += 1
        return next(self.__iter)
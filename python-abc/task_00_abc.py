#!usr/bin/python3
from abc import ABC, abstractclassmethod
"""Creamos una clase abstracta con
un metodo sound"""

class Animal(ABC):
    @abstractclassmethod
    def sound(self):
        pass


class Dog(Animal):
   def sound(self):
        return 'Bark'


class Cat(Animal):
    def sound(sefl):
        return 'Meow'

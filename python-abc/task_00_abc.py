#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""clase abstracta"""

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return 'Bark'

class Cat(Animal):
    def sound(self):
        return 'Meow'
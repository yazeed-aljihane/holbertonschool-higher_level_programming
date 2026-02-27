#!/usr/bin/python3
class hero:
    def __init__(self, name=None):
        self.name = name
        self.__name2 = name
        self._name3 = name


hero = hero("yazeed")
print(hero.name3)

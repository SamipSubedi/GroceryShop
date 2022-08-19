from Database import *


class Shop:
    def __init__(self, name,):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


s1 = Shop('Grocery')
print('WELCOME TO ' + s1.name + ' Store')

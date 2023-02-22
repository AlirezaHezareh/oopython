#!/usr/bin/env python3

"""
yatzee1 dice 
"""
# Importera relevanta moduler
import random

#Denna klassen ska representera tärning.
class Die():
    #statiska attribud för classen Die
    MIN_ROLL_VALUE = 1 # publikt statiskt attribut
    MAX_ROLL_VALUE = 6 # publikt statiskt attribut
    def __init__(self, _value=None, MIN_ROLL_VALUE=1, MAX_ROLL_VALUE=7):
        self._value = _value
    def get_value(self, _value=None):
        if _value is not None:
            if _value < self.MIN_ROLL_VALUE:
                self._value = self.MIN_ROLL_VALUE
            elif _value > self.MAX_ROLL_VALUE:
                self._value = self.MAX_ROLL_VALUE
        else:
            self._value = random.randrange(self.MIN_ROLL_VALUE,self.MAX_ROLL_VALUE)
        #print('get_value:', self._value)
        return self._value
    def get_name(self):
        name = ['one', 'two', 'three', 'four', 'five', 'six']
        #print('get_name: ', end='')
        return name[self-1]
    def roll():
        return Die.get_value(Die())
        """ kasta = Die.get_value(Die())
            print(kasta) 
        """
    def __str__(self):
        #__str__() ska returnera värdet som tärningen har som en sträng.
        print('__str__', end='')
        return str(self.get_name())



objekt = Die.get_name(Die.roll())
print(Die.get_value(Die()))
#print(objekt)
objekt_som_str = objekt.__str__()
#print(objekt_som_str, type(objekt_som_str))

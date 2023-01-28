from random import *

class Dice:

    __number_of_sides: int = -1 # Anzahl der Seiten entspricht hier den möglichen Augenzahlen Bsp. 6 Seiten entspricht den Augenzahl 1 bis 6
    __diceResult: int = -1

    def __init__(self, number_of_sides):
        self.__number_of_sides = number_of_sides

    def getResult(self):
        if self.__diceResult == -1:
            raise Exception("Es wurde noch nicht gewürfelt.")
        return self.__diceResult

    def roll(self):
        if self.__number_of_sides == -1:
            raise Exception("Bitte bestimmen Sie zunächst die Anzahl der Seiten des Würfels.")
        self.__diceResult = randint(1, self.__number_of_sides) #6 Seiten entspricht den Augenzahl 1 bis 6
        return self

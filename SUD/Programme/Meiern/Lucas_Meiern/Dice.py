from random import *


class Dice:
    def __init__(self, number_of_sides):
        # Anzahl der Seiten entspricht hier den möglichen Augenzahlen Bsp. 6 Seiten entspricht den Augenzahl 1 bis 6
        self.__number_of_faces= number_of_sides

    def getResult(self):
        if self.__result == -1:
            raise Exception("Es wurde noch nicht gewürfelt.")
        return self.__result

    def roll(self):
        if self.__number_of_faces == -1:
            raise Exception("Bitte bestimmen Sie zunächst die Anzahl der Seiten des Würfels.")
        self.__result = randint(1, self.__number_of_faces)  # 6 Seiten entspricht den Augenzahl 1 bis 6
        return self

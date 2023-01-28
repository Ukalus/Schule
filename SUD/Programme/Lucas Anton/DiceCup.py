import numpy
from Dice import Dice

class DiceCup:
    __dice: Dice[]

    def __init__(self, number_of_faces: int):
        pass
    def roll(self):
        result: int 
        for die in Dice:
            die.roll()
    def format(self) -> int:
        self.__dice = []
    def getDice(self):
        return self.__dice

import numpy
from Dice import Dice


class DiceCup:
    ''' Creates a dice cup that manages the rolling of an arbitary number of dice dice'''
    __dice: Dice[]

    def __init__(self, die dice[]):
        '''
        initialises a Dicecup Object
        parameters:
        dice: array of dice that you you put in the cup
        '''
        pass
    def roll(self):
        '''rolls every dice that was previously added'''
        result: int 
        for die in Dice:
            die.roll()
        
    def format(self) -> int:
        '''empties the dice cup'''
        self.__dice = []
    def getDice(self):
        '''returns an array of all the dice '''
        return self.__dice

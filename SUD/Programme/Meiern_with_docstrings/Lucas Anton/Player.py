class Player:
    '''Player object class'''
    __name: str
    __points = 0 # Achtung, je weniger Punkte desto besser

    def __init__(self, name):
        '''initializes a player'''
        self.__name = name

    def getName(self):
        '''returns player name'''
        return self.__name

    def addPoints(self, points = 1):
        '''adds points to player'''
        self.__points += points
        return self

    def getPoints(self):
        '''returns player points'''
        return self.__points
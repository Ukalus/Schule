class Player:
    __name: str
    __points = 0  # Achtung, je weniger Punkte desto besser

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def addPoints(self, points=1):
        self.__points += points
        return self

    def getPoints(self):
        return self.__points

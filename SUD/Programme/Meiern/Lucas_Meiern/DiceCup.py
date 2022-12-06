from Dice import Dice


class DiceCup:
    def __init__(self, number_of_faces: int):
        self.__number_of_faces = number_of_faces
        self.__dice = [Dice(self.__number_of_faces), Dice(self.__number_of_faces)]

    def __getDice(self):
        if not self.__dice:
            raise Exception("keine Würfel klasse definiert.")
        return self.__dice

    def roll(self):
        for dice in self.__getDice():
            dice.roll()
        return self.__dice

    # concat the dice values in a single integer (sorted)
    def format(self):
        result_list = []
        result = ""
        for dice in self.__getDice():
            result_list.append(dice.getResult())
        result_list.sort(reverse=True)
        for digit in result_list:
            result = result + str(digit)
        return int(result)

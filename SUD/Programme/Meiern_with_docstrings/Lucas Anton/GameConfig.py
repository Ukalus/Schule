import random

class GameConfig:
    '''Game config class (settings)'''
    ZERO_PLAYERS_RESPONSES = (
            "Ernsthaft? Ein Null-Spieler-Spiel?!",
            "Warum starten Sie ein Spiel, dass Sie selbst nicht spielen wollen?"
        )

    ONE_PLAYER_RESPONSES = (
            "Error 404: Friends not found!",
            "Suchen Sie sich doch Freunde."
        )

    __possible_results = []
    __number_of_faces: int = 6
    __player_names = []

    def setup(self):
        '''settings IO (ran before the game starts)'''
        print("""
        #################################
        # Starte den Spielaufbau #
        #################################

        """)

        number_of_faces = input("\nBitte geben Sie die Anzahl der Würfelseiten ein, die die Würfel haben sollen(3-9)\nFür einen Standardwürfel drücken Sie einfach ENTER: ")
        if number_of_faces != "":
            self.__number_of_faces = max(3, min(9, int(number_of_faces)))
            self.generatePossibleResults(number_of_faces)
        else:
            self.generatePossibleResults(self.__number_of_faces)

        print("\nBitte geben Sie die Namen der Spieler einzeln ein und bestätigen jeden Namen mit einem ENTER. Um die Spielereingabe zu beenden drücken Sie einfach ENTER.\n")
        while True:
            player_name = input("> ")
            if "" == player_name:
                if self.__player_names.__len__() == 0:
                    print("\n" + random.choice(self.ZERO_PLAYERS_RESPONSES) + "\n")
                    continue
                elif self.__player_names.__len__() == 1:
                    print("\n" + random.choice(self.ONE_PLAYER_RESPONSES) + "\n")
                    continue
                else:
                    break
            self.__player_names.append(player_name)

        print("\nEs wurden ", self.__player_names.__len__()), " Spieler registriert."

        return self

    def getPossibleResults(self):
        return self.__possible_results

    def getNumberOfFaces(self):
        return self.__number_of_faces

    def getPlayerNames(self):
        return self.__player_names

    
    def generatePossibleResults(self, number_of_faces: int):
        '''This generates a list with all of the possible results with the given number of faces on the dice, sorted by value'''
        for digit1 in range(1, int(number_of_faces) + 1):
            if (digit1 == 1) or (digit1 == 2):
                continue
            for digit2 in range(1, digit1):
                self.__possible_results.append(10 * digit1 + digit2)

        for digit in range(1, int(number_of_faces) + 1):
            self.__possible_results.append(11 * digit)

        self.__possible_results.append(21)

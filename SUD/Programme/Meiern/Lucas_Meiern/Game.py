import random
import signal
import sys
from time import sleep
from Player import Player
from DiceCup import DiceCup
from GameConfig import GameConfig
from Dice import Dice


class Game:
    # Definiert eine Antwort als Hinweis für einen schlechten Spielzug
    BAD_CHOICE_RESPONSES = (
        "Ich will Ihnen helfen zu gewinnen. Daher mein Tipp: Das ist keine gute Antwort. Probieren Sie etwas anderes.",
    )

    # Initialisierung der Klassenattribute
    __config: GameConfig = None
    __playerNames = []
    __dice_cup: DiceCup = None
    __current_call: int = -1

    __dice = []

    # Init-Methode und Instanzattribut-Initialisierung und Deklaration
    def __init__(self, config):
        self.__config = config

        for player_name in config.getPlayerNames():
            self.__playerNames.append(Player(player_name))

        numberOfSides = config.getNumberOfFaces()
        self.__dice_cup = DiceCup(numberOfSides)

        self.play()  # Starte das Spiel

    def play(self):
        print("""
        #################################
        # Spielstart #
        #################################

        In dieser Version ist auch das niedriger Lügen nicht erlaubt.

        Der letzte Spieler >>>   """ + self.__playerNames[-1].getName() + """   <<< startet und würfelt...
        """)

        self.__dice_cup.roll()

        print("Du hast gewürfelt:", self.__dice_cup.format())

        self.__call(self.__playerNames[-1])

        while True:  # Loops every round
            for player in self.__playerNames:  # Iterates over all players
                while True:  # Loops until turn is completed
                    print("\n\n>>>  " + player.getName() + "  <<<, Sie sind an der Reihe!\n")
                    print("Drücken Sie [X] um anzuzweifeln.")
                    if self.__current_call != 21:
                        print("Drücken Sie [C] um zu Würfeln.")
                        print("Drücken Sie [V] um eine Zahl zu sagen, ohne zu würfeln.")
                    print("Drücken Sie [B] um die Punkte anzuzeigen.")
                    decision = input("\nWas möchten Sie nun tun? ")
                    print("\n")

                    if decision == "X" or decision == "x":
                        self.__doubt(player)
                        break
                    elif decision == "C" or decision == "c" or decision == "V" or decision == "v":
                        # When current call is 21, don't enter call function, that would cause a deadlock
                        if self.__current_call == 21:
                            print("Sie können keine neue Zahl ansagen, als das Maximum 21")
                            continue
                        if decision == "C" or decision == "c":
                            self.__dice_cup.roll()  # mit Würfelbecher
                            print("Sie haben folgendes gewürfelt:", self.__dice_cup.format())
                        self.__call(player)
                        break
                    elif decision == "B" or decision == "b":
                        self.__showScores()
                    else:
                        # Error message
                        print(random.choice(self.BAD_CHOICE_RESPONSES))

    # Ausrufen einer Zahl >= der gewürfelten Zahl
    def __call(self, player: Player):
        while True:
            # Short names so the conditionals are not so long
            pr = self.__config.getPossibleResults()
            cc = self.__current_call
            nc_string = input("Welches Ergebnis wollen Sie ansagen? ")

            # Print an error, if the given number is not an integer
            if not nc_string.isdigit():
                print("Bitte geben Sie eine Zahl ein!\n")
                continue
            nc = int(nc_string)

            # Check, whether the given call is valid or not
            # and checks if the call is higher than the last (Exception: First call),
            # as otherwise would not make any sense
            if nc in pr:
                if cc == -1 or pr.index(nc) > pr.index(cc):
                    break
                print("Sind Sie sicher?: Sollten Sie nicht eine Zahl ansagen die höher ist als die, "
                      "die Sie gewürfelt haben?.\n")
            print(random.choice(self.BAD_CHOICE_RESPONSES) + "\n")

        self.__current_call = nc
        print((50 * "\n") + "Spieler", player.getName(), "sagt:", nc)  # inserts 50 new lines and announces new call
        return self

    def __doubt(self, player: Player):
        pr = self.__config.getPossibleResults()  # Short variable name so the conditional is not so long

        if pr.index(self.__current_call) <= pr.index(self.__dice_cup.format()):
            player.addPoints()
            print("\nSie lagen falsch! Die richtige Zahl war:", self.__dice_cup.format())  # mit Würfelbecher
            print("Sie kriegen 1 Strafpunkt!")
        else:
            self.__playerNames[self.__playerNames.index(player) - 1].addPoints()
            print("\nSie lagen richtig! Die Zahl war:", self.__dice_cup.format())  # mit Würfelbecher
            print("Der Lügner (" + self.__playerNames[
                self.__playerNames.index(player) - 1].getName() + ") wird mit einem 1 Strafpunkt bestraft!")
        self.__showScores()

        input("Drücken Sie ENTER, um eine neue Runde zu starten.\n")
        self.__current_call = -1
        self.__dice_cup.roll()  # mit Würfelbecher

        print("Die Würfel sind gefallen und Sie haben folgendes gewürfelt:", self.__dice_cup.format())
        self.__call(player)
        return self

    def __showScores(self):
        print("""
        _____________________________
        # Punktestand #
        _____________________________
        """)

        # Huge and complicated code to vertically align the scores with different name lengths
        longest_name_length = 0
        most_point_digits = 0

        for player in self.__playerNames:
            longest_name_length = max(player.getName().__len__(), longest_name_length)
            most_point_digits = max(len(str(player.getPoints())), most_point_digits)

        for player in self.__playerNames:
            added_spaces = (longest_name_length - player.getName().__len__()) * " "
            added_spaces += (most_point_digits - len(str(player.getPoints()))) * " "
            print(player.getName() + ": " + added_spaces + str(player.getPoints()))

        print("")  # Print a new line
        return self

# Don't print python error message when Ctrl+C has been pressed
def sigint_handler(signal, frame):
    print('\n\nBis zum nächsten Mal!')
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)

# --------------------Instanziierung des Konfigurations-Objektes und Setup des Spiels
GConfig = GameConfig().setup()  # Starte zunächst den Spielaufbau und gib das konfigurierte Objekt zurück

# --------------------Instanziierung eines Game-Objektes und Start des Spiels
G1 = Game(GConfig)

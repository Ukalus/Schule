
import random
import signal
import sys
from time import sleep
from Player import Player
#from DiceCup import DiceCup #  Nur notwendig, wenn auch eine Würfelbecherklasse vorhanden ist
from GameConfig import GameConfig
from Dice import Dice
from DiceCup import DiceCup

class Game:

    BAD_CHOICE_RESPONSES = (
            "Ich will Ihnen helfen zu gewinnen. Daher mein Tipp: Das ist keine gute Antwort. Probieren Sie etwas anderes.",
            )

    __config: GameConfig = None
    __players = [] 
    __dice_cup = DiceCup
    #__dice_cup: DiceCup = None  # Nur notwendig, wenn  auch eine Würfelbecherklasse vorhanden sein soll
    __current_call: int = -1

   


    def __init__(self, config):
        self.__config = config
        

        for player_name in config.getPlayerNames():
            self.__players.append(Player(player_name))
        
        numberOfSides = config.getNumberOfFaces()
        #self.__dice_cup = DiceCup(numberOfSides) #  Nur notwendig, wenn auch eine Würfelbecherklasse vorhanden ist

        self.createDice()

        self.play() #Starte das Spiel



    def play(self):
        print("""
        #################################
        # Spielstart #
        #################################

        In dieser Version ist auch das niedriger Lügen nicht erlaubt.

        Der letzte Spieler >>>   """ + self.__players[-1].getName() + """   <<< startet und würfelt...
        """)

        #self.__dice_cup.roll()
        self.roll()

        #print("Du hast gewürfelt:", self.__dice_cup.format())
        print("Sie haben gewürfelt:", self.format())

        self.call(self.__players[-1])

        while True: # Loops every round
            for player in self.__players: # Iterates over all players
                while True: # Loops until turn is completed
                    print("\n\n>>>  " + player.getName() + "  <<<, Sie sind an der Reihe!\n")
                    print("Drücken Sie [X] um anzuzweifeln.")
                    if self.__current_call != 21:
                        print("Drücken Sie [C] um zu Würfeln.")
                        print("Drücken Sie [V] um eine Zahl zu sagen, ohne zu würfeln.")
                    print("Drücken Sie [B] um die Punkte anzuzeigen.")
                    decision = input("\nWas möchten Sie nun tun? ")
                    print("\n")

                    if decision == "X" or decision == "x":
                        self.doubt(player)
                        break
                    elif decision == "C" or decision == "c" or decision == "V" or decision == "v":
                        # When current call is 21, don't enter call function, that would cause a deadlock
                        if self.__current_call == 21:
                            print("Sie können keine neue Zahl ansagen, als das Maximum 21")
                            continue
                        if decision == "C" or decision == "c":
                            # self.__dice_cup.roll() # mit Würfelbecher
                            self.roll()
                            #print("Sie haben folgendes gewürfelt:", self.__dice_cup.format())
                            print("Sie haben folgendes gewürfelt:", self.format())
                        self.call(player)
                        break
                    elif decision == "B" or decision == "b":
                        self.showScores()
                    else:
                        # Error message
                        print(random.choice(self.BAD_CHOICE_RESPONSES))


    def call(self, player: Player):
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
                print("Sind Sie sicher?: Sollten Sie nicht eine Zahl ansagen die höher ist als die, die Sie gewürfelt haben?.\n")
            print(random.choice(self.BAD_CHOICE_RESPONSES) + "\n")

        self.__current_call = nc
        print((50 * "\n") + "Spieler", player.getName(), "sagt:", nc) # inserts 50 new lines and announces new call
        return self


    def doubt(self, player: Player):
        pr = self.__config.getPossibleResults() # Short variable name so the conditional is not so long

        #if pr.index(self.__current_call) <= pr.index(self.__dice_cup.format()):
        if pr.index(self.__current_call) <= pr.index(self.format()):
            player.addPoints()
            #print("\nSie lagen falsch! Die richtige Zahl war:", self.__dice_cup.format()) # mit Würfelbecher
            print("\nSie lagen falsch! Die richtige Zahl war:", self.format())
            print("Sie kriegen 1 Strafpunkt!")
        else:
            self.__players[self.__players.index(player) - 1].addPoints()
            #print("\nSie lagen richtig! Die Zahl war:", self.__dice_cup.format()) # mit Würfelbecher
            print("\nSie lagen richtig! Die Zahl war:", self.format())
            print("Der Lügner (" + self.__players[self.__players.index(player) - 1].getName() + ") wird mit einem 1 Strafpunkt bestraft!")
        self.showScores()

        input("Drücken Sie ENTER, um eine neue Runde zu starten.\n")
        self.__current_call = -1
        #self.__dice_cup.roll() #mit Würfelbecher #Falls es eine Würfelbecher geben sollte.
        self.roll()
        
        #print("Die Würfel sind gefallen und Sie haben folgendes gewürfelt:", self.__dice_cup.format()) #Falls es eine Würfelbecher geben sollte.
        print("Die Würfel sind gefallen und Sie haben folgendes gewürfelt:", self.format())
        self.call(player)
        return self


    def showScores(self):
        print("""
        _____________________________
        # Punktestand #
        _____________________________
        """)

        # Huge and complicated code to vertically align the scores with different name lengths
        longest_name_length = 0
        most_point_digits = 0

        for player in self.__players:
            longest_name_length = max(player.getName().__len__(), longest_name_length)
            most_point_digits = max(len(str(player.getPoints())), most_point_digits)

        for player in self.__players:
            added_spaces = (longest_name_length - player.getName().__len__()) * " "
            added_spaces += (most_point_digits - len(str(player.getPoints()))) * " "
            print(player.getName() + ": " + added_spaces + str(player.getPoints()))

        print("") # Print a new line
        return self



    # Statt in der Würfelbecher-Klasse ist dieser Code an dieser Stelle integriert---------------------------------------
    # Wenn es eine Würfelbecher-klasse geben sollte kann dieser Code dorthin kopiert UND angepasst werden.
    def createDice(self):
        diceCount = 2
        for i in range(diceCount):
            
            self.__dice_cup.append(Dice(self.__config.getNumberOfFaces()))

    def getDice(self):
        if not self.__dice_cup:
            raise Exception("Die Würfel müssen zuerst erzeugt werden, damit der Zugriff darauf klappt.")
        return self.__dice_cup

    def roll(self):
        for dice in self.getDice():
            dice.roll()
        return self.__dice_cup

    # Format the dice values in a single integer (sorted digits)
    def format(self):
        result_list = []
        result = ""
        for dice in self.getDice():
            result_list.append(dice.getResult())
        result_list.sort(reverse=True)
        for digit in result_list:
            result = result + str(digit)
        return int(result)
    #----------------------------------------------------------------------




# Don't print python error message when Ctrl+C has been pressed
def sigint_handler(signal, frame):
    print('\n\nBis zum nächsten Mal!')
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)



#--------------------Instanziierung des Konfigurations-Objektes und Setup des Spiels
GConfig = GameConfig().setup() # Starte zunächste den Spielaufbau und gib das konfigurierte Objekt zurück

#--------------------Instanziierung eines Game-Objektes und Start der Spiels
G1 = Game(GConfig)


from typing import List
from dataclasses import dataclass


@dataclass
class Silo: 
    siloId: int
    __kapazitaet: float
    __bestand: float

    def __init__(self, siloId: int, kapazitaet: float, bestand: float = 0):
        self.siloId = siloId
        self.__kapazitaet = kapazitaet
        self.__bestand = bestand

    def getSiloId(self):
        return self.siloId
    def getKapazitaet(self):
        return self.__kapazitaet
    def getBestand(self):
        return self.__bestand
    def getAllSiloInfo(self):
        return {"siloId": self.getSiloId(), "kapazitaet" : self.getKapazitaet(), "bestand" : self.getBestand()}
    def setKapazitaet(self, newKapazitaet):
        self.__kapazitaet = newKapazitaet
    def setBestand(self, newBestand):
        self.__bestand = newBestand
        
class SiloManager:
    __silos: List[Silo]

    def __init__(self, silos: Silo = []):
        self.__silos = silos

    def addSilo(self, silo: Silo | None = None):
        if silo:
            self.__silos.append(silo)
            print("you added The following Silo")
            print(silo.getAllSiloInfo())
            print("\n")
        else:
            print("oops")

        
    def removeSilo(self, siloId: Silo):
        activeSilo = list(filter(lambda x: x.siloId == siloId, self.__silos))[0]
        index_of = self.__silos.index(activeSilo)
        self.__silos.pop(index_of)
    def getAllSiloInfo(self):
        print("All current silos:")
        for silo in self.__silos:
            print(silo.getAllSiloInfo())
        print("\n")
    def changeBestand(self,siloId: int, changeValue):

        if changeValue == 0:
            print("please enter non null number")
            return changeValue

        activeSilo = list(filter(lambda x: x.siloId == siloId, self.__silos))[0]
        newBestand = activeSilo.getBestand() + changeValue
        if newBestand <= activeSilo.getKapazitaet():
            activeSilo.setBestand(newBestand)
            print("you added " + str(changeValue)) if changeValue > 0 else print("you removed " + str(changeValue))
        else:
            print("Kapazität: " + str(activeSilo.getKapazitaet()))
            print("new Bestand:" + str(newBestand))
            print("please enter a valid number")

        
        
# Testing 

silo1, silo2, silo3 = Silo(123,1000,400), Silo(124,2000,300),Silo(125,1500,0)

siloManager = SiloManager([silo1,silo2,silo3])
siloManager.getAllSiloInfo()

siloManager.changeBestand(124, 600)
siloManager.getAllSiloInfo()

newSilo = Silo(126,2000,2000)
siloManager.addSilo(newSilo)
siloManager.getAllSiloInfo()

siloManager.removeSilo(123)
siloManager.getAllSiloInfo()
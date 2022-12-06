
class WetterStation:
    __currentTemperature: float
    __minTemperature: float
    __maxTemperature: float
    __humidity: int   
    def __init__(self,__currentTemperature: float,minTemperature: float,maxTemperature: float,humidity: int):
        self.__currentTemperature = __currentTemperature
        self.__minTemperature = minTemperature
        self.__maxTemperature = maxTemperature
        self.__humidity = humidity

    def setCurrentTemperature(self,newCurrentTemp: float):
        self.__currentTemperature = newCurrentTemp
        self.__updateMinMaxTemperature(self)
    
    def setHumidity(self,newHumidity:float):
        self.__humidity = newHumidity
    def getCurrentTemperature(self):
        return self.__currentTemperature
    def getHumidity(self):
        return self.__humidity
    def getMinTemperature(self):
        return self.__minTemperature
    def getMaxTemperature(self):
        return self.__maxTemperature
    def __updateMinMaxTemperature(self):
        if self.__currentTemperature > self.__maxTemperature:
            self.__maxTemperature = self.__currentTemperature
        elif self.__currentTemperature < self.__minTemperature:
            self.__minTemperature = self.__currentTemperature
            
        

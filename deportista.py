import string


class Deportista:
    def __init__(self, deporte, añosPracticando):
        self.__deporte = deporte
        self.__añosPracticando = añosPracticando
        
    def setDeporte(self, deporte):
        self.__deporte = deporte
        
    def getDeporte(self):
        return self.__deporte
    
    def setañosPracticando(self, añosPracticando):
        self.__añosPracticando = añosPracticando
        
    def getAñosPracticando(self):
        return self.__añosPracticando
from deportista import Deportista
from persona import Persona


class Futbolista(Persona, Deportista):
    __listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self,nombre, edad, altura, sexo)
        Deportista.__init__(self,"Futbol", añosPracticando)
        self.__golesMarcados = golesMarcados
        self.__tarjetasRojas = tarjetasRojas
        self.__piernaHabil = piernaHabil
        Futbolista.__listaFutbolistas.append(self)
        
    def setGolesMarcados(self, golesMarcados):
        self.__golesMarcados = golesMarcados
        
    def getGolesMarcados(self):
        return self.__golesMarcados
    
    def setTarjetasRojas(self, tarjetasRojas):
        self.__tarjetasRojas = tarjetasRojas
        
    def getTarjetasRojas(self):
        return self.__tarjetasRojas
    
    def setPiernaHabil(self, piernaHabil):
        self.__piernaHabil = piernaHabil
        
    def getPiernaHabil(self):
        return self.__piernaHabil
    
    def __str__(self):
        return "Mi nombre es " + Persona.getNombre + " soy profesional en el deporte " + Deportista.getDeporte + " Tengo " + Persona.getEdad + " años de edad y  llevo " + Deportista.getAñosPracticando + " años en el deporte"
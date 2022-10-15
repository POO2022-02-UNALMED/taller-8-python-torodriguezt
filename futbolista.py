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
        return "Mi nombre es " + self.getNombre() + " soy profesional en el deporte " + self.getDeporte() + " Tengo " + str(self.getEdad()) + " años de edad y llevo " + str(self.getAñosPracticando()) + " años en el deporte"
    
    
if __name__ == "__main__":
    futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
    print(futbolista.__str__())

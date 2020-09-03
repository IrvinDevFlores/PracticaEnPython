from abc import ABC, abstractclassmethod

class Ecuacion(ABC):

    @abstractclassmethod
    def Calcular(cls, self):
        pass
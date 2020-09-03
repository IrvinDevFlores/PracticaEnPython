from ShareKernel.InputData import InputData
from math import pi
class VolumenEsfera:
    def __init__(self):
        super().__init__()
        self._inputData = InputData()


    def Ejecutar(self):
        radio = self._inputData.ObtenerValorNumerico("Ingrese el radio: ")
        volumen = (4/3)*pi*radio**3
        print(f"El volumen de la esfera es {volumen}")

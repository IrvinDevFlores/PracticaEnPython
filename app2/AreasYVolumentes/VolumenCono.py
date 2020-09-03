from ShareKernel.InputData import InputData
import math 
class VolumenCono:
    def __init__(self):
        super().__init__()
        self._inputData = InputData()
    
    def Ejecutar(self):
        radio = self._inputData.ObtenerValorNumerico("Ingrese el radio: ")
        altura = self._inputData.ObtenerValorNumerico("Ingrese el valor la altura: ")

        arg = (math.pi* math.pow(radio,2))
        volumen=(arg*altura)/3
        print(f"El volumen del cono es {volumen}")
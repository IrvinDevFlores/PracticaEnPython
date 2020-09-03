from ShareKernel.InputData import InputData
import math
class TiempoCaida:
    def __init__(self):
        super().__init__()
        self._inputData = InputData()

    def Ejecutar(self):
        altura = self._inputData.ObtenerValorNumerico("Ingrese la altura: ")
        

        arg = 2 * (altura/9.8)
        tiempo = math.sqrt(arg)
        print(f"el tiempo que tardo el objeto es {tiempo}")
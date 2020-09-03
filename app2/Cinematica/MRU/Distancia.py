from ShareKernel.InputData import InputData

class Distancia:
    def __init__(self):
        super().__init__()
        self._inputData = InputData()
    
    def Ejecutar(self):
        vIncial = self._inputData.ObtenerValorNumerico("Ingrese la velocidad inicial: ")
        tiempo = self._inputData.ObtenerValorNumerico("Ingrese el tiempo que se tardo: ")
        aceleracion = self._inputData.ObtenerValorNumerico("Ingrese la aceleracion del objeto: ")

        distancia = (vIncial*tiempo) + 0.5*(aceleracion*(tiempo**2))
        print(f"La distancia es: {distancia}")
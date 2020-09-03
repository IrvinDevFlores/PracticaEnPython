from ShareKernel.InputData import InputData

class AlturaObjeto:
    def __init__(self):
        super().__init__()
        self._inputData = InputData()

    def Ejecutar(self):
        vInicial = self._inputData.ObtenerValorNumerico("Ingrese la velocidad inicial: ")
        tiempo = self._inputData.ObtenerValorNumerico("Ingrese el tiempo que se tardo: ")

        distancia = vInicial*tiempo - (0.5*(-9.8))*tiempo**2
        print(f"La altura del objeto {distancia}")
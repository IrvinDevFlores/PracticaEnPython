from ShareKernel.InputData import InputData

class VelocidadFinal:
    def __init__(self):
        super().__init__()
        self._inputData = InputData()


    def Ejecutar(self):
        vInicial = self._inputData.ObtenerValorNumerico("Ingrese la velocidad inicial: ")
        aceleracion = self._inputData.ObtenerValorNumerico("Ingrese aceleracion: ")
        tiempo = self._inputData.ObtenerValorNumerico("Ingrese el tiempo que se tardo: ")

        vFinal = vInicial + (aceleracion*tiempo)
        print(f"La velocidad final {vFinal}")
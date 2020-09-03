from ShareKernel.InputData import InputData

class AceleracionMedia:
    def __init__(self):
        super().__init__()
        self._inputData = InputData()
    
    def Ejecutar(self):
        vFinal = self._inputData.ObtenerValorNumerico("Ingresar velocidad final: ")
        vIncial = self._inputData.ObtenerValorNumerico("Ingresar velocidad inicial: ")

        tFinal = self._inputData.ObtenerValorNumerico("Ingresar el tiempo final: ")
        tIncial = self._inputData.ObtenerValorNumerico("Ingresar el tiempo inicial: ")

        aceleracion = (vFinal - vIncial)/(tFinal - tIncial)

        print(f"La aceleracion media es {aceleracion}")
        
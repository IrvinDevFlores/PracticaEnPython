from ShareKernel.InputData import InputData

class VelocidadFinalCaidaLibre:
    def __init__(self):
        super().__init__()
        self._inputData = InputData()

    def Ejecutar(self):
        
        tiempo = self._inputData.ObtenerValorNumerico("Ingrese el tiempo que se tardo: ")

        distancia = (9.8)*tiempo
        print(f"La altura del objeto {distancia}")
from ShareKernel.InputData import InputData

class VolumenCubo:
    def __init__(self):
        super().__init__()
        self._inputData = InputData()

    def Ejecutar(self):
        lado = self._inputData.ObtenerValorNumerico("Ingrese el valor del lado del cubo: ")
        volumen = float((lado**3))

        print(f"El volumen del cubo es {volumen}")
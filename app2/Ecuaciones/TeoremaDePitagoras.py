from ShareKernel.Ecuacion import Ecuacion
from ShareKernel.InputData import InputData
from math import sqrt

class TeoremaDePitagoras(Ecuacion):

    """ 
    pitagoras = TeoremaDePitagoras()


    print("\nDejar en blanco el valor desconocido")

    pitagoras.PedirLados()
    """
    

    def __init__(self):
        #sirve para asignar las variables de la superclase

        self._inputData = InputData()

    def Ejecutar(self):
        self.DefinirTriangulo()
        self.PedirLados()

    def DefinirTriangulo(self, a = None, b = None, c = None):
        return r"""
    |\
    | \
    |  \ h
  a |   \
    |    \
    |_ _ _\
      b
    
    a = %s
    b = %s
    h = %s""" % ("?" if a is None else a,
                 "?" if b is None else b,
                 "?" if c is None else c)
    
    def PedirLados(self):
        a = self._inputData.ObtenerValorNumerico("a: ")
        b = self._inputData.ObtenerValorNumerico("b: ")
        

        if a is None or b is None:
            c = self._inputData.ObtenerValorNumerico("c: ")
        else:
            c = None
        
        isMenorQueDos = (bool(a) + bool(b) + bool(c)) < 2


        
        if c is None:
            data = float((a*a) + (b*b))
            c = sqrt(data)
        elif a is None:
            data = float((c*c) - (b*b))
            a = sqrt(data)
        elif b is None:
            data = float((c*c) - (a*a))
            b = sqrt(data)    
        print("")

        print(self.DefinirTriangulo(a, b, c))

        

    def Calcular(self):
        pass

        
   

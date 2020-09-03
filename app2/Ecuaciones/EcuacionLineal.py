
class EcuacionLineal:
    def __init__(self):
        super().__init__()


    def Ejecutar(self):
        expresion = input("Ingrese la expresion lineal: ")
        solucion = self.solve_linear(expresion)
        print(solucion)
        
    
    
    def solve_linear(self, ecuacion,var='x'):
        expression = ecuacion.replace("=","-(")+")"
        grouped = eval(expression.replace(var,'1j'))

        return -grouped.real/grouped.imag


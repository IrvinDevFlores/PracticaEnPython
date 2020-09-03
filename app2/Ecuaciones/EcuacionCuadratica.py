import math
class EcuacionCuadratica:
    def __init__(self):
        super().__init__()
        

    def Ejecutar(self):
        print("ax2 + bx + c = 0")
        a = int(input("Introduce el valor de a: "))
        b = int(input("Introduce el valor de b: "))
        c = int(input("Introduce el valor de c: "))

        d = b**2-4*a*c # discriminant

        if d < 0:
            print ("No tiene soluciones reales esta ecuacion")
        elif d == 0:
            x = (-b+math.sqrt(b**2-4*a*c))/2*a
            print ("Esta ecuacion tiene una solucion: "), x
        else:
            x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
            x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
            print ("Esta ecuacion tiene dos soluciones: ", x1, 
                        " ó ", x2)
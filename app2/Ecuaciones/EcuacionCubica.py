from random import randint
import sympy as sp
# pip install sympy

class EcuacionCubica:


    def __init__(self):
        super().__init__()

    def Ejecutar(self):
        # Ecuacion: x3 - 4x2 - 3x - 10 = 0
        #video julio profe: https://www.youtube.com/watch?v=DnmyzvSQGVA
        #comprobador de ecuaciones: https://es.calcuworld.com/calculadoras-matematicas/ecuaciones-tercer-grado/

        coeficientePrincipal = int(input("Ingrese del coeficiente principal: "))
        
        a = int(input("Ingrese el valor de a: "))
        b = int(input("Ingrese el valor de b: "))
        c = int(input("Ingrese el valor de c: "))
        if(coeficientePrincipal != 1):
            a = a / coeficientePrincipal
            b = b / coeficientePrincipal
            c = c / coeficientePrincipal
            coeficientePrincipal = 1
        
        
        variable = sp.Symbol ('x') 
        funcion = ((variable ** 3) + (a * variable ** 2) + (b * variable) + c) 
        variable = sp.solve (funcion) 
        

        sol1 = variable[0]
        sol2 = variable[1]
        sol3 = variable[2]
        print(f"Solucion 1: {sol1}")
        print(f"Solucion 2: {sol2}")
        print(f"Solucion 3: {sol3}") # solve function returns the result is a list of

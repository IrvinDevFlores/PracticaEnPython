from ShareKernel.Switch import Switch


import turtle


def arbol(longitudRama,t):
    if longitudRama > 5:
        t.forward(longitudRama)
        t.right(20)
        arbol(longitudRama-15,t)
        t.left(40)
        arbol(longitudRama-15,t)
        t.right(20)
        t.backward(longitudRama)

def main():
    t = turtle.Turtle()
    miVentana = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    arbol(75,t)
    miVentana.exitonclick()


class MessagePresenter:
    
    def __init__(self):
        self.switch = Switch()

    def MostrarMensaje(self):
                print(r""" 
            1. Ecuaciones
                1.1 Teorema de pitagoras
                1.2 Ecuacion Lineal
                1.3 Cuadratica
                1.4 Cubica

            2. Volumenes y Areas
                2.1 Esfera
                2.2 Cubo
                2.3 Cono

            3. Ecuaciones Cinematicas
                3.1 Velocidad Final (No hay distancia)
                3.2 Distancia (No hay Velocidad Final)
                3.3 Aceleracion media

            4. Ecuaciones Cinematicas Caida libre
                4.1 Altura objeto 
                4.2 Velocidad final
                4.3 Tiempo (Sin velocidad Final)
            
            5. Para sorprender
                5.1 Sorpresa
            
            6. Salir
            """)
    
    def MostrarMenu(self):
        
        
        i = None
        while(True):
                self.MostrarMensaje()

                i = input("Elige tu opcion: ")

                if i == "5.1":
                    main()
                elif i == "6":
                    break

                self.switch.GetOption(i).Ejecutar()
                print("")
                delay = input("presione cualquier tecla para continuar...")


       

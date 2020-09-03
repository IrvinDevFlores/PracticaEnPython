
import os


from Services.UsuarioService import UsuarioService
import Sopresa.ArbolRecursivo as ArbolRecursivo
import Biciesto.AñoBiciesto as Biciesto



class MessagePresenter:
    
    def __init__(self):
        super().__init__()
        self.userService = UsuarioService()





    def IrvinUsuarios(self):
   
         self.userService.CrearUsuarios()

    def IrvinSorpresa(self):
         ArbolRecursivo.main()

    def IrvinEjercicio3(self):
        
        Biciesto.IrvinEjercicio3()
    
    def LimpiarPantalla(self):
        delay = input("presione cualquier tecla para continuar...")
        os.system('cls||clear')

    def MostrarMensaje(self):
            print(r""" 
            1. Crear usuario y contraseña
                
            2. Año biciesto

            3. Sorpresa

            4. Salir
            """)
    
    def MostrarMenu(self):
        
        
        i = None
        while(True):
            self.MostrarMensaje()

            i = input("Elige tu opcion: ")

            if i == "1":
                self.IrvinUsuarios()
                self.LimpiarPantalla()
                continue
            elif i == "2":

                noExiste = self.userService.ValidarCredenciales() == False
                if(noExiste):
                   print("Credenciales incorrectas")
                   continue
                
                print("===> Login correcto")
                self.IrvinEjercicio3()
                self.LimpiarPantalla()
         
                continue
            elif i == "3":
                self.IrvinSorpresa()
                self.LimpiarPantalla()
                continue
            elif i == "4":
                print(self.userService.GetUsers())
                self.LimpiarPantalla()
                break
            print("")
            

       

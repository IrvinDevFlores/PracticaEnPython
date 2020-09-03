
from dataclasses import dataclass

from Models.Usuario import Usuario
import SharedModules.InputData as InputData

import getpass



@dataclass
class UsuarioService:
   
   

    def __init__(self):
        super().__init__()
        self.usuarios = []
        

    def GetUsers(self):
        return self.usuarios
    
    def ValidarCredenciales(self):
        user = InputData.PedirDato("Ingrese su usuario: ")
        #pswd = getpass.getpass('Password:')
        password = getpass.getpass('Password: ')

        elUsuarioExiste = False
        for u in self.GetUsers():
            if u.nombreUsuario == user and u.password == password:
                elUsuarioExiste = True
                
                break
            else:
                elUsuarioExiste = False
        
        return elUsuarioExiste


    def CrearUsuarios(self):
       
        
         
        while(True):
        
            nombreUsuario = InputData.PedirDato("Ingrese su nuevo nombre de usuario: ")

            seEncontroUsuario = False
            for u in self.usuarios:
                seEncontroUsuario = u.nombreUsuario == nombreUsuario
            
            
            if(seEncontroUsuario):
                print("El usuario ya existe")
                continue

            password = InputData.PedirDato("Ingrese su password: ")
            
            validacionPassword = InputData.PedirDato("Ingrese de nuevo su password: ")

            if(password != validacionPassword):
                print("Las contraseñas no coinciden")
                continue

            usuario = Usuario(nombreUsuario, password)

            self.usuarios.append(usuario)
            
            print("Usuario creado correctamente!!!")

            break

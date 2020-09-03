
def PedirDato(mensaje):
    entrada = ""
    while(True):
        entrada = input(mensaje)
        esElUsuarioValido = entrada == None or entrada == ""
        if(esElUsuarioValido):
            print("No se permiten cadenas vacias")
            continue
        
        break

    return entrada

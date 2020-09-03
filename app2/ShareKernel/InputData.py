class InputData:
    
    def __init__(self):
        super().__init__()

    def ObtenerValorNumerico(self, prompt):
            
          while True:
            value = input(prompt)
            if not value:
                return None
            try:
                value = int(value)
                return value
            except ValueError:
                print("Ingrese un valor numerico. "
                    "Porfa no sea como JOH.")
            else:
                break

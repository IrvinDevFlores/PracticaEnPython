

from dataclasses import dataclass

@dataclass
class Usuario:
    nombreUsuario: str
    password: str
    """
    def __init__(self, user = None, passwd = None):
        super().__init__()
        self.nombreUsuario = user
        self.password = passwd
    """
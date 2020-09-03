from Ecuaciones.EcuacionLineal import EcuacionLineal
from Ecuaciones.TeoremaDePitagoras import TeoremaDePitagoras
from Ecuaciones.EcuacionCuadratica import EcuacionCuadratica
from Ecuaciones.EcuacionCubica import EcuacionCubica
from Ecuaciones.Sorpresa import Sorpresa

from AreasYVolumentes.VolumenEsfera import VolumenEsfera
from AreasYVolumentes.VolumenCubo import VolumenCubo
from AreasYVolumentes.VolumenCono import VolumenCono

from Cinematica.MRU.VelocidadFinal import VelocidadFinal
from Cinematica.MRU.Distancia import Distancia
from Cinematica.MRU.AceleracionMedia import AceleracionMedia

from Cinematica.CaidaLibre.AlturaObjeto import AlturaObjeto
from Cinematica.CaidaLibre.VelocidadFinalCaidaLibre import VelocidadFinalCaidaLibre
from Cinematica.CaidaLibre.TiempoCaida import TiempoCaida

class Switch:
    def __init__(self):
        super().__init__()

        self.switcher = {
            "1.1" : TeoremaDePitagoras(),
            "1.2" : EcuacionLineal(),
            "1.3" : EcuacionCuadratica(),
            "1.4" : EcuacionCubica(),
            "2.1" : VolumenEsfera(),
            "2.2" : VolumenCubo(),
            "2.3" : VolumenCono(), 
            "3.1" : VelocidadFinal(),
            "3.2" : Distancia(),
            "3.3" : AceleracionMedia(),
            "4.1" : AlturaObjeto(),
            "4.2" : VelocidadFinalCaidaLibre(),
            "4.3" : TiempoCaida()
        }

    def GetOption(self,i):
        return self.switcher.get(i,lambda x : print('No existe esa opcion'))
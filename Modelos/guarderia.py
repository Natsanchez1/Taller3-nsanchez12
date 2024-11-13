from boaconstrictor import BoaConstrictor
from huron import Huron

class Guarderia():
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.boas = []
        self.hurones = []

    def alimentar_boa(self, boa, raton):
        try:
            if boa is None:
                raise ValueError ("Esta Boa no existe")
            resultado=boa.agregar_raton(raton)
            return "Exito"
        except ValueError as e:
            return str(e)  # Retorna el mensaje de error si boa es None o no pertenece
        except Exception as e:
            return "La boa esta llena"


boa1=BoaConstrictor("Boa1",2,3.5,"Mexico",450.9,3)
boa2=BoaConstrictor("Boa2",2,3.5,"Australia",450.9,3)
huron1=Huron("Pepe",3,7.9,"Australia",9000)
huron2=Huron("Juan",3,9.0,"Colombia",700.5)





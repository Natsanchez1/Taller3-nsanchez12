from animalexotico import AnimalExotico

class Huron(AnimalExotico):

    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float) -> None:
        #Hereda todos los atributos de animal exotico
        super().__init__(nombre, edad, peso, pais_origen, impuestos)

    def hacer_sonido(self) -> str:
        return "¡Eek Eek!"
    
huron1=Huron("Pepe",3,7.9,"Australia",9000)

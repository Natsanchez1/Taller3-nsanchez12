from animal import Animal
from ianimal import IAnimal

class AnimalExotico(Animal):
    
    def __init__(self, nombre: str, edad: int, peso: float,pais_origen: str, impuestos:float) -> None:
        #atributos heredados
        super().__init__(nombre, edad, peso)
        #atributos propios de la clase
        self.pais_origen = pais_origen
        self.impuestos= impuestos

    def hacer_sonido(self) -> str:
        return super().hacer_sonido()

    #metodo
    def calcular_flete(self)-> float:
        return self.peso*self.impuestos
    
    @property
    def pais_origen(self) -> str:
        """ Devuelve el valor del atributo privado 'pais_origem' """
        return self.__pais_origem
    
    @pais_origen.setter
    def pais_origen(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'pais_origem'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__pais_origen = value
        else:
            raise ValueError('Expected str')
    
    @property
    def impuestos(self) -> float:
        """ Devuelve el valor del atributo privado 'impuestos' """
        return self.__impuestos
    
    @impuestos.setter
    def impuestos(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'impuestos'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self.__impuestos = value
        else:
            raise ValueError('Expected float')
    
animal1=AnimalExotico("Pedro",2,45.0,"Canada",450.0)
print(animal1.calcular_flete())

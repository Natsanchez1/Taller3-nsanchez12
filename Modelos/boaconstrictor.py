from animalexotico import AnimalExotico

class BoaConstrictor(AnimalExotico):
    
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float,ratones:int) -> None:
        #atributos heredados
        super().__init__(nombre, edad, peso, pais_origen, impuestos)
        #atributo propio
        self.ratones = ratones

    def hacer_sonido(self) -> str:
        return "¡Tsss!"

    @property
    def ratones(self) -> int:
        """ Devuelve el valor del atributo privado 'ratones'"""
        return self.__ratones
    
    @ratones.setter
    def ratones(self, ratones:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'ratones_comidos'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(ratones, int):
            self.__ratones = ratones
        else:
            raise ValueError('Expected int')
        
    #Definimos la función para agregar el raton
        def agregar_raton(self,raton:int)-> int:
            if raton == 20:
                self.ratones = 20
                print("Muchos ratones")
            else:
                self.ratones += raton

boa1=BoaConstrictor("Boa1",2,3.5,"Mexico",450.9,3)
print(boa1.ratones)
boa1.agregar_raton(9)
print(boa1.__dict__)
print(boa1.agregar_raton(10))


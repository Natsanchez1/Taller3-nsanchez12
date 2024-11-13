import unittest
from Modelos.boaconstrictor import BoaConstrictor
from Modelos.animalexotico import AnimalExotico

class TestHuron(unittest,TestCase):
    def test_hacer_sonido(self):
        boa1=BoaConstrictor("Boa1",2,3.5,"Mexico",456,3)
        self.assertEqual(boa1.hacer_sonido(),"¡Tsss!")

    def test_calcular_flete(self):
        boa1=BoaConstrictor("Boa1",2,3.5,"Mexico",456,3)
        self.assertEqual(boa1.calcular_flete(), self.peso*self.impuestos)

    def test_agregar_raton(self):
        boa1=BoaConstrictor("Boa1",2,3.5,"Mexico",456,3)
        boa1.agregar_raton(4)
        self.assertEqual(boa1.ratones,7)

        
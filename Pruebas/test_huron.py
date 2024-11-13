import unittest
from Modelos.huron import Huron
from Modelos.animalexotico import AnimalExotico

class TestHuron(unittest,TestCase):
    def test_hacer_sonido(self):
        huron = Huron("Pepe",3,7.9,"Australia",9000)
        self.aseertEqual(huron.hacer_sonido(),"¡Eek Eek!")

    def test_calcular_flete(self):
        huron = Huron("Pepe",3,7.9,"Australia",9000)
        self.aseertEqual(huron.calcular_flete(), self.peso*self.impuestos)
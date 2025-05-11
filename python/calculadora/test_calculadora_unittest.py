import unittest
import math
from calculadora import (
    adicionar,
    subtrair,
    multiplicar,
    dividir,
    potencia,
    raiz_quadrada,
    porcentagem
)

class TestCalculadora(unittest.TestCase):

    def test_adicionar(self):
        self.assertEqual(adicionar(2, 3), 5)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 7), 21)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(5, 0)

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_raiz_quadrada(self):
        self.assertAlmostEqual(raiz_quadrada(25), 5)

    def test_raiz_quadrada_negativa(self):
        with self.assertRaises(ValueError):
            raiz_quadrada(-9)

    def test_porcentagem(self):
        self.assertEqual(porcentagem(10, 200), 20)

if __name__ == "__main__":
    unittest.main()

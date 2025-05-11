import unittest
from calculadora.core import *

class TestCalculadora(unittest.TestCase):
    def test_adicao(self): self.assertEqual(adicionar(2, 3), 5)
    def test_subtracao(self): self.assertEqual(subtrair(5, 2), 3)
    def test_multiplicacao(self): self.assertEqual(multiplicar(4, 3), 12)
    def test_divisao(self): self.assertEqual(dividir(10, 2), 5)
    def test_divisao_por_zero(self): 
        with self.assertRaises(ValueError): dividir(4, 0)
    def test_potencia(self): self.assertEqual(potencia(2, 4), 16)
    def test_raiz_quadrada(self): self.assertEqual(raiz_quadrada(9), 3)
    def test_raiz_negativa(self):
        with self.assertRaises(ValueError): raiz_quadrada(-1)
    def test_porcentagem(self): self.assertEqual(porcentagem(10, 200), 20)

if __name__ == '__main__':
    unittest.main()

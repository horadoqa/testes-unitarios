# pip install pytest

import pytest
from calculadora import (
    adicionar, subtrair, multiplicar, dividir,
    potencia, raiz_quadrada, porcentagem
)

def test_adicionar():
    assert adicionar(2, 3) == 5

def test_subtrair():
    assert subtrair(10, 4) == 6

def test_multiplicar():
    assert multiplicar(3, 7) == 21

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ValueError, match="Divisão por zero"):
        dividir(5, 0)

def test_potencia():
    assert potencia(2, 3) == 8

def test_raiz_quadrada():
    assert raiz_quadrada(25) == 5

def test_raiz_quadrada_negativa():
    with pytest.raises(ValueError, match="raiz quadrada.*negativo"):
        raiz_quadrada(-9)

def test_porcentagem():
    assert porcentagem(10, 200) == 20


# pytest test_calculadora_pytest.py

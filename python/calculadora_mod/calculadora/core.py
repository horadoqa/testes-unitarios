import math

def adicionar(a: float, b: float) -> float:
    return a + b

def subtrair(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def potencia(a: float, b: float) -> float:
    return a ** b

def raiz_quadrada(a: float) -> float:
    if a < 0:
        raise ValueError("Raiz quadrada de número negativo não é permitida.")
    return math.sqrt(a)

def porcentagem(a: float, b: float) -> float:
    return (a / 100) * b

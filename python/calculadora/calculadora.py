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
        raise ValueError("Não é possível calcular a raiz quadrada de número negativo.")
    return math.sqrt(a)

def porcentagem(a: float, b: float) -> float:
    return (a / 100) * b

def obter_numero(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def exibir_menu() -> None:
    print("\n=== CALCULADORA MODERNA ===")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência (a^b)")
    print("6. Raiz Quadrada")
    print("7. Porcentagem (a% de b)")
    print("8. Sair")

def main() -> None:
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-8): ")

        match escolha:
            case '1':
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                print(f"Resultado: {adicionar(a, b)}")
            case '2':
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                print(f"Resultado: {subtrair(a, b)}")
            case '3':
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                print(f"Resultado: {multiplicar(a, b)}")
            case '4':
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                try:
                    print(f"Resultado: {dividir(a, b)}")
                except ValueError as e:
                    print(f"Erro: {e}")
            case '5':
                a = obter_numero("Digite a base: ")
                b = obter_numero("Digite o expoente: ")
                print(f"Resultado: {potencia(a, b)}")
            case '6':
                a = obter_numero("Digite o número: ")
                try:
                    print(f"Resultado: {raiz_quadrada(a)}")
                except ValueError as e:
                    print(f"Erro: {e}")
            case '7':
                a = obter_numero("Digite a porcentagem (ex: 25 para 25%): ")
                b = obter_numero("Digite o número base: ")
                print(f"Resultado: {porcentagem(a, b)}")
            case '8':
                print("Encerrando a calculadora. Até mais!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

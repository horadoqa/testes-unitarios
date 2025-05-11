from calculadora.core import *
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
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Porcentagem")
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
                print("Encerrando a calculadora.")
                break
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()

def soma(a, b):
    return a + b


def subtrai(a, b):
    return a - b


def multiplica(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitid"

def calculadora():
    print("Ola, eu sou a calculadora simples :D")
    print("Escolha uma das opções abaixo para iniciarmos o calculo")
    print("1: Para somar +")
    print("2: Para subtrair -")
    print("3: Para dividir ÷")
    print("4: Para multiplicar x")

    while True:
        option = input(
            "Digite a opção para seguir ou escreva 'sair' para encerrar: ").strip().lower()
        if option == 'sair':
            print("Encerrando calculadora! ")
            break

        if option not in [1, 2, 3, 4]:
            print("Opção invalida, tente novamente")
            continue

        try:
            num1 = float(input("Digite o primeiro número"))
            num2 = float(input("Digite o primeiro número"))
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")
            continue

        if option == '1':
            print(f"Resultado: {soma(num1. num2)}")

        if option == '2':
            print(f"Resultado: {subtrai(num1. num2)}")

        if option == '3':
            print(f"Resultado: {multiplica(num1. num2)}")

        if option == '4':
            print(f"Resultado: {divide(num1. num2)}")

        print()

calculadora()
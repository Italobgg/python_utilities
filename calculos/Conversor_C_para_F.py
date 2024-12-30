def celsius_para_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def conversor_temperaturas():
    while True:
        print("\nEscolha uma conversão:")
        print("1 - Celsius para Fahrenheit")
        print("2 - Fahrenheit para Celsius")
        print("3 - Sair")

        opcao = input("Digite o número da opção desejada: ").strip()

        if opcao == "1":
            try:
                celsius = float(input("Digite a temperatura em Celsius: "))
                fahrenheit = celsius_para_fahrenheit(celsius)
                print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "2":
            try:
                fahrenheit = float(
                    input("Digite a temperatura em Fahrenheit: "))
                celsius = fahrenheit_para_celsius(fahrenheit)
                print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "3":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


conversor_temperaturas()

def impar_par():
    while True:
        try:
            num1 = int(input("Escolha o primeiro número: "))
            num2 = int(input("Escolha o segundo número: "))
            soma = num1 + num2
            if soma % 2 == 0:
                print(f"A soma de {num1} + {num2} é {soma}, que é PAR!")
            else:
                print(f"A soma de {num1} + {num2} é {soma}, que é ÍMPAR!")
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        repetir = input("Deseja tentar novamente? (s/n): ").strip().lower()
        if repetir != 's':
            print("Obrigado por usar o programa! Até mais!")
            break


impar_par()

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2  # Divisão inteira para obter um índice válido
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1  # Ajusta limite superior
        else:
            baixo = meio + 1  # Ajusta limite inferior
    return None  # Retorna None se não encontrar o item


minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))  # => 1
print(pesquisa_binaria(minha_lista, -1))  # => None

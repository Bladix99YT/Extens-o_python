import os
lista = []
opcao = 0

while True:
    print("Selecione uma das opções abaixo: ")
    opcao = input("[i]nserir [a]pagar [l]istar: ")

    if opcao == 'i':
        os.system('cls')
        item = input("Digite um item a ser adicionado: ")
        lista.append(item)

    elif opcao == 'a':
        os.system('cls')
        for item in enumerate(lista):
            print(item)

        indice = input("Digite o numero do item a ser apagado: ")
        indice = int(indice)
        del lista[indice]

        if not lista:
            print("Lista vazia não posso apagar!")

    elif opcao == 'l':
        os.system('cls')
        for item in enumerate(lista):
            print(item)

        if not lista:
            print("Lista vazia")

    # Esta parte é o tratamento de exceções não vou fazer por enquanto !!!
    # try:
    #     indice = int(indice)
    #     del lista[indice]

    # except ValueError:
    #     print("Por favor digite apenas numeros inteiros")

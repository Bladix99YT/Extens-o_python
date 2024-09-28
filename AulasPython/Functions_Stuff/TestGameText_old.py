import os
import sys

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2 ?',
        'Opcoes': [1, 2, 3, 4],
        'Resposta': '4',
    },

    {
        'Pergunta': 'Quanto é 5x5 ?',
        'Opcoes': [10, 25, 30, 50],
        'Resposta': '25',
    },

    {
        'Pergunta': 'Quanto é 10/2 ?',
        'Opcoes': [5, 2, 4, 6],
        'Resposta': '5',
    },
]


def responder_pergunta(pergunta):
    print('Pergunta:', pergunta['Pergunta'])

    opcoes = pergunta['Opcoes']
    for i, opcao in enumerate(opcoes):
        print(f'Opção {i}: {opcao}')

    while True:
        escolha = input('Escolha uma das opções de 0 a 3: ')

        if escolha.isdigit():
            escolha = int(escolha)
            if escolha >= 0 and escolha < len(opcoes):
                break
            else:
                print("Escolha inválida. Digite um número válido.")
                sys.exit()
        else:
            print("DIGITE APENAS NÚMEROS INTEIROS!!!")
            sys.exit()

    return escolha


qtd_acertos = 0


for pergunta in perguntas:

    escolha = responder_pergunta(pergunta)

    acertou = pergunta['Opcoes'][escolha] == pergunta['Resposta']

    # Lógica para verificar se a escolha está correta ou incorreta
    if escolha == pergunta['Resposta']:
        acertou = True

    if acertou:
        qtd_acertos += 1
        print('Acertou 👍\n')
    else:
        print('Errou ❌')


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')

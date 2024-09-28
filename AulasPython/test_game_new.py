perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },

    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },

    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0

def responder_pergunta(pergunta):
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opcoes']
    for i, opcao in enumerate(opcoes):
        print(f'{i + 1})', opcao)
    print()

    while True:
        escolha = input('Escolha uma opção (digite o número): ')

        if escolha.isdigit():
            escolha_int = int(escolha) - 1  # Convertendo para índice (começando de 0)
            if 0 <= escolha_int < len(opcoes):
                break
            else:
                print("Escolha inválida. Digite um número correspondente a uma opção.")
        else:
            print("Digite apenas números inteiros.")

    return escolha_int

for pergunta in perguntas:
    escolha = responder_pergunta(pergunta)

    acertou = pergunta['Opcoes'][escolha] == pergunta['Resposta']

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()

print('Você acertou', qtd_acertos, 'de', len(perguntas), 'perguntas.')

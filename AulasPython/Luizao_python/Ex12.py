######################### EXERCÍCIO 12 ###############################

# Escreva um programa que leia o número de alunos e o de alunas de uma sala. Como saída, o programa
# deve apresentar primeiro quem estiver em maior quantidade. Por exemplo, se na sala tiver mais alunos,
# apresente primeiro o número de alunos, caso contrário apresente o número de alunas e depois o de
# alunos.

######################### EXERCÍCIO 12 ###############################

# Inicializa listas para alunos e alunas
alunos = []
alunas = []

# Solicita a quantidade total de estudantes (alunos e alunas)
total_estudantes = int(input('Digite o número total de estudantes: '))

# Loop para coletar os nomes e tipos (aluno ou aluna)
for i in range(total_estudantes):
    nome = input('Digite o nome do estudante: ')
    tipo = input('Digite "aluno" se for homem ou "aluna" se for mulher: ').strip().lower()

    # Armazena o nome na lista correspondente
    if tipo == 'aluno':
        alunos.append(nome)
    elif tipo == 'aluna':
        alunas.append(nome)
    else:
        print('Tipo inválido, tente novamente.')

# Verifica quem tem maior quantidade e exibe o resultado
num_alunos = len(alunos)
num_alunas = len(alunas)

if num_alunos > num_alunas:
    print(f'\nQuantidade de estudantes: {total_estudantes}')
    print(f'A maior quantidade de estudantes são "alunos" com: {num_alunos} alunos.')
    print(f'Número de alunos: {num_alunos}')
    print(f'Número de alunas: {num_alunas}')
    
elif num_alunas > num_alunos:
    print(f'\nQuantidade de estudantes: {total_estudantes}')
    print(f'A maior quantidade de estudantes são "alunas" com: {num_alunas} alunas.')
    print(f'Número de alunas: {num_alunas}')
    print(f'Número de alunos: {num_alunos}')
else:
    print(f'O número de alunos e alunas é igual: {num_alunos}')


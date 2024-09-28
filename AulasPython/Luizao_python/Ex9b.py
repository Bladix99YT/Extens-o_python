######################### EXERCÍCIO 09b###############################

# Desenvolva um programa em Python que leia uma lista de 5 nomes fornecidos pelo usuário e conte
# quantos desses nomes contêm a letra 'a' (maiúscula ou minúscula). O programa deve usar a instrução
# while para percorrer a lista e realizar a contagem.

######################### EXERCÍCIO 09b###############################

lista_nomes = []

for i in range(5):
    nomes = input(f'Digite o nome {i+1}: ')
    lista_nomes.append(nomes)

indice = 0
contador = 0

# Conta quantos nomes contêm a letra 'a' (ou 'A')
while indice < len(lista_nomes):
    nomes = lista_nomes[indice]
    if 'a' in nomes.lower(): # Verifica se a letra 'a' está no nome, ignorando maiúsculas e minúsculas
        contador += 1
    indice += 1

print (f'O numero de nomes que contem a letra a são: {contador}')

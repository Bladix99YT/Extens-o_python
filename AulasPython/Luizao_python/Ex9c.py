######################### EXERCÍCIO 09c###############################

# Desenvolva um programa em Python que leia números inteiros fornecidos pelo usuário e calcule a soma
# de todos os números positivos inseridos. O programa deve usar a instrução while para continuar lendo
# números até que o usuário insira um número negativo. O programa deve, então, imprimir a soma dos
# números positivos.

######################### EXERCÍCIO 09c###############################

soma = 0

while True:
    numero = int(input('Digite um numero inteiro: '))

    if numero < 0:
        break

    soma += numero

print(f'A soma dos numeros inteiros positivos é de: {soma}') 
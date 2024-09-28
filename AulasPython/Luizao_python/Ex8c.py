######################### EXERCÍCIO 08c###############################

# Desenvolva um programa em Python que leia uma lista de 10 números inteiros fornecidos pelo usuário e
# calcule a soma de todos os números pares presentes na lista. O programa deve usar a instrução for para
# percorrer a lista e realizar o cálculo.

######################### EXERCÍCIO 08c###############################

numeros = []

for i in range(10):
    entrada = int(input(f'Digite o numero {i+1}: '))
    numeros.append(entrada)

somar_pares = 0
for numero in numeros:
    if(numero % 2 == 0):
        somar_pares += numero

print(f'A soma de todos os numeros pares da lista é: {somar_pares}')
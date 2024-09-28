######################### EXERCÍCIO 08b###############################

# Crie um programa que leia 5 números (utilizando arrays) e mostre o dobro, o triplo e a raiz quadrada de
# cada um. Utilize a instrução for para exibir os dados.

######################### EXERCÍCIO 08b###############################

import math


numeros = []

# Colocando dados dentro da array
for i in range(5):
    entrada = float(input(f'Digite o número {i+1}: '))
    numeros.append(entrada)

#Acessando a array e imprimindo os resultados (i + 1 aqui serve como um contador)
for i in range(5):
    dobro = numeros[i] * 2
    triplo = numeros[i] * 3
    raiz_quadrada = math.sqrt(numeros[i])
    print(f'Número {i+1}: {numeros[i]}')
    print(f'Dobro: {dobro}')
    print(f'Triplo: {triplo}')
    print(f'Raiz quadrada: {raiz_quadrada}')
    print()
######################### EXERCÍCIO 10 ###############################

# Faça um programa em Python que leia o preço de um produto. Se o valor do produto for inferior à R$
# 100,00, recalcule seu valor com 5% de desconto. Caso contrário, recalcule seu valor com 10% de
# desconto. Imprima seu novo preço, informando o valor de desconto.

######################### EXERCÍCIO 10 ###############################

while True:

    preco = float(input(f'Digite o preço a ser adicionado desconto: '))

    if preco < 100:
        desconto = preco * 0.05
        preco_novo = preco - desconto
    else:
        desconto = preco * 0.10
        preco_novo = preco - desconto


    print(f'\nPreço original: R$ {preco:.2f}')
    print(f'Desconto aplicado: R$ {desconto:.2f}')
    print(f'Novo preço: R$ {preco_novo:.2f}')


######################### EXERCÍCIO 11 ###############################

# Faça um programa em Python que leia o salário de um funcionário. Se o valor do salário for inferior a R$
# 1200,00, recalcule seu salário com aumento de 10%. Caso contrário, recalcule seu salário com aumento
# de 5%. Imprima o novo salário, informando o valor de aumento.

######################### EXERCÍCIO 11 ###############################

while True:
    salario = float(input('Digite o salário do funcionário: '))

    if salario < 1200:
        aumento = salario * 0.10
        # (valor_desconto = preco * desconto) essa variavel 'valor_desconto' poderia ser alguma instancia, 
        # fazendo que o valor desconto possa ser alterado por outro lugar como uma classe.
        salario_novo = salario + aumento
    else:
        aumento = salario * 0.5
        salario_novo = salario + aumento

    print(f'\nSalario original: R$ {salario:.2f}')
    print(f'Aumento aplicado: R$ {aumento:.2f}')
    print(f'Salario Recalculado: R$ {salario_novo:.2f}')
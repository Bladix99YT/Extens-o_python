######################### EXERCÍCIO 13 ###############################

# Desenvolva um programa para comparar a idade de Pedro e de Joana e informar quem é o mais velho.
# Dados de entrada: idade de Pedro e de Joana (tipos das variáveis: inteiro, e valor em anos).

######################### EXERCÍCIO 13 ###############################

idade_pedro = int(input('Insira a idade de pedro: '))
idade_joana = int(input('Insira a idade de Joana: '))


if idade_pedro > idade_joana:
    comparar_idades = idade_pedro - idade_joana
    print(f'Pedro é mais velho que joana com {comparar_idades} anos de diferença')
    
elif idade_joana > idade_pedro:
    comparar_idades = idade_joana - idade_pedro
    print(f'Joana é mais velha com {comparar_idades} anos de diferença')

else:
    print('Os dois tem a mesma idade!! ')
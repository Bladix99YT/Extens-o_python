###################### exercicio6 ######################################
numero = int(input('Digite um numero inteiro: '))

if numero % 5 == 0 and (numero % 3 == 0):
    print(f'O numero: {numero} é divisivel por 5 e 3 ao mesmo tempo')

else:
    print(f'O numero: {numero} não é divisivel por 5 e 3 ao mesmo tempo')
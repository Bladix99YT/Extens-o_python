###################### exercicio6b (versao prof) ######################################

numero = int(input('Digite um numero inteiro:'))

if(numero % 5 == 0) and (numero % 3 == 0):
    print(f'O numero {numero} é divisivel por 5 e por 3 ao mesmo tempo')

elif (numero % 5 == 0) and (numero % 3 != 0):
    print(f'O numero {numero} é divisivel por 5 mas nao por 3')

elif (numero % 5 != 0) and (numero % 3 == 0):
    print(f'O numero: {numero} é divisivel por 3 mas nao por 5 ')

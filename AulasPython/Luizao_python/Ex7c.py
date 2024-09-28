###################### exercicio7C ######################################

# Desenvolver um programa em Linguagem Python, que leia um número x, calcule e imprima o valor de y,
# de acordo com as condições abaixo:
# y = x , se x < 1;
# y = 0 , se x = 1;
# y = x2 , se x > 1;

###################### exercicio7C ######################################

x = float(input("Digite um numero: "))

if (x < 1):
    y = print(f'valor de y: {x}')
    
elif(x == 1):
    y = 0
    print(f'valor de y: {y}')

elif(x > 1):
   y = x * x
   print(f'Valor de y: {y}')
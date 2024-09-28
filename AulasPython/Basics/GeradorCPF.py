"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re
import sys

# cpf = '74682489070'
entrada = input("Digite o seu CPF: ")
cpf = re.sub(r'[^0-9]', '', entrada)
digitos_cpf = cpf[:9]
contador_1 = 10

entrada_repetida = entrada == entrada[0] * len(entrada)

resultado = 0

if entrada_repetida:
    print("Voce enviou uma entrada invalida!!")
    sys.exit()


for i in digitos_cpf:
    resultado += int(i) * contador_1
    contador_1 -= 1

digito_1 = resultado * 10 % 11

if digito_1 <= 9:

    digito_1 = digito_1

else:
    digito_1 = 0

digito_2 = digitos_cpf + str(digito_1)
# print(digito_2)

contador_2 = 11
resultado_2 = 0

for j in digito_2:
    resultado_2 += int(j) * contador_2
    contador_2 -= 1

digito_2 = resultado_2 * 10 % 11

# Outra forma de fazer ifs que sao mais simples
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_calculo = f'{digitos_cpf}{digito_1}{digito_2}'

if cpf == cpf_calculo:

    print("Cpf Válido")

else:
    print("Cpf Inválido")

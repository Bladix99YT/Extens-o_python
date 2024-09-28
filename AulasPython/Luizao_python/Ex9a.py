######################### EXERCÍCIO 09a###############################

# Elabore um programa em Python, que calcule e imprima a tabuada de qualquer número informado,
# utilizando a instrução while.

######################### EXERCÍCIO 09a###############################
numero = int(input("Digite um número inteiro para ver a tabuada: "))
i = 1

while i < 11:
    print(f"Tabuada do {numero}:")
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1

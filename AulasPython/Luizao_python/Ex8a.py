######################### EXERCÍCIO 08a###############################

# Elabore um programa em Python, que calcule e imprima a tabuada de qualquer número informado,
# utilizando a instrução for.

######################### EXERCÍCIO 08a###############################

# Solicita que o usuário informe o número
numero = int(input("Digite um número para ver a tabuada: "))

# Calcula e imprime a tabuada de 1 a 10
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

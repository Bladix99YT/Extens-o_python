# """
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.
# """
# numero = input("Digite um numero inteiro: ")

# # numero_int = int(numero) Jeito um pouco ruim de fazer o exercicio
# # pois ele converte de string para int
# # antes de poder fazer qualquer coisa e antes mesmo de saber se é inteiro

# if numero.isdigit():
#     numero_inteiro = int(numero)  # converter depois de checar se é inteiro
#     par_impar = numero_inteiro % 2 == 0  # varialvel bool pra verificar se é p/i
#     par_impar_str = 'impar'

#     if par_impar is True:  # O is true não é necessario pois ja tem uma variavel bool para retornar algo se for true ou false
#         par_impar_str = 'par'

#     print(f"O numero {numero_inteiro} é {par_impar_str}")

# else:
#     print("Voce nao digitou um numero inteiro!")

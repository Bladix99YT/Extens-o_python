###################### exercicio7b ######################################
# Desenvolva um programa em Python que leia a nota final de um aluno e determine sua situação acadêmica
# com base na seguinte tabela:
# - Nota >= 7: Aprovado
# - Nota >= 5 e < 7: Em Recuperação
# - Nota < 5: Reprovado


# Solicitar a nota
nota = float(input("Digite a nota do aluno: "))

if (nota >= 7):
    print("Aluno Aprovado!!!")

elif (nota >= 5 < 7):
    print("Aluno em recuperação!!!")

else:
    print("Aluno Reprovado")
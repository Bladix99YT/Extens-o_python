###################### exercicio7a ######################################

idade = int(input('Informe sua idade: '))

if (idade < 13):
    categoria = 'Criança'

elif (13 <= idade <= 19):
    categoria = 'Adolescente'

elif (20 <= idade <= 64):
    categoria = 'Adulto'

else:
    categoria = 'Idoso'

print(f'Sua faixa etária é {categoria}')
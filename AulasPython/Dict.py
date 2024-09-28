a, b = 1, 2
a, b = b, a


# Desempacotamento
# a, b = pessoa.values()
# (a1, a2), b = pessoa.items()

# print(a1, a2)
# print(b)


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# posso editar o dicionario e desempacotar
pessoa_completa = {**pessoa, **dados_pessoa, 'chave': 1}

print(pessoa_completa)

# for chave, valor in pessoa.items():
# print(chave, valor)


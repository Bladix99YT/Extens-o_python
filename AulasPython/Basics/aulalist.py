# nomes = ['maikon', 'mauricio']
# indices = range(len(nomes)
#                 )
# for indice in indices:
#     print(indice, nomes[indice], type(nomes[indice])) //mostrar o indice junto ao valor

# nome1, nome2 = ['maikon', 'mauricio', 'abc'] # isso da erro (muitos valores para poucas variaveis)
# A variavel _ junto com o * guarda os valores restantes resolvendo o problema que basicamente cria uma lista vazia para os valores
# nome1, *_ = ['maikon', 'mauricio', 'abc']
# print(nome1)

# Metodo enumerate

lista = ['maikon', 'pão', 'bolo']
"""
 lista_enumerada = enumerate(lista) #Desta forma assim que passar no for o enumerate esgota os valores e nao itera mais
 for item in lista_enumerada:
     print(item)
"""
for item in enumerate(lista):
    print(item)

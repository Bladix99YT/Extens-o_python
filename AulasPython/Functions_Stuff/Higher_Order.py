"""
Higher Order Functions
Funções de primeira classe
"""


# def saudacao(msg, nome):
#     return f'{msg}, {nome}!'


# def executa(funcao, *args):
#     return funcao(*args)


# print(executa(saudacao, 'Bom dia', 'Luiz'))
# print(executa(saudacao, 'Boa noite', 'Maria'))

"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))


# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicador(multi):
    def multiplicar(numero):
        return numero * multi
    return multiplicar


duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadriplicar = multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadriplicar(4))

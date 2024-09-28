# def multiplo_de(numero, multiplo):
#     resultado = numero % multiplo == 0
#     print(f'{numero} é múltiplo de {multiplo}?', end=' ')
#     print(resultado)


# multiplo_de(16, 8)
# multiplo_de(15, 3)
# multiplo_de(10, 2)

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero

    return total


# Imprimir o retorno da função na variavel multiplicado!!!
multiplicado = multiplica(1, 2, 3, 4, 5)

print(multiplicado)


def par_impar(numero):
    impar_par = numero % 2 == 0

    if impar_par:
        return f'{numero} é par'

    return f'{numero} é impar'


print(par_impar(2))
print(par_impar(5))
print(par_impar(4))

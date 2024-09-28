######################### EXERCÍCIO 15 ###############################

# Uma frutaria vende frutas com a seguinte tabela de preços:
# Até 5Kg: Morango: R$ 7,50 p/Kg / Maçã: R$ 3,50 p/Kg
# Acima de 5Kg: Morango: R$ 5,30 p/Kg / Maçã: R$ 2,80 p/Kg

# Se o cliente comprar menos de 5 kg de frutas e o valor total da compra ultrapassar R$ 19,00, receberá um
# desconto de 8% sobre o total. Escreva um programa em Python para ler a quantidade (em Kg) de
# morangos e a de maçãs (em Kg) e que informe o valor a ser pago pelo cliente.

######################### EXERCÍCIO 15 ###############################
# Inicializa listas para armazenar os produtos e variáveis para acumular o peso total e o preço por kg
morango = []
maca = []

preco_total = 0
kg_total_morango = 0  # Acumulador de peso para morangos
kg_total_maca = 0     # Acumulador de peso para maçãs
preco_morango_por_kg = 0
preco_maca_por_kg = 0

# Exemplo de laço para a inserção de produtos e seus pesos
while True:
    nome = input("Digite o nome da fruta ('morango' ou 'maça', ou 'sair' para finalizar o pedido): ").lower()

    if nome == 'sair':
        break
    
    peso = float(input(f"Digite o peso do {nome} (em Kg): "))

    if nome == 'morango' and peso <= 5:
        preco_morango_por_kg = 7.50
        preco_kilo = peso * preco_morango_por_kg
        morango.append(peso)
        preco_total += preco_kilo
        kg_total_morango += peso  # Acumula o peso dos morangos

    elif nome == 'morango' and peso > 5:
        preco_morango_por_kg = 5.30
        preco_kilo = peso * preco_morango_por_kg
        morango.append(peso)
        preco_total += preco_kilo
        kg_total_morango += peso  # Acumula o peso dos morangos

    elif nome == 'maça' and peso <= 5:
        preco_maca_por_kg = 3.50
        preco_kilo = peso * preco_maca_por_kg
        maca.append(peso)
        preco_total += preco_kilo
        kg_total_maca += peso  # Acumula o peso das maçãs

    elif nome == 'maça' and peso > 5:
        preco_maca_por_kg = 2.80
        preco_kilo = peso * preco_maca_por_kg
        maca.append(peso)
        preco_total += preco_kilo
        kg_total_maca += peso  # Acumula o peso das maçãs
    else:
        print('Produto inválido! Selecione apenas "morango" ou "maça".')

    if (kg_total_maca + kg_total_morango) < 5 and preco_total > 19:
        desconto = preco_total * 0.08
        preco_total = preco_total - desconto

# Exibe os produtos, o total de Kg, o preço por Kg e o preço total
print(f"\nTotal de morangos: {kg_total_morango:.2f} Kg")
if kg_total_morango > 0:
    print(f"Preço por Kg de morango: R$ {preco_morango_por_kg:.2f}")

print(f"Total de maçãs: {kg_total_maca:.2f} Kg")
if kg_total_maca > 0:
    print(f"Preço por Kg de maçã: R$ {preco_maca_por_kg:.2f}")

if desconto > 0:
    print(f"\nDesconto aplicado: R$ {desconto:.2f} (8%)")
    print(f"Preco total: R$ {preco_total:.2f}")

else:
    print(f"\nPreço total: R$ {preco_total:.2f}")

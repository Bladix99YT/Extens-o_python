######################### EXERCÍCIO 14 ###############################

# Desenvolva um programa para calcular e comparar a área de dois retângulos A e B. O programa deverá
# dizer qual retângulo possui a maior área ou se ambos possuem tamanhos iguais. Dados de entrada:
# tamanho da base e da altura (tipo das variáveis: inteiro, valor em centímetros).

######################### EXERCÍCIO 14 ###############################


# Solicita as dimensões do retângulo A
base_a = int(input("Digite o tamanho da base do retângulo A (em cm): "))
altura_a = int(input("Digite o tamanho da altura do retângulo A (em cm): "))

# Solicita as dimensões do retângulo B
base_b = int(input("Digite o tamanho da base do retângulo B (em cm): "))
altura_b = int(input("Digite o tamanho da altura do retângulo B (em cm): "))

# Calcula as áreas dos retângulos
area_a = base_a * altura_a
area_b = base_b * altura_b

# Compara as áreas
if area_a > area_b:
    print(f"O retângulo A tem maior área ({area_a} cm²) que o retângulo B ({area_b} cm²).")
elif area_b > area_a:
    print(f"O retângulo B tem maior área ({area_b} cm²) que o retângulo A ({area_a} cm²).")
else:
    print(f"Os retângulos A e B possuem áreas iguais ({area_a} cm²).")

palavra_secreta = 'maikon'
letra_digitada = 0
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input("Digite uma letra minuscula: ")
    tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!!")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_revelada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_revelada += letra_secreta
        else:
            palavra_revelada += '*'

    print(f"Palavras atuais: {palavra_revelada}")

    if palavra_revelada == palavra_secreta:
        print("Voce Ganhou!!!")
        print(f"A palavra era: {palavra_secreta}")
        print(f"Tentativas realizadas: {tentativas}")
        break
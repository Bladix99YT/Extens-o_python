"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

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

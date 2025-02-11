import random

# Lista de palavras para escolher aleatoriamente
palavras = ["maçã", "banana", "laranja", "uva", "abacate"]

def jogo_da_forca():
    palavra_escolhida = random.choice(palavras)
    palavra_oculta = ["_"] * len(palavra_escolhida)
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print("Você tem 6 tentativas para adivinhar a palavra.")

    while tentativas > 0 and "_" in palavra_oculta:
        print(" ".join(palavra_oculta))
        chute = input("Digite uma letra: ").lower()

        if len(chute) != 1:
            print("Por favor, digite apenas uma letra.")
            continue

        if chute in palavra_escolhida:
            for i, letra in enumerate(palavra_escolhida):
                if letra == chute:
                    palavra_oculta[i] = chute
        else:
            tentativas -= 1
            print(f"Incorreto! Você tem {tentativas} tentativas restantes.")

    if "_" not in palavra_oculta:
        print("Parabéns! Você ganhou!")
    else:
        print(f"Game over! A palavra era {palavra_escolhida}.")

jogo_da_forca()
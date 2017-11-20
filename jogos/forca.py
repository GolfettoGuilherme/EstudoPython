import random

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_arcetadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_arcetadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letras_arcetadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_arcetadas
        print(letras_arcetadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def desenha_forca(erros):
    cabeca = "   "
    corpo = " "
    pernas = "   "
    bracos = "   "
    if erros >= 1:
        cabeca = "(_)"

    if erros >= 2:
        bracos = " | "
        corpo = "|"

    if erros >= 3:
        bracos = "\\|/"

    if erros >= 4:
        pernas = "/ \\"

    print("  _______       ")
    print(" |/      |      ")
    print(" |      {}  ".format(cabeca))
    print(" |      {}  ".format(bracos))
    print(" |       {}     ".format(corpo))
    print(" |      {}   ".format(pernas))
    print(" |              ")
    print("_|___           ")
    print()


def imprime_mensagem_abertura():
    print("********************************")
    print("***Bem vindo ao jogo de Forca***")
    print("********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in
                        palavra]  # inicia a lista atribuindo o valor para cada letra na palavra secreta


def pede_chute():
    return input("Qual letra:").strip().upper()


def marca_chute_correto(palavra_secreta, chute, letras_arcetadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_arcetadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("Você ganhou!")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Você perdeu!")
    print("A palavra era {}".format(palavra_secreta))

if __name__ == "__main__":
    jogar()
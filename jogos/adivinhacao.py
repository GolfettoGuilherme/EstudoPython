import random


def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Nével:"))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite o seu número entre 1 e 100: "))
        print("Você digitou:", chute)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        eh_maior = chute > numero_secreto
        eh_menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if eh_maior:
                print("Erro, o chute foi maior que o numero secreto")
            elif eh_menor:
                print("Erro, o chute foi menor que o numero secreto")
            pontos_perdidos = numero_secreto - chute
            pontos -= abs(pontos_perdidos)

    print("O número secreto era {}".format(numero_secreto))
    print("Fim do Jogo")


if __name__ == "__main__":
    jogar()

import time
import random

name = input("Digite seu nome:")
print("Ola, " + name, "hoje de jogar!\n")
time.sleep(1) #fazer o programa esperar 1 segundo
print("Iniciando jogo...\n")
time.sleep(0.5)

lista = ("Camila", "Gabriela", "Beatriz", "Isabela")

randomNumber = random.randint(0,len(lista) - 1)

palavra = lista[randomNumber]
word = palavra
guesses = ''
turns = 10

while(turns > 0):
    failed = 0

    for char in word:
        if char in guesses:
            print(char),
        else:
            print("_"),
            failed += 1

    if failed == 0 :
        print("\nYou win")
        break
    guess = input("Digite uma letra:")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Errou\n")
        print("Você tem ainda:", turns, " palpites")

        if turns == 0:
            print("Você perdeu\n")

# Crie um programa para adivinhar um número de 0 a 20, com 3 tentativas e dicas

from math import floor
from random import randint

numero_aleatorio = randint(0, 20)

c = 1
while c < 4:
    print("-=" * 20)
    numero = int(input("Digite um número entre 0 e 20: "))
    if numero == numero_aleatorio:
        print("Acertou Miseravi!")
        break
    else:
        print("Você Errou :/")
        if c != 3:
            print(f"Você ainda tem { 3 - c } tentativas")
            print("O número é maior" if numero < numero_aleatorio else "O número é menor")
        else:
            print(f"Acabou as suas tentativas!\nA resposta correta é : {numero_aleatorio}")
    c += 1
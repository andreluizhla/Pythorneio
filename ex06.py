# Faremos um bolão da megasena… faça um programa que gere 6 jogos de 6 números cada para jogarmos
from random import randint

print('-=' * 20)
print("Bolão do Terceirão!")
print('-=' * 20)

for jogo in range(1, 7):
    print(f"Jogo n° {jogo}: ", end='')
    for numeros in range(0, 6):
        print(randint(1, 60), end='') 
        if numeros != 5:
            print(end=', ')
    print()

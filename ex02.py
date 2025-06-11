# Entre com uma data de nascimento e indique qual o signo do zodíaco

dia = int(input("Digite o seu dia de nascimento: "))
mes = int(input("Digite o seu mês de nascimento: "))

if (31 >= dia >= 21 and mes == 3) or (1 <= dia <= 20 and mes == 4):
    print("Áries")

elif (30 >= dia >= 21 and mes == 4) or (1 <= dia <= 20 and mes == 5):
    print("Touro")

elif (31 >= dia >= 21 and mes == 5) or (1 <= dia <= 20 and mes == 6):
    print("Gêmeos")

elif (30 >= dia >= 21 and mes == 6) or (1 <= dia <= 21 and mes == 7):
    print("Câncer")

elif (31 >= dia >= 22 and mes == 7) or (1 <= dia <= 22 and mes == 8):
    print("Leão")

elif (31 >= dia >= 23 and mes == 8) or (1 <= dia <= 22 and mes == 9):
    print("Virgem")

elif (30 >= dia >= 23 and mes == 9) or (1 <= dia <= 22 and mes == 10):
    print("Libra")

elif (31 >= dia >= 23 and mes == 10) or (1 <= dia <= 21 and mes == 11):
    print("Escorpião")

elif (30 >= dia >= 22 and mes == 11) or (1 <= dia <= 21 and mes == 12):
    print("Sagitário")

elif (31 >= dia >= 22 and mes == 12) or (1 <= dia <= 20 and mes == 1):
    print("Capricórnio")

elif (31 >= dia >= 21 and mes == 1) or (1 <= dia <= 19 and mes == 2):
    print("Aquário")

elif (29 >= dia >= 20 and mes == 2) or (1 <= dia <= 20 and mes == 3):
    print("Peixes")

else:
    print("Data de Nascimento Inválido!")

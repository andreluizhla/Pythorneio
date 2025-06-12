# Faça um programa para calcular, com base na sua data de nascimento e hora, quantos dias e horas a pessoa tem de vida “vivida” 

import datetime
from math import floor

dia = int(input("Digite o dia que você nasceu: "))
mes = int(input("Digite o mês que você nasceu: "))
ano = int(input("Digite o ano que você nasceu: "))
hora = int(input("Digite à que horas você nasceu: "))

nasceu_data = datetime.datetime(ano, mes, dia, hora)

dia_atual = datetime.datetime.now()

dias_horas_vividos = dia_atual - nasceu_data

print(f"Você viveu {dias_horas_vividos.days} dias e {floor(dias_horas_vividos.seconds / 3600)} horas")

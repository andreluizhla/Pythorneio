# Entre com uma data qualquer e o programa deverá dizer em qual dia da semana caiu esta data

from datetime import date

dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês: "))
ano = int(input("Digite um ano: "))

data = date(ano, mes, dia)
dia_semana_int = data.weekday()
dias_semana_list = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

dia_semana_day = dias_semana_list[dia_semana_int]

print(f"O dia {data.day}/{data.month}/{data.year} caiu no dia {dia_semana_day}")
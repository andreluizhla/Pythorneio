# Entro com duas data e calcule o número de dias entre estas duas datas
from datetime import date

dia_first = int(input("Digite o primeiro dia: "))
mes_first = int(input("Digite o primeiro mês: "))
ano_first = int(input("Digite o primeiro ano: "))

data_first = date(ano_first, mes_first, dia_first)

dia_last = int(input("Digite o último dia: "))
mes_last = int(input("Digite o último mês: "))
ano_last = int(input("Digite o último ano: "))

data_last = date(ano_last, mes_last, dia_last)

distancia = data_last - data_first

print(f"O número de dias entre as datas: {data_first.day}/{data_first.month}/{data_first.year} e {data_last.day}/{data_last.month}/{data_last.year}")
print(f"É de {distancia.days} dias.")

# Programa de Roma… este programa deve transformar números arábicos entre 1 e 10000 em algarismo romanos

# Numeração romana:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# v = 5000
# x = 10000

def numero_romano(numero : int, decimal : int) -> str:
    numeracao_romana = [["I", "V", "X"], ["X", "L", "C"], ["C", "D", "M"], ["M", "v", "x"], ["x"]]
    tipo_numero = numeracao_romana[decimal]
    if 1 <= numero <= 3:
        return (tipo_numero[0] * numero)
    elif numero == 4:
        return (tipo_numero[0] + tipo_numero[1])
    elif numero == 5:
        return (tipo_numero[1])
    elif 6 <= numero <= 8:
        return (tipo_numero[1] + tipo_numero[0] * (numero - 5))
    elif numero == 9:
        return (tipo_numero[0] + tipo_numero[2])
    else:
        return ""

numero = str(input("Digite um número: "))
if 10000 >= int(numero) >= 1:
    print(f"O valor {numero} em algarismos romanos é igual a: ", end='')
    for c in range (1, len(numero) + 1):
        print(numero_romano(int(numero[c - 1]), len(numero) - c), end='')
else:
    print("Valor inválido")

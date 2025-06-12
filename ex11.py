# Conversor binário… com este programa você entrará com um número decimal inteiro qualquer e ele o converterá para binário

numero = int(input("Digite um número: "))

binario = bin(numero).lstrip("-0b")

print(f"O número {numero} em binário é {binario}")

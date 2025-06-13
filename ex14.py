# Dados os 3 lados de um triângulo, faça um código para calcular a área deste triângulo

lado1 = int(input("Digite o 1º lado do triângulo: "))
lado2 = int(input("Digite o 2º lado do triângulo: "))
lado3 = int(input("Digite o 3º lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    s = (lado1 + lado2 + lado3) / 2
    area = (s * (s-lado1) * (s-lado2) * (s-lado3)) ** (1/2)
    print(f"A área do triângulo é: {area:.3f}")
else:
    print("Os lados informados não formam um triângulo")
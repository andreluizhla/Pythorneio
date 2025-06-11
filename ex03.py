# Faça um programa para calcular a tabuada de um número

# 3 x 0 = 0
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ...
# 3 x 10 = 30

# Loops 

# c = 0
# while c <= 10:
#     print(c)
#     c = c + 1

numero = int(input("Digite um número: "))

for c in range(0, 11):
    print("{} x {} = {}".format(numero, c, c * numero))

# Calcule a sequência de fibonacci. A condição de parada será a quantidade de termos que o usuário indicar para processar… por exemplo: 
# Qtde de Termos: 7
# Programa mostrará: 0, 1, 1, 2, 3, 5, 8

numero_termos = int(input("Digite a quantidade de dígitos à serem exibidos: "))

termo = 0
anterior = 0
proximo = c =  0
while c < numero_termos:
    print(termo)
    proximo = termo + anterior
    anterior = termo
    termo = proximo
    termo += 1 if termo == 0 else 0
    c += 1

# Entre com suas notas em Programação no ano passado nos 3 trimestres e calcule: a média, a mediana e o desvio padrão

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))

lista_notas = [nota1, nota2, nota3]

media = (nota1+nota2+nota3) / 3
mediana = sorted(lista_notas)[1]

somatoria = 0

for nota in lista_notas:
    somatoria += ( nota - media ) ** 2

desvio_padrao_populacao = ( ( somatoria ) / 3 ) ** (1/2)
# Se o aluno tem que fazer mais trabalhos, usar a próxima função:
# desvio_padrao_amostra = ( ( somatoria ) / 2 ) ** (1/2)

print('-=' * 20)
print(f"A Média das suas notas é: {media}")
print(f"A Mediana das suas notas é: {mediana}")
print(f"O Desvio Padrão por População das suas notas é: {desvio_padrao_populacao:.3f}")
# print(f"O Desvio Padrão por Amostra das suas notas é: {desvio_padrao_amostra}")
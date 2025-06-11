# Peça um nome e idade e escreva na tela, em duas linhas:
# O nome em LETRAS MAIÙSCULAS
# O ano de nascimento baseado na idade

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

nome_maiusculo = nome.upper()
ano_nacimento = 2025 - idade

print(nome_maiusculo)
print(ano_nacimento)

# texto = "" ou '' => string ou str
# inteiro = 17 => int

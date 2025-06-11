# Entre com um programa que, com o ano do nascimento ele mostre o signo no horóscopo chinês

ano_nascimento = int(input("Digite o seu ano de nascimento: "))

ano_inicio = 1960

signos = ["rato", "boi", "tigre", "lebre", "dragao", "cobra", "cavalo", "ovelha", "macaco", "galo", "cao", "Porco"]
resto = (ano_nascimento - ano_inicio) % 12
print(signos[resto])

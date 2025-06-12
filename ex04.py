# Entre com um programa que, com o ano do nascimento ele mostre o signo no horóscopo chinês

ano_nascimento = int(input("Digite o seu ano de nascimento: "))

ano_inicio = 1960

signos_lista = ["Rato", "Boi", "Tigre", "Lebre", "Dragão", "Cobra", "Cavalo", "Ovelha", "Macaco", "Galo", "Cão", "Porco"]
resto = (ano_nascimento - ano_inicio) % 12
signo = signos_lista[resto]
print(f"O seu signo é de {signo}")

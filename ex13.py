# Será que é bissexto? Entre com um ano qualquer e verifique se ele é bissexto ou não com seu programa

ano = int(input("Digite um ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é Bissexto!")
else:
    print(f"O ano {ano} Não é Bissexto")
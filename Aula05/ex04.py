altura = float(input("Digite o sua altura em metros :"))
sexo = input("Digite seu sexo: h para homem ou m mulher ")
if sexo == "h":
    print(f"O seu peso ideal é {(72.7 * altura) - 58}kg")
else:
    print(f"O seu peso ideal é {(62.1 * altura) - 44.7}kg")


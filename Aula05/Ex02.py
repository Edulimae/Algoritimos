nota_a = float(input("Entre com o valor da primeira nota: "))
nota_b = float(input("Entre com o valor da segunda nota: "))
nota_c = float(input("Entre com o valor da terceira nota: "))
media = (nota_a + nota_b + nota_c) / 3
nota_exame=0

if media < 3:
    resultado = "Reprovado"
else:
    if media < 7:
        resultado = "Exame"
        nota_exame = 12 - media
    else:
        resultado = "Aprovado"

print(f"Média {media:5.2f} - {resultado}!")
if nota_exame != 0:
    print(f"Tem que tirar no minimo {nota_exame:5.2f}")



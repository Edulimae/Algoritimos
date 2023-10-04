#EXERCÍCIO 3
#Faça um algoritmo que leia o valor do peso e da altura de 20 pessoas.
# Ao final, o algoritmo deve mostrar: - O peso médio - A altura média
#- O maior e o menor IMC Obs: IMC (Índice de Massa Corporal) – calculado a
#partir da fórmula: IMC = MASSA / (ALTURA * ALTURA)

s_peso = 0
s_altura = 0
maior_imc = 0
menor_imc = 0
for i in range (1,5):
    peso = float(input(f"Entre com o valor do peso da {i}ª pessoa: "))
    altura =float(input(f"Entre com o valor da altura da {i}ª pessoa: "))
    s_peso = s_peso + peso
    s_altura = s_altura + altura
    imc = peso / (altura * altura)
    if maior_imc == 0:
        maior_imc = imc
        menor_imc = imc
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc
media_peso = s_peso / (i)
media_altura = s_altura / (i)

print(f"Peso médio = {media_peso:5.2f}")
print(f"Altura média = {media_altura:5.2f}")
print(f"Maior IMC = {maior_imc:.2f}")
print(f"Menor IMC = {menor_imc:.2f}")
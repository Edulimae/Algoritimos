#EXERCÍCIO 2
#Faça um algoritmo que calcule a soma dos primeiros 50 números pares. Este algoritmo não
# recebe valores do teclado. Os primeiros números pares são 2, 4, 6...

soma = 0
for i in range(0,51):
    soma = soma + (i*2)
print("O valor da soma dos 50 primeiros números pares é: ", soma)
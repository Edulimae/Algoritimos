#EXERCÍCIO 7
#Faça um programa que calcule os 10 primeiros números da sequencia de Fibonacci
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2594…
# Como se vê, a composição é formada por números que são o resultado da soma dos
# dois anteriores: 0 + 1 = 1 / 1 + 1 = 2 / 2 + 1 = 3 / 3 + 2 = 5 / 5 + 3 = 8

ultimo = 1
penultimo = 1
for f in range(1,15):
    if f == 1 or f == 2:
        print(1)
    else:
        seq = ultimo + penultimo
        penultimo = ultimo
        ultimo = seq
    #    print(f"seq{seq}  ultimo {ultimo} penultimo {penultimo}")
        print(seq)
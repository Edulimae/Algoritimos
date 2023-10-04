# Construa um algoritmo que calcule a média  aritmética de um conjunto de números pares que
# forem fornecidos pelo usuário. O valor de finalização será a entrada do número 0. Observe
# que nada impede que o usuário forneça quantos números ímpares quiser, com a ressalva de que
# eles não poderão ser acumulados.

s_par = 0
escolha = 1
resto = 0
n = 0
while escolha != 0:
    par = int(input("Digite um número par qualquer para cálculo da média: "))
    resto = par % 2
    if resto == 0:
        s_par = s_par + par
        n = n + 1
    escolha = int(input("Deseja acrescentar outro número? digite 1 > sim e  0 > não "))

print(f"O resultado da média do(s) {n} número(s) par(es) é {s_par / n:.0f}.")
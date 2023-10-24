#Faça um algoritimo que armazenará os 10 primeiros primos acima de 100
#em uma tupla. Ao final, o algoritimo deve mostrar os valores dessa estrutura de
#dados
primos = []
i = 0
n = 100
while i < 10:
    primo=True
    for k in range(2, n//2):
        if (n % k) == 0:
            primo = False
            break
    if primo:
        primos.append(n)
        i = i + 1
    n = n + 1
t = tuple(primos)

for x in range(len(t)):
    print(t[x], end= ' - ')

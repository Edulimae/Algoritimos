#Faça um Algoritmo que simule 6000 jogadas de um dado de 6 faces. Para simular o
#resultado utilize a função randint Ao final, mostre a frequência de sorteio de
#cada uma das faces
from random import randint
lista = [0]*6
for _ in range (6000):
    n = randint(1,6)
    lista[(n-1)] = lista[(n-1)]+1

p=[0]*6
for i in range(0,6):
    p[i] = (lista[i] / 6000) * 100
    print(f'{i+1} - {p[i]:.2f}% - {lista[i]} vezes')





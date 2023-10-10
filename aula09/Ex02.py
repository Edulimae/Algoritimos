#Faça um algorimto que carregue um vetor de 10 elementos numéricos inteiros.
#Após a finalização da entrada, o algoritmo deve escrever o maior valor e sua posição
lista = []
for i in range (5):
    lista.append(int(input(f'Digite o número {i+1}: ')))

pos = 0
maior = lista[pos]

for n in range(0, len(lista)):
    if lista[n] >= maior:
        maior = lista[n]
        pos = n

print(f'O maior elemento é {maior} no índice {pos}.')


#Faça um algoritmo que carregue um vetor de 10 elementos numéricos inteiros.
#Após a finalização da entrada, o algoritmo deve escrever o mesmo vetor, na ordem
#inversa de entrada.
lista = []
for i in range(0,10):
    lista.append(int(input(f'Digite o número {i+1}: ')))

for i in lista[::-1]:
    print(i, end=' ')

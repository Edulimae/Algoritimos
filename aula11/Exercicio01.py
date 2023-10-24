#Faça um algoritmo que carregue uma tupla de 10 elementos numéricos inteiros.
#Após a finalização da entrada, o algoritmo deve escrever a mesma tupla, na ordem
#inversa de entrada.

lista = []
i = 0
while i < 10:
    x = int(input('Digite um número: '))
    lista.append(x)
    i = i + 1

t = tuple(lista)

print(t)
print(t[::-1])






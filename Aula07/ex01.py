#EXERCÍCIO 1
#Faça um algoritmo que leia um valor N inteiro #e positivo, calcule e mostre o valor E,
#conforme a fórmula a seguir. E = (2 ** 1) + (2 ** 2) + (2 ** 3) + ... + (2 ** N)

e = 0
numero = int(input("Entre com o valor de um número inteiro: "))
for i in range(1,numero+1):
    e = e + (2**i)
print(f"O valor de e = {e}")
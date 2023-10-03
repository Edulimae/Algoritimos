# EXERCÍCIO 6
#Faça um algoritmo para determinar se um determinado vetor, digitado pelo usuário, é
#um palíndromo. Palíndromo: lido da direita para a esquerda,ou vice versa, representam
# a mesma coisa. Ex: AMA
palavra = input("Entre com uma palavra palíndromo: ")
palavra_igual = palavra[::-1].lower()

if palavra.lower() == palavra_igual.lower():
    print(f"A palavra {palavra} é um palíndromo")
else:
    print(f"A palavra {palavra} não é um palíndromo")
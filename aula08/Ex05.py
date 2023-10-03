# EXERCÍCIO 5
#Faça um algoritmo para determinar quantas palavras existem em uma determinada frase
#Obs: tanto a palavra, quanto a frase, devem ser informadas pelo usuário.
frase = input("Digite um texto qualquer para testes: ")
palavra = input("Digite a palavra a ser comparada: ")

qtd = frase.count(palavra)
total_palavras = frase.count(' ') + 1

print(f"A frase possui um total de {total_palavras} palavras")
print(f"A palavra {palavra} foi encontrada {qtd} vezes na frase")
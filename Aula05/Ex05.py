#Faça um algoritmo que leia o ano de nascimento de uma pessoa, calcule e mostre sua idade e, também, #verifique e mostre se ela já tem idade para votar (16anos ou mais) e para conseguir a Carteira
#de Habilitação (18 anos ou mais).
ano = int(input('Qual o ano de seu nascimento: '))
idade = 2023 - ano
if idade < 16:
    print(f'Você ainda não pode votar nem dirigir pois só tem {idade} anos de idade')
elif idade < 18:
    print(f'Você já pode votar, mas ainda não pode dirigir pois só tem {idade} anos de idade')
else:
    print(f'Parabéns você já pode fazer os testes para sua carteira de habilitação pois já tem {idade} anos de idade')
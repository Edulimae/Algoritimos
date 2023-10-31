#Faça uma algoritimo que carregue um dicionário de 10 elementos onde a chave
#é o nome e idade da pessoa [pelo menos 5 pares]. Deposi de carregar, mostre todos
# os nomes que tenham idade maior que a média das idadesdic={}
maior_sobrenome=''
media_idade=0
soma_idade=0
dic={}
dend={}

for i in range(1,6):
    nome=input(f'Qual o nome da {i}ª pessoa:  ')
    idade=int(input(f'Qua a idade da {i}ª pessoa: '))
    dic[nome]=idade
    soma_idade+=idade

media_idade = soma_idade / 5
print(f'A médida das idades é {media_idade:.2f}')

for chave, valor in dic.items():
    if valor >= media_idade:
        dend[chave]=valor
        print(f'Nome {chave} idade {valor}')



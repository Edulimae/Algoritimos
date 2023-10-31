#Faça uma algoritimo que carregue um dicionário de 10 elementos onde a chave
#é o sobrenome da pessoa e o valor a sua idade. Após a finalização de entarada,
#o algoritimo deve escrever o sobrenome da pessoa com amior idade
dic={}
maior_sobrenome=''
maior_idade=0
for i in range(1,6):
    nome=input(f'Qual o sobrenome da {i}ª pessoa:  ')
    idade=int(input(f'Qua a idade da {i}ª pessoa: '))
    dic[nome]=idade
    print(dic)
for chave, valor in dic.items():
    if valor > maior_idade:
        maior_idade=valor
        maior_sobrenome=chave

print(f"O sobrenome da pessoa com maior idade é {maior_sobrenome} com {maior_idade} anos")




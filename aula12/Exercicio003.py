#Faça algoritmo que carregue duas listas de 5 elementos numéricos inteiros cada um. A
#partir dessas duas listas, crie um conjunto da união entre essas duas listas
l1=[]
l2=[]
for i in range (1,6):
    l1.append(int(input(f'Entre com o {i}º número inteiro da 1ª lista: ')))
    l2.append(int(input(f'Entre com o {i}° número inteiro da 2ª lista: ')))
print(f'lista 1 {l1}, lista 2 {l2}')
a=set(l1).union(set(l2))

print ('Conjunto da união entre as duas listas:')
print (a)


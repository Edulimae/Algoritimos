#Esse algoritimo recebe a lista de jogos feitos e depois apresenta a quantidade  números sorteados
import random
jogos = 0
numbers = []
numeros = []
numerosall = []
resultado = []
n = int(1)
s = 0
acertos = []

#for i in range(1,16):
#    s = s + 1
#    resultado.append(int(input(f'Digite o {s}° número sorteado: ')))
resultado=[1,2,4,5,6,7,11,12,13,15,17,18,20,21,24]

sel = int(input('Quantos números você deseja jogar: '))
jogos = int(input('Digite a quantidade de volantes que deseja fazer: '))
while jogos > 0:
    jogos = jogos - 1
    for n in range (1,26):
        numerosall.append(n)
        random.shuffle(numerosall)
        numeros = numerosall[0:(sel)] 
        
    for i in numeros:
        for j in resultado:
            if i==j:
                acertos.append(j)
                numerosall=[]              
    print (f'Você acertou {len(acertos)} números, foram eles {sorted(acertos)}')
    print (f'Números escolhidos                  {sorted(numeros)}')
    #print (sorted(numeros))
    numeros=[]
    acertos=[]
        
print (f'Os números sorteados foram: {resultado}')
      



 
    

#i=0
#x=1
#games=int(input('Digite a quantidade de números apostados: '))
#while i < games:
#    numbers.append(input("Informe um número na entre 1 e 25 para aposta na lotofácil: "))
#    i=i+1
#print(numbers)    
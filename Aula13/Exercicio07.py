#Crie uma função que re

from funcoes import ehprimo
primo = 0
numero = int(input('Digite um número maior que zero: '))
if numero != 0:
    for i in range(1,numero+1):
        if ehprimo(i):
            primo = primo + 1
print(primo)
from funcoes import ehpar
from funcoes import ehprimo

v3 = int(input('Digite um numero real: '))
if ehpar(v3):
    print('O número é par!')
else:
    print('O número é impar')
v4 = int(input('Digite um numero real: '))
if ehprimo(v4):
    print('É primo')
else:
    print('É par')


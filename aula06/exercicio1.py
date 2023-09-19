numero = int(input("Digite um número inteiro para saber se ele é divisível por 5 e 3 ao mesmo tempo:  "))
if numero % 3 == 0 and numero % 5 == 0:
    print(f'O número {numero} é divisível por 3 e 5 ao mesmo tempo')
else:
    print(f'O número {numero} não é divisível por 3 e 5 ao mesmo tempo')

#FAZER UM PROGRAMA QUE RECEBA DOIS NÚMEROS E EXECUTE AS OPERAÇÕES LISTADAS A SEGUIR DE ACORDO COM A
#ESCOLHA DO USUÁRIO:
#1. Média entre os números digitados
#2. Diferença do maior pelo menor
#3. Produto entre os números digitados
#4. Divisão do primeiro pelo segundo
n1 = float(input('Digite o valor de um número: '))
n2 = float(input('Digite o valor de outro numero: '))
sel = int(input('Digite uma opção para o cálculo: \n1. Média entre os números digitados \n2. Diferença do maior pelo menor \n3. Produto entre os números digitados \n4. Divisão do primeiro pelo segundo\n opção: '))
if sel == 1:
    result = (n1 + n2) / 2
    operacao = 'da média'
elif sel == 2:
    if n1 > n2:
        result = n1 - n2
        operacao = 'da subtração'
    else:
        n1, n2 = n2, n1
        result = n1 - n2
        operacao = 'da subtração' 
elif sel == 3:
    result = n1 * n2
    operação = 'do produto'
elif sel == 4:
    result = n1 / n2 
    operação = 'da divisão'           
print (f'O valor {operacao} entre os números {n1:.0f} e {n2:.0f} é {result:.2f}.')        
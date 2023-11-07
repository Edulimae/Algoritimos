#Crie uma função que receba como parametro 3 numeros inteiros( representando
#horas, minutos e segundos). A função deve converter em segundos
from funcoes import converte_time
hora = int(input('Digite o valor de hora: '))
minuto = int(input("Digite o valor de minuto: "))
segundo = int(input('Digite o valor de segundos: '))
print(f'O valor correspondente em segundos é  {converte_time(hora, minuto, segundo)}')

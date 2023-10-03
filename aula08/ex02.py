#EXERCÍCIO 2
#Faça um algoritmo que solicite uma data no formato de uma string – dd/mm/aaaa. Mostre
#essa data no formato AAAAMMDD
data = input("Entre com a data dd/mm/aaaa: ")
print(f"{data[6:10]}{data[3:5]}{data[0:2]}")

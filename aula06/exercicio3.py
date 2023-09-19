largura = float(input('Entre com o valor da largura do aposento em metros: '))
comprimento = float(input('Entre com o valor do comprimento do aposento em metros: '))
print('Escolha um tipo de lata para o cálculo:')
tipo_lata = int(input('Digite 1 - 18 litros / Digite 2 - 3,6 litros / Digite 3 - 1 litro :'))
porta = (0.80 * 2.10)
area_largura= largura * 2.80
area_comprimento= comprimento * 2.80
area_total= (area_largura * 2) + (area_comprimento * 2) - porta
qtde_tinta = (area_total / 3)
if tipo_lata == 1:
    print(f'A quantidade de latas de 18 litros para pintura é {qtde_tinta / 18:4.2f} latas')
elif tipo_lata == 2:
    print(f'A quantidade de latas de 3,6 litros para pintura é {qtde_tinta / 3.6:4.2f} latas')
elif tipo_lata == 3:
    print(f'A quantidade de latas de 1 litros para pintura é {qtde_tinta / 1:4.2f} latas')
else:
    print('A escolha de tipo lata não é válida')

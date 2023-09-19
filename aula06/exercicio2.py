valor_compra = float(input('Digite o valor da compra pra saber o desconto: R$ '))
if valor_compra <= 1000:
    print(f'O valor do desconto é de R$ {valor_compra * 0.10:6.2f}')
elif valor_compra <= 5000:
    print(f'O valor do desconto é de R$ {valor_compra * 0.20:6.2f}')
else:
    print(f'O valor do desconto é de R$ {valor_compra * 0.30:6.2f}')


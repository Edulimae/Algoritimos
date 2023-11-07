# Definição de funções
qtd = 5


def desenha(qtd=20):
    for _ in range(0, qtd):
        print('-=', end='')
    print()


desenha()
print('*** Uso de funções ***')
desenha(25)

a = int(input("Digite o valor do lado A "))
b = int(input("Digite o valor do lado B "))
c = int(input("Digite o valor do lado C "))
if ((a + b > c) and (b + c > a) and (a + c > b)):
    #é um triângulo
    if (a == b == c):
        print("É um triângulo equilátero!")
    elif ((a == b) or (b == c) or (c == a)):
        print("É um triângulo Isósceles!")
    else:
        print("É um triângulo Escaleno")
else:
    #não é um triângulo
    print("Não é um triângulo possível!")

lado_a = int(input("Digite o valor do lado A"))
lado_b = int(input("Digite o valor do lado B"))
lado_c = int(input("Digite o valor do lado C"))
if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_a + lado_c > lado_b:
    match case 1: \
        lado_a == lado_b == lado_c = "Equilatero"

else:
    print("Não é um triângulo possível!")
        else
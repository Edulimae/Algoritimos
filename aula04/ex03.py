ano_nascimento = int(input("Entre com ano de seu nascimento com 4 digitos: "))
ano_atual = int(input("Entre com o ano atual com 4 digitos: "))
idade_ano = ano_atual - ano_nascimento
idade_meses = idade_ano * 12
idade_dias = idade_ano * 365
idade_semanas = idade_ano * 53
print("Sua idade é", idade_ano, "anos")
print("Sua idade em meses é", idade_meses, "meses")
print("Sua idade em dias é", idade_dias, "dias")
print("Sua idade em semanas é", idade_semanas, "semanas")

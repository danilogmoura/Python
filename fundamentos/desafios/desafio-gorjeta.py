# Solicite ao usuário o total de uma conta de restaurante
# e a porcentagem de gorjeta que ele gostaria de dar.
# Calcule e mostre o valor total da conta incluindo a gorjeta.

valor = float(input("Valor tota (R$): "))
gorjeta = float(input("Percentual da gorjeta (0-100): "))

valor_gorjeta = valor * (gorjeta / 100)
valor_total = valor + valor_gorjeta

print(f"""
Dado o valor da conta de {valor} sem a gorjeta
aplicando {gorjeta}% (R${valor_gorjeta}) de gorjeta
o valor total da conta a ser paga será de R${valor_total}
""")

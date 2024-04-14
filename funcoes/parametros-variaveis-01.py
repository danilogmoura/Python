def calcular_media(*numeros):
    print(type(numeros))
    return sum(numeros) / len(numeros)


media = calcular_media(7, 8, 7.5)
print(f"O valor da média é {media:.1f}")

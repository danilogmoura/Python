numeros = [10, 20, 30]
indice_20 = numeros.index(20)
print(indice_20)  # Saída: 1

numeros.append(10)
quantidade_10 = numeros.count(10)
print(quantidade_10)  # Saída: 2

numeros = [56, 32, 44, 4, -32, 7]
numeros.sort();
print(numeros)  # Saída: [-32, 4, 7, 32, 44, 56]

numeros.reverse()
print(numeros)  # Saída: [56, 44, 32, 7, 4, -32]

numeros.clear()
print(numeros)  # Saída: []

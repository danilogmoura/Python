# Escreva um código em Python que gere os números da mega-sena
# Primeiramente solicite para o usuário informar quantidade de
# números da aposta (entre 6 e 20) e depois gere uma lista com
# o tamanho solicitado com números não repetidos entre 1 e 60.

import random

print("Jogo da Mega-Sena")

while True:
    quantidade_numeros = int(input("Informe a quantidade de números [6-20]: "))

    if quantidade_numeros >= 6 and quantidade_numeros <= 20:
        break

    print("Informe uma quantidade de números válido:")

contador = 1
numeros_aposta = set()
while len(numeros_aposta) < quantidade_numeros:
    numero = int(input(f"Digite o {contador}º número: "))

    if numero in numeros_aposta:
        print(f"O número {numero} já está registrado, escolha um novo entre 1 e 60: ")
    elif numero < 1 or numero > 60:
        print(f"O número {numero} é inválido, escolha um novo entre 1 e 60: ")
    else:
        numeros_aposta.add(numero);
        contador += 1;

numeros_sorteados = set()
while len(numeros_sorteados) <= 6:
    numeros_sorteados.add(random.randint(1, 60))

print(numeros_aposta)
print(sorted(numeros_sorteados))

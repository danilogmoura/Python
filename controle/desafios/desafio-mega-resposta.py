# Escreva um código em Python que gere os números da mega-sena
# Primeiramente solicite para o usuário informar quantidade de
# números da aposta (entre 6 e 20) e depois gere uma lista com
# o tamanho solicitado com números não repetidos entre 1 e 60.

import random

quantidade = int(input("Informe a quantidade [6-20]: "))

if 6 <= quantidade <= 20:
    aposta = random.sample([x for x in range(1, 61)], quantidade)  # Só pegua repetido se existir no array
    aposta.sort()
    print(f"A aposta gerada é {aposta}")
else:
    print("Aposta inválida")

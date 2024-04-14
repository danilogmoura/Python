# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem
# dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80 mk/h

VELOCIDADE_MAXIMA = 80
VALOR_MULTA_EXCEDENTE_POR_KM_HORA = 5

velocidade_veiculo = int(input("Qual a velocidade atual: "))

if velocidade_veiculo > VELOCIDADE_MAXIMA:
    velocidade_excedente = velocidade_veiculo - VELOCIDADE_MAXIMA
    valor_multa = velocidade_excedente * VALOR_MULTA_EXCEDENTE_POR_KM_HORA
    print(f"Você foi multado! A velocidade do seu veículo é {velocidade_veiculo} km/h, "
          f"que é acima da velocidade máxima permitida de {VELOCIDADE_MAXIMA} km/h.\n"
          f"O valor da sua multa é R${valor_multa:.2f}.")
else:
    print("Você escapou. Pode ir embora.")

# Peça para que o usuário insira um número total de segundos
# e converta esse valor para horas, minutos e segundo.

UMA_HORA_EM_SEGUNDO = 3600
UM_MINUTO_EM_SEGUNDO = 60

total_em_segundos = int(input("Informe a quantidade de segundos: "))

hora = total_em_segundos // UMA_HORA_EM_SEGUNDO
resto = total_em_segundos % UMA_HORA_EM_SEGUNDO
minuto = resto // UM_MINUTO_EM_SEGUNDO
segundo = resto % UM_MINUTO_EM_SEGUNDO

print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")

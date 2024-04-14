# Função SEM parâmetro parâmetro e COM retorno

from datetime import datetime, timedelta, timezone

brazilia_tz = timezone(timedelta(hours=-3))


def hora_certa():
    agora = datetime.now(brazilia_tz)
    return f"{agora.hour:02d}:{agora.minute:02d}:{agora.second:02d}"


hora = hora_certa()
print(hora)

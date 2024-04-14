from datetime import datetime, timedelta, timezone

brazil_tzm = timezone(timedelta(hours=-3))


def hora_atual():
    agora = datetime.now(brazil_tzm)
    return agora.hour


def saudacao():
    hora = hora_atual()

    match hora:
        case h if h in range(0, 6):
            s = "Boa madrugada"
        case h if h in range(6, 12):
            s = "Bom dia"
        case h if h in range(12, 18):
            s = "Boa tarde"
        case _:
            s = "Boa noite"

    return s


resultado = saudacao()
print(resultado)
print(saudacao())

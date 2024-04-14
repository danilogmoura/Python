import secrets
from datetime import timedelta, timezone, datetime

BRAZIL_TZ = timezone(timedelta(hours=-3))


def date_time_now():
    return datetime.now(BRAZIL_TZ).strftime("%Y-%m-%d %H:%M:%S")


def criar_usuario(**atributos):
    print(type(atributos))
    usuario = {
        "nome": "",
        "email": "",
        "senha": secrets.token_urlsafe(20),
        "data_criacao": date_time_now(),
        "ativo": True
    }

    usuario.update(atributos)
    return usuario


novo_usuario = criar_usuario(
    nome="Maria Ferreira",
    email="mariafr@email.com"
)

print(novo_usuario)

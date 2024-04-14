import random
from string import ascii_uppercase, ascii_lowercase, digits, punctuation


def criar_senha(tamanho, maiuscula, minuscula, numeros, simbolos):
    caracteres = "".join([
        ascii_uppercase if maiuscula else "",
        ascii_lowercase if minuscula else "",
        digits if numeros else "",
        punctuation if simbolos else ""
    ])

    senha = random.choices(caracteres, k=tamanho)
    senha = "".join(senha);
    return senha


nova_senha = criar_senha(
    tamanho=100,
    maiuscula=True,
    minuscula=True,
    numeros=True,
    simbolos=False)

print(nova_senha)

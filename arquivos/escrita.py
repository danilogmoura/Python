import os

pasta_atual = os.path.dirname(__file__)
caminho_arquivo = os.path.join(
    pasta_atual, "docs", "texto-01.txt"
)

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write("Olá, Estou criando um arquivo com o Python!\n")

linhas = [
    "Escrevendo multiplas linhas",
    "em um arquivo de texto",
    "com Python"
]

with open(caminho_arquivo, 'a') as arquivo:
    # for linha in linhas:
    #     arquivo.writelines(f"{linha}\n")

    arquivo.writelines(f"{linha}\n" for linha in linhas)

import os
from arquivos.listar import listar_arquivos


def ler_arquivor(diretorio, lista_arquivos):
    conteudo = []

    for nome_arquivo in lista_arquivos:
        caminho = os.path.join(diretorio, nome_arquivo)
        with open(caminho) as arquivo:
            conteudo.extend(arquivo.read().splitlines())

    return conteudo


def remover_numero(linhas):
    return [linha for linha in linhas if not linha.isdigit()]


def remover_tempo(linhas):
    return [linha for linha in linhas if "-->" not in linha]


def contar_palavra(linhas):
    palavras = {}

    for linha in linhas:
        linha = linha.translate(
            str.maketrans("", "", "\"#$&?!./0123456789%<>[]()-")
        )

        for palavra in linha.split():
            palavra = palavra.lower()
            palavras[palavra] = palavras.get(palavra, 0) + 1

    palavras = sorted(palavras.items(), key=lambda item: item[1], reverse=True)
    return palavras


def main():
    diretorio_legendas = os.path.join(
        os.path.dirname(__file__), "..", "legendas"
    )

    arquivos_legendas = listar_arquivos(diretorio_legendas, ".srt")
    linhas = ler_arquivor(diretorio_legendas, arquivos_legendas)
    linhas = remover_numero(linhas)
    linhas = remover_tempo(linhas)

    palavras = contar_palavra(linhas)

    print(palavras)


if __name__ == "__main__":
    main()

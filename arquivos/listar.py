import os


def listar_arquivos(pasta, filtro=""):
    lista_arquivos = os.listdir(pasta)

    arquivos_filtrados = []
    for nome_arquivo in lista_arquivos:
        if not filtro or filtro in nome_arquivo:
            arquivos_filtrados.append(nome_arquivo)

    return arquivos_filtrados


def main():
    pasta_atual = os.path.dirname(__file__)
    pasta_legendas = os.path.join(
        pasta_atual, "legendas"
    )

    arquivos = listar_arquivos(pasta_legendas, "04")
    print(arquivos)


if __name__ == "__main__":
    main()

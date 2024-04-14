nome = """
Pedro de Alcântara Francisco António João 
Carlos Xavier de Paula Miguel Rafael Joaquim 
José Gonzaga Pascoal Cipriano Serafim
"""

partes_nome = nome.split()

print(partes_nome)

match partes_nome:
    case [primeiro]:
        sigla = primeiro[0:2]
    # case [primeiro, segundo]:
    #     sigla = primeiro[0] + segundo[0]
    case [primeiro, *m, ultimo]:
        sigla = primeiro[0] + ultimo[0]
    case _:
        sigla = "AL"

print(f"A sigla do usuário é {sigla.upper()}")

# Peça ao usuário que insira uma quantdade de quilômetros
# e converta essa distância para milhas.
# Lembre-se de que 1km = 0.621371mi.

MILHAS_POR_KM = 0.621371

distancia_km = float(input("Informe a quilometragem: "))

distancia_milha = distancia_km * MILHAS_POR_KM

print(f"{distancia_km} Km = {distancia_milha} Mi")

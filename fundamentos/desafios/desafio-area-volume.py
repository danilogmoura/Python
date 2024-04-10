# Solicite ao usuário o raio de um circulo e calcule
# a área (`A = π * r²`) e o volume de uma esfera com esse
# raio (`V = 4/3 * π * r³`).
# Use 3.14159 como aproximação de π

PI = 3.14159

raio = float(input("Informe o valor do raio: "))

area = PI * (raio ** 2)
volume = 4 / 3 * PI * (raio ** 3)

print(f"""
    A área do circulo é {area} m2
    com volume de {volume} m3
""")

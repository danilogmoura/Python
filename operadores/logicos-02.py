terca_feira = bool(int(input("Trabanho de Terça? [0-1]: ")))
quinta_feira = bool(int(input("Trabanho de Quinta? [0-1]: ")))

comprar_tv_60 = terca_feira and quinta_feira
comprar_tv_32 = terca_feira != quinta_feira
tomar_sorvete = comprar_tv_60 or comprar_tv_32
ficar_em_casa = not tomar_sorvete

print("Comprar TV 60'", comprar_tv_60)
print("Comprar TV 32'", comprar_tv_32)
print("Tomar sorverte", tomar_sorvete)
print("Ficar em casa", ficar_em_casa)

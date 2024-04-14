print("Iterando uma lista: ")
lista = [10, 20, 30, 40, 50]
for numero in lista:
    print(numero, end=" ")

print("\nCom indíce: ")
for indice, numero in enumerate(lista):
    print(f"({indice}, {numero})", end=" ")

print("\n\nIterando uma tupla: ")
tupla = (1, 2, 3, 4, 5)
for numero in tupla:
    print(numero, end=" ")

print("\n\nIterando um Set: ")
conjunto = {1, 1, 2, 3, 4, 5, 5, 5}
for numero in conjunto:
    print(numero, end=" ")

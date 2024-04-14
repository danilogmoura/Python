# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Informe o número 1: "))
n2 = int(input("Informe o número 2: "))
n3 = int(input("Informe o número 3: "))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

print(f"O maior número é {maior}!")

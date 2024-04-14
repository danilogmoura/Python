# base_dois = []
#
# for x in range(1, 21):
#     base_dois.append(2 ** x)
#
# print(base_dois)

# List Comprehension
# Modelo [exp for ... if ...]
base_dois = [2 ** x for x in range(1, 21)]
print(base_dois)

base_dois = [2 ** x for x in range(1, 21) if x % 2 == 0]
print(base_dois)

numeros = [x * x for x in range(1, 30) if x % 3 != 0]
print(numeros)

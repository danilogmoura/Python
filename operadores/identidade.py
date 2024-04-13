# Típicos Básicos - Imutáveis
a = 6
b = a
b = 5 + 1

print(id(a))
print(id(b))
print(a == b)
print(a is b)

# Típicos Compostos - Mutáveis
x = [1, 2, 3]
y = [1, 2, 3]

print(id(x))
print(id(y))
print(x == y)
print(x is y)

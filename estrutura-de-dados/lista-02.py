numeros = [1, 2, 3]
numeros.append(100)

print(numeros)  # Saída: [1, 2, 3, 100]

numeros.insert(1, 200)  # Saída: [1, 200, 2, 3, 100]
print(numeros)

numeros.remove(200)
numeros.remove(100)
print(numeros)  # Saída : [1, 2, 3]

# Pilha (Stack) - LIFO -> pop()
pilha_livros = ["MMM", "DDD", "Hábitos Atômicos"]
pilha_livros.append("Range")
print(f"Acabei de ler {pilha_livros.pop()}")
print(f"Acabei de ler {pilha_livros.pop()}")
print(f"Acabei de ler {pilha_livros.pop()}")
print(f"Acabei de ler {pilha_livros.pop()}")

print(pilha_livros)
print(len(pilha_livros))

# Fila (Queue) - FIFO -> pop(0)
fila_kalzone = ["Pedrinho", "Enzo", "Valentina"]
print(f"Qual é o seu pedido {fila_kalzone.pop(0)}")
print(f"Qual é o seu pedido {fila_kalzone.pop(0)}")
print(f"Qual é o seu pedido {fila_kalzone.pop(0)}")

print(fila_kalzone)
print(len(fila_kalzone))

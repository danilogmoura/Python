try:
    divisor = float(input("Informe o divisor: "))
    resultado = 1000 / divisor
    print(f"O resultado da divisão é {resultado:.2f}")
except ZeroDivisionError as e:
    print(f"Não é possível dividir por zero {e.__class__}")
except ValueError:
    print("formata essa porra direito")
except Exception as e:
    print(f"Erros mais genéricos {e.__class__}")

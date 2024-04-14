n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
operacao = input("Informe a operação [+ - * /]: ")

match operacao:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*" | "x":
        resultado = n1 * n2
    case "/":
        resultado = n1 / n2
    case _:
        resultado = None

if resultado is None:
    print(f"O resultadado da operação {n1} {operacao} {n2} = {resultado}.")
else:
    print("Operação não reconhecida.")

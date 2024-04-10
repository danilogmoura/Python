# Peça ao usuário que forneça uma temperatura em Celcius
# e converta-a para Fahrenheit.
# A fórmula de conversão é `F = C * 9/5 + 32`.

temperatura_celcius = float(input("Informe a temperatura em °C: "))

temperatura_fahrenheit = (temperatura_celcius * (9 / 5)) + 32

print(f"A temperatura de {temperatura_celcius}°C equivale a {temperatura_fahrenheit}°F")

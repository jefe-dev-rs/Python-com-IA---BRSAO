# Conversor de Temperatura no Python

"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

# Conversor de Temperatura

# Solicita os dados ao usuário
temperatura = float(input("Digite a temperatura: "))
origem = input("Informe a unidade de origem (C, F ou K): ").upper()
destino = input("Informe a unidade de destino (C, F ou K): ").upper()

# Converte para Celsius primeiro (base de cálculo)
if origem == "C":
    temp_c = temperatura
elif origem == "F":
    temp_c = (temperatura - 32) * 5/9
elif origem == "K":
    temp_c = temperatura - 273.15
else:
    print("Unidade de origem inválida.")
    exit()

# Converte de Celsius para o destino
if destino == "C":
    resultado = temp_c
elif destino == "F":
    resultado = (temp_c * 9/5) + 32
elif destino == "K":
    resultado = temp_c + 273.15
else:
    print("Unidade de destino inválida.")
    exit()

# Exibe o resultado final
print(f"{temperatura:.2f}°{origem} = {resultado:.2f}°{destino}")

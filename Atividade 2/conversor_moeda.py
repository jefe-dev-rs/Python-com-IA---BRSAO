# Conversor de Moeda no Python

valor_real = 100.00
taxa_euro = 6.15
taxa_dolar = 5.20

valor_dolar = valor_real / taxa_dolar
valor_euro = valor_real / taxa_euro

print(f'O valor em Real é: R$ {round(valor_real, 2)}')
print(f'O valor em Dólar é: US$ {round(valor_dolar, 2)}')
print(f'O valor em Euro é: € {round(valor_euro, 2)}')

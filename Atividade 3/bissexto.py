# Ano Bissexto em Python

"""
Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

# Verificador de Ano Bissexto

# Solicita o ano ao usuário
ano = int(input("Digite um ano: "))

# Verifica se é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

"""
Explicação da lógica:
Um ano é bissexto se:

for divisível por 4,
mas não for divisível por 100,
exceto se for divisível por 400 (nesse caso, continua sendo bissexto).

Exemplos:
2024 → bissexto
1900 → não bissexto
2000 → bissexto

"""
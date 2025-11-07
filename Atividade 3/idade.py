# Classificador de Idade

"""
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais)."""

# Programa para classificar a idade do usuário

# Solicita a idade
# Programa para classificar a idade do usuário (usando operadores lógicos)

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você é uma Criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um Adolescente.")
elif idade >= 18 and idade <= 59:
    print("Você é um Adulto.")
elif idade >= 60:
    print("Você é um Idoso.")
else:
    print("Idade inválida.")



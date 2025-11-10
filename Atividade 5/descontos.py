# Verificador de Descontos

def calcular_desconto(preco: float, porcentagem: float) -> float:
    """
    Calcula o valor do desconto baseado na porcentagem.
    """
    return preco * (porcentagem / 100)


def preco_final(preco: float, desconto: float) -> float:
    """
    Determina o preço final subtraindo o desconto.
    """
    return preco - desconto


# Programa principal
print("=== Calculadora de Desconto ===")

preco_produto = float(input("Digite o preço do produto (R$): "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))

# Cálculo
valor_desconto = calcular_desconto(preco_produto, porcentagem_desconto)
valor_final = preco_final(preco_produto, valor_desconto)

# Saída formatada
print(f"\nValor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final após desconto: R$ {valor_final:.2f}")

# Cálculo de Porcentagem de Gorjetas

"""
  Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

  Argumentos:
    valor_conta (float): O valor total da fatura.
    porcentagem_gorjeta (float): A porcentagem que você deseja dar (ex: 15 para 15%).

  Retorna:
    float: O valor monetário da gorjeta.
  """

def calcular_gorjeta(total_conta, porcentagem):
    gorjeta = total_conta * (porcentagem / 100)
    return gorjeta

# Exemplo de uso:
valor_total = float(input("Digite o valor total da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta desejada: "))

valor_gorjeta = calcular_gorjeta(valor_total, porcentagem_gorjeta)

print(f"A gorjeta deve ser de R$ {valor_gorjeta:.2f}")
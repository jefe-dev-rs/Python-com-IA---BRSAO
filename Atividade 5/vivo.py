# Verificador de dias de vida

from datetime import datetime

print("=== Calculadora de Dias de Vida ===")

# Entrada da data de nascimento
data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte string para objeto datetime
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

# Data atual
data_atual = datetime.now()

# Cálculo da diferença
dias_vivo = (data_atual - data_nascimento).days

print(f"\nVocê está vivo há aproximadamente {dias_vivo} dias.")

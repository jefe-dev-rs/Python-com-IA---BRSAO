# Programa que gera senhas Aleatórias

'''
1 - Crie um programa que gere senhas aleatórias com letras,
números e símbolos e que o usuário também escolha o tamanho da senha  para criar senhas seguras automaticamente.
'''

import random
import string

def gerar_senha(tamanho):
    # Conjunto de caracteres: letras maiúsculas, minúsculas, números e símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Programa principal
print("=== GERADOR DE SENHAS SEGURAS ===")
try:
    tamanho = int(input("Digite o tamanho da senha: "))
    if tamanho < 4:
        print("⚠️ A senha deve ter pelo menos 4 caracteres para ser segura.")
    else:
        senha = gerar_senha(tamanho)
        print(f"\n🔐 Sua senha gerada é: {senha}")
except ValueError:
    print("❌ Por favor, digite um número válido.")

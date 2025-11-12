# Programa de Busca por meio de uma API

'''
3 - Crie um programa que consulte informações de um  na API ,
retorne logradouro, bairro, cidade e estado do CEP digitado,
caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.
'''
# OBS
'''Entrada do usuário	Resultado
01001000	Mostra o endereço corretamente
0100100 (7 dígitos)	⚠️ Erro: CEP inválido
010010000 (9 dígitos)	⚠️ Erro: CEP inválido
01001-000 (com hífen)	⚠️ Erro: CEP inválido
ABC12345	⚠️ Erro: CEP inválido'''

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        dados = resposta.json()

        # Se o CEP não existir
        if "erro" in dados:
            print("❌ CEP não encontrado. Verifique e tente novamente.")
            return

        # Exibe os dados do CEP
        print("\n=== Resultado da Consulta ===")
        print(f"📍 Logradouro: {dados.get('logradouro', 'Não informado')}")
        print(f"🏘️ Bairro: {dados.get('bairro', 'Não informado')}")
        print(f"🏙️ Cidade: {dados.get('localidade', 'Não informado')}")
        print(f"🗺️ Estado: {dados.get('uf', 'Não informado')}")

    except requests.exceptions.RequestException:
        print("❌ Erro ao conectar à API. Verifique sua conexão e tente novamente.")

# Programa principal
print("=== CONSULTA DE CEP ===")
cep_input = input("Digite o CEP (somente números): ").strip()

# ✅ Validação rigorosa: exatamente 8 números
if len(cep_input) != 8 or not cep_input.isdigit():
    print("⚠️ CEP inválido! O CEP deve conter exatamente 8 números.")
else:
    consultar_cep(cep_input)
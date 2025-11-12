# Programa que busca um usuário fctício por meio de uma API

'''
2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório.
exibindo o nome, e-mail e país desse usuário,
caso houver erro na conexão, mostre uma mensagem de falha.
'''
# OBS: O enunciado não pedia, mas eu quiz buscar apenas usuários Brasileiros.

import requests

def buscar_usuario_brasileiro():
    url = "https://randomuser.me/api/?nat=br"  # Somente usuários do Brasil

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Gera erro se a resposta não for 200

        dados = resposta.json()
        usuario = dados["results"][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print("=== Usuário Brasileiro Gerado ===")
        print(f"👤 Nome: {nome}")
        print(f"📧 E-mail: {email}")
        print(f"🌍 País: {pais}")

    except requests.exceptions.RequestException:
        print("❌ Falha ao conectar à API. Verifique sua conexão e tente novamente.")

# Programa principal
buscar_usuario_brasileiro()

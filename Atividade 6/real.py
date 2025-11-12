# Programa de Consulta do Valor do Real por consulta via API

'''
4 - Crie um programa que realize consultas a  em relação ao Real (BRL)
usando a API mostre valor atual, máxima, mínima e data/hora da última atualização,
caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.
'''

import requests
from datetime import datetime

def consultar_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()

        # A chave vem no formato, por exemplo: "USD" → "USDBRL"
        chave = f"{moeda.upper()}BRL"

        if chave not in dados:
            print("❌ Moeda não encontrada. Verifique o código e tente novamente.")
            return

        info = dados[chave]

        valor_atual = float(info["bid"])
        valor_max = float(info["high"])
        valor_min = float(info["low"])
        atualizacao = datetime.fromtimestamp(int(info["timestamp"]))

        print("\n=== COTAÇÃO ATUAL ===")
        print(f"💰 Moeda: {moeda.upper()} / BRL")
        print(f"📊 Valor atual: R$ {valor_atual:.2f}")
        print(f"📈 Máximo do dia: R$ {valor_max:.2f}")
        print(f"📉 Mínimo do dia: R$ {valor_min:.2f}")
        print(f"⏰ Última atualização: {atualizacao.strftime('%d/%m/%Y %H:%M:%S')}")

    except requests.exceptions.RequestException:
        print("❌ Erro ao conectar à API. Verifique sua conexão e tente novamente.")

# Programa principal
print("=== CONSULTA DE COTAÇÃO ===")
print("Exemplos de moedas: USD (Dólar), EUR (Euro), GBP (Libra), ARS (Peso Argentino)")
moeda = input("Digite o código da moeda que deseja consultar: ").strip().upper()

if len(moeda) != 3 or not moeda.isalpha():
    print("⚠️ Código de moeda inválido! Use 3 letras (ex: USD, EUR, GBP).")
else:
    consultar_moeda(moeda)

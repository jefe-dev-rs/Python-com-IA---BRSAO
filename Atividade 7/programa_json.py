# Programa que cria lê e arquivos no formato JSON

# programa_json.py

import json

def main():
    # Dicionário com dados da pessoa
    pessoa = {
        "nome": "João",
        "idade": 28,
        "cidade": "Belo Horizonte"
    }

    # Nome do arquivo JSON
    nome_arquivo = input("Digite o nome do arquivo JSON para salvar (ex: pessoa.json): ")

    # ----- Salvando o arquivo JSON -----
    try:
        with open(nome_arquivo, "w") as arquivo:
            json.dump(pessoa, arquivo, indent=4)
        print(f"\nArquivo '{nome_arquivo}' salvo com sucesso!\n")

    except Exception as e:
        print("Erro ao salvar o arquivo JSON:", e)
        return  # não tenta ler se não conseguiu salvar

    # ----- Lendo o arquivo JSON -----
    try:
        with open(nome_arquivo, "r") as arquivo:
            dados_lidos = json.load(arquivo)

        print("--- Dados lidos do arquivo JSON ---")
        print("Nome  :", dados_lidos["nome"])
        print("Idade :", dados_lidos["idade"])
        print("Cidade:", dados_lidos["cidade"])

    except FileNotFoundError:
        print("Erro: Arquivo JSON não encontrado.")

    except Exception as e:
        print("Erro ao ler o arquivo JSON:", e)


if __name__ == "__main__":
    main()

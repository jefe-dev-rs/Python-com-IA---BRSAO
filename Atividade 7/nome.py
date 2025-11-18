# Programa que cria arquivo com nome e dados tabulares
# depois mostra o resultado na tela

# programa_tabela.py

def main():
    # Dados das pessoas
    pessoas = [
        ["Nome", "Idade", "Cidade"],
        ["Ana", 25, "São Paulo"],
        ["Carlos", 30, "Rio de Janeiro"],
        ["Mariana", 22, "Curitiba"],
        ["João", 28, "Belo Horizonte"]
    ]

    # Escolha do arquivo
    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: pessoas.txt): ")

    try:
        with open(nome_arquivo, "w") as arquivo:
            print("\n--- TABELA GERADA ---\n")

            for pessoa in pessoas:
                linha = "\t".join(map(str, pessoa))

                # Mostra no terminal
                print(linha)

                # Salva no arquivo
                arquivo.write(linha + "\n")

        print(f"\nArquivo '{nome_arquivo}' salvo com sucesso!")

    except Exception as e:
        print("Erro ao salvar o arquivo:", e)


if __name__ == "__main__":
    main()

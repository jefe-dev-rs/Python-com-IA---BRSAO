# Programa que lê o arquivo

# leitor_arquivo.py

def main():
    nome_arquivo = input("Digite o nome do arquivo para leitura: ")

    try:
        with open(nome_arquivo, "r") as arquivo:
            print("\n--- Conteúdo do arquivo ---\n")
            for linha in arquivo:
                print(linha.strip())  # remove quebras de linha extras

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")

    except Exception as e:
        print("Erro ao ler o arquivo:", e)


if __name__ == "__main__":
    main()

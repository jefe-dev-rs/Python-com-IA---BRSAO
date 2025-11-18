# Programa que lê arquivo CSV

import pandas as pd

# -------------------------------------------------------
# Edite aqui: coloque o nome OU caminho completo do seu CSV
ARQUIVO = "dados.csv"
# Exemplo com caminho completo:
# ARQUIVO = "/home/eujefe/Área de Trabalho/EDN205/Python_com_IA_BRSAO205/Atividade 7/dados.csv"
# -------------------------------------------------------

def main():
    try:
        df = pd.read_csv(ARQUIVO)

        if "tempo_execucao" not in df.columns:
            print("Erro: a coluna 'tempo_execucao' não existe no arquivo.")
            return

        media = df["tempo_execucao"].mean()
        mediana = df["tempo_execucao"].median()

        print(f"Média do tempo de execução : {media}")
        print(f"Mediana do tempo de execução : {mediana}")

    except FileNotFoundError:
        print("Erro: Arquivo CSV não encontrado.")
    except Exception as erro:
        print(f"Erro ao ler o arquivo: {erro}")

if __name__ == "__main__":
    main()


   
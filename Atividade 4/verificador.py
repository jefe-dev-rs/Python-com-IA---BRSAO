# Verificador de Números

'''
4 - Criar um código que serve para analisar números digitados pelo usuário, 
classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
'''

# Programa: Analisador de Números Pares e Ímpares

def analisar_numeros():
    qtd = int(input("Quantos números deseja digitar? "))
    
    pares = 0
    impares = 0

    for i in range(qtd):
        numero = int(input(f"Digite o {i+1}º número: "))

        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1

    print("\n=== RESULTADO FINAL ===")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

# Programa principal
analisar_numeros()

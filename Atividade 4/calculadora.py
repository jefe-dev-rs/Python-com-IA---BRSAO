# Calculadora de Operações Básicas

'''
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
'''

# Calculadora Simples em Python

print("=== Calculadora Simples ===")
print("Operações disponíveis: +  -  *  /")

# Solicita os valores e a operação ao usuário
num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Verifica qual operação deve ser realizada
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero não é permitida.")
        exit()
else:
    print("Operação inválida.")
    exit()

# Exibe o resultado
print(f"Resultado: {num1} {operacao} {num2} = {resultado}")

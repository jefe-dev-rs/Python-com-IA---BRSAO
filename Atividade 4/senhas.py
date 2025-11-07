# Verificador de Senhas

'''
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
'''

# Verificador de senha segura

def verificar_senha(senha):
    # Critério A: pelo menos 8 caracteres
    if len(senha) < 8:
        return "Senha inválida: deve ter pelo menos 8 caracteres."

    # Critério B: conter pelo menos um número
    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():  # verifica se é número
            tem_numero = True
            break

    if not tem_numero:
        return "Senha inválida: deve conter pelo menos um número."

    # Se passou em todos os critérios
    return "Senha válida! ✅"

# Programa principal
senha_usuario = input("Digite uma senha: ")
resultado = verificar_senha(senha_usuario)
print(resultado)

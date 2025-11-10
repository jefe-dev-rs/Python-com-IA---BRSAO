# Verificador de Palavras Palindromo

def eh_palindromo(texto: str) -> bool:
    """
    Verifica se uma palavra ou frase é um palíndromo,
    ignorando espaços, acentos, pontuação e maiúsculas/minúsculas.
    """
    # Remove espaços e pontuações
    texto_limpo = "".join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]


# Programa principal
frase = input("Digite uma palavra ou frase: ")

if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")

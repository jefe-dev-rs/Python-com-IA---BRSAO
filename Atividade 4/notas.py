# Soma as notas dos Alunos e faz a média da turma

'''
Criar um código que registre as notas de alunos e calcular a média da turma.
'''

# Registro de notas e cálculo da média da turma

# Programa: Registro de notas e cálculo da média da turma

def registrar_notas():
    alunos = {}  # Dicionário: nome -> nota

    qtd = int(input("Quantos alunos deseja cadastrar? "))

    for i in range(qtd):
        print(f"\nAluno {i+1}:")
        nome = input("Nome do aluno: ")
        nota = float(input("Nota do aluno (0 a 10): "))
        alunos[nome] = nota

    # Calcula a média da turma
    media_turma = sum(alunos.values()) / len(alunos)

    # Mostra o relatório
    print("\n=== RELATÓRIO DE NOTAS ===")
    for nome, nota in alunos.items():
        print(f"Aluno: {nome} — Nota: {nota}")

    print(f"\nMédia da turma: {media_turma:.2f}")

# Programa principal
registrar_notas()
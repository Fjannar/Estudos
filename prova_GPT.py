num_alunos = int(input("Digite o número de alunos: "))
soma_medias = 0
for i in range(1, num_alunos + 1):
    print(f"\nAluno {i}:")
    nome_aluno = input("Nome do aluno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Digite a nota {j+1} do aluno: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    soma_medias += media
    if media >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print("\nInformações do aluno:")
    print("Nome:", nome_aluno)
    print("Notas:", notas)
    print("Média:", media)
    print("Situação:", situacao)
media_geral = soma_medias / num_alunos
print("\nMédia geral da turma:", media_geral)

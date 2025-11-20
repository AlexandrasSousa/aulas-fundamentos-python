turma = []
qtd_alunos = 1
aluno = dict() # ou {}

for c in range(qtd_alunos):
    aluno['Nome'] = input(f'Digite o nome do  aluno: ')
    aluno['Média'] = float(input(f'Digite sua média : '))

    if aluno['Média'] > 9.5:
        aluno['Situação'] = 'Aprovado'
    else:
        aluno['Situação'] = 'Reprovado'

    turma.append(aluno.copy())
print(turma)
from random import choice
alunos = list()
for i in range(1, 5):
    aluno = str(input(f'Digite o nome do aluno {i}: '))
    alunos.append(aluno)
print(f'O aluno sorteado foi {choice(alunos)}')

from random import shuffle
alunos = list()
for i in range(1, 5):
    aluno = str(input(f'Digite o nome do aluno {i}: '))
    alunos.append(aluno)
shuffle(alunos)
print(f'O aluno sorteado foi {alunos}')

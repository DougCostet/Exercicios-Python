from time import sleep
n = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    print(f'{n}*{i}= {n*i}')
    sleep(0.2)
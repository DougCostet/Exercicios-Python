nome = str(input('Digite seu nome completo: ')).upper()
print(f'A letra A aparece {nome.count("A")} vezes no nome')
print(f'A primeira letra A apareceu na posição {nome.find("A")+1}')
print(f'A ultima letra A apareceu {nome.rfind("A")+1}')

n1 = int(input('Digite um Número: '))
num = str(n1)
print(f'Analisando o numero {n1}')
if len(num) >= 4:
    print(f'Unidades: {num[3]}')
    print(f'Dezena: {num[2]}')
    print(f'Centena: {num[1]}')
    print(f'Milhar: {num[0]}')
else:
    print(f'Unidade: {num[2]}')
    print(f'Dezena: {num[1]}')
    print(f'Centena: {num[0]}')

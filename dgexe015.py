km = int(input('Quantos KM foram percorridos: '))
dias = int(input('Quantos dias você ficou com o carro: '))
kmrodado = km*0.15
diarias = dias*60
print(f'O valor cobrado pelos KM é R${kmrodado:.2f}')
print(f'O valor a ser pago pelas diárias é R${diarias:.2f}')
print(f'O valor total do aluguel do carro sera R${kmrodado+diarias:.2f}')
from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome', end='')
sleep(0.5); print('.', end=''); sleep(0.5); print('.', end=''); sleep(0.5); print('.', end=''); sleep(0.5)
print(f'Seu nome com todas letras Maiusculas é {nome.upper()}')
print(f'Seu nome com todas letras Minusculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)-nome.count(" ")}')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')

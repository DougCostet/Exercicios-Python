n1 = input('Digite algo: ')
print('É número? ', n1.isnumeric())
print('O tipo primitivo desse valor é? ', type(n1))
print('Contem letras e números? ',  n1.isalnum())
print('Esta em minusculas?', n1.islower())
print('Esta em maiusculas', n1.isupper())
print('É alfabético?', n1.isalpha())
print('Esta capitalizada?', n1.title())
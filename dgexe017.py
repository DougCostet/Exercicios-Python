cat1 = float(input('Digite o valor do Cateto Adjacente: '))
cat2 = float(input('Digite o valor do Cateto Oposto: '))
somacatetos = (cat1**2)+(cat2**2)
hipotenusa = somacatetos**(1/2)
print(f'Em um triangulo com o cateto adjacente no valor de {cat1:.0f} '
      f'e o cateto oposto de {cat2:.0f} a hipotenusa será de {hipotenusa:.2f}.')
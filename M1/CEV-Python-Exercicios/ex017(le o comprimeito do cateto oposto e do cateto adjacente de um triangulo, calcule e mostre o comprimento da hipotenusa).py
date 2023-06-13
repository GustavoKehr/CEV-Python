# Programa que leia o comprimeito do cateto oposto e do cateto adjacente de um triangulo retangulo
# calcule e mostre o comprimento da hipotenusa.

#adjacente é a de baixo oposta é a da vertical, hipotenusa é a


from math import sqrt

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hip = (co**2) + (ca**2)
vh = sqrt(hip)
print('Valor do cateto oposto: {}\nValor do cateto adjacente: {}\nComprimento da Hipotenusa: {:.2f}cm' .format(co, ca, vh))


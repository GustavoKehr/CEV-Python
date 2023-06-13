# Algoritimo que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiusculas
# O nome com todas minusculas
# Quantas letras ao todo sem considerar espacos
# Quantas letras tem o primeiro nome

n = input('Digite seu nome: ').strip()
d = n.split()
print('Seu nome em letra maiuscula: {}\nSeu nome com letra minuscula: {}' .format(n.upper(), n.lower()))
print('Quantas letras tem seu nome completo: ', len(n) - n.count(' '))
print('Quantas letras tem o primeiro nome: ', len(d[0]))

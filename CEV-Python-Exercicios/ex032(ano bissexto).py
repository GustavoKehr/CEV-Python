# Programa que leia um ano qualquer e mostr se ele é BISSEXTO.

anoDig = int(input('Digite um ano para saber se ele é bissexto ou nao: '))

if anoDig % 100 != 0 and anoDig % 4 == 0 or anoDig % 400 == 0:
    print('ano BISSEXTO')
else:
    print('ano NÃO bissexto!')

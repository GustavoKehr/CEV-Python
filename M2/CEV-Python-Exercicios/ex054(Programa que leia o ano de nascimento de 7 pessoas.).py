# Programa que leia o ano de nascimento de 7 pessoas.
# No final mostre quantas sao ainda nao chegaram em 18 anos e quantas já chegaram
from datetime import date

data = date.today().year
tm = 0
tmenor = 0
for pes in range(1,8):
    nasc = int(input('Digite o ano de nascimento de 7 pessoas :'))
    idade = data - nasc
    if idade >= 21:
        print('Maior')
        tm += 1
    else:
        tmenor += 1
print('Tivemos {} maiores e {} pessoas menores' .format(tm, tmenor))
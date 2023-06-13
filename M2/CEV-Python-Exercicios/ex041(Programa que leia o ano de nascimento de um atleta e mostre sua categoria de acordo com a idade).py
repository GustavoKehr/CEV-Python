# Programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# ata 9 anos: mirim
# ate 14 anos: infantil
# ate 19 anos: junior
# ate 20 anos: senior
# acima de 20 anos: master
from datetime import date
nasc = int(input('Digite seu ano de nascimento para determinar sua categoria: '))
data = date.today().year
idade = data - nasc
print('Idade: {} anos' .format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 20:
    print('Sua categoria é SENIOR')
else:
    print('Sua categoria é MASTER')


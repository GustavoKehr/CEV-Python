# Um programa que le o que o usuario digita e mostra na tela o tipo primitivo
# e todas as informacoes possiveis sobre o que foi digitado


msg = input('Digite algo:')

print('Tipo primitivo: {}' .format(type(msg)))

print('É númerico? {}' .format(msg.isnumeric()))
print('É alphanumérico? {}' .format(msg.isalnum()))
print('É decimal? {}' .format(msg.isdecimal()))
print('Está com letras minusculas? {}' .format(msg.islower()))
print('Está com letras maiusculas? {}' .format(msg.isupper()))
print('Esta com espaços? {}' .format(msg.isspace()))
print('Está captalizada? {}' .format(msg.istitle()))

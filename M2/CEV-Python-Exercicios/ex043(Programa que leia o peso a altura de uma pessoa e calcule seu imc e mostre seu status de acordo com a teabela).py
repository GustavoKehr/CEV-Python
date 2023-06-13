# Programa que leia o peso a altura de uma pessoa e calcule seu imc e mostre seu status de acordo com a teabela:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25 : Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade morbida
print('Para digiar peso/altura utilize o . para separar as casas')
pes = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = pes/(alt * alt)


if imc < 18.5:
    print('Seu IMC é de {:.2f} quer dizer que vc está no estado de ABAIXO DO PESO!' .format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.2f} quer dizer que vc está no estado de PESO IDEAL' .format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.2f} quer dizer que vc está no estado de SOBREPESO!' .format(imc))
elif imc <= 40:
    print('Seu IMC é de {:.2f} quer dizer que vc está no estado de OBESIDADE' .format(imc))
else:
    print('Seu IMC é de {:.2f} quer dizer que vc está no estado de OBESIDADE MORBIDA' .format(imc))

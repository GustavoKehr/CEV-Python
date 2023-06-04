# Programa que pergunte a distancia de uma viagem em km.
# calcule o preco da passagem, cobrando R$0,50 por Km para viagens de até 200km
# e R$0,45 para viagens mais longas.

distanciaKM = float(input('Digite a distancia da viagem em KM: '))
if distanciaKM <= 200:
    passagem = distanciaKM*0.50
    print('O valor da passagem com a distancia da viagem de {}KMs foi de: R${:.2f}' .format(distanciaKM, passagem))
else:
    passagem = distanciaKM*0.45
    print('O valor da passagem com a distancia da viagem de {}KMs foi de: R${:.2f}' .format(distanciaKM, passagem))


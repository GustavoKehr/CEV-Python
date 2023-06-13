# Programa que leia a velocidade de um carro.
# Se ele ultrapssar 80Km, mostre uma mensagem dizendo que foi multado.
# A multa custa R$7 para cada Km acima do limite

vel = int(input('Digite a velocidade do carro: '))
ac = vel - 80
acima = float((vel - 80) * 7)
if vel > 80:
    print('Vc foi multado, cada cada Km acima do limite é R$7,00 vc passou a {}KMs do limite, entao sua multa é de: R${}' .format(ac, acima))
else:
    print('Tudo tranquilo! Tenha uma ótima viagem!')

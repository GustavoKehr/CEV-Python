# Programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao servico militar.
# Se é a hora de se alistar.
# Se já passou do tempo de alistamento
# o programa devera mostrar o tempo que falta ou que passou do prazo
from datetime import date

nasc = int(input('Digite o seu ano de nascimento: '))
data = date.today().year
idadereal = data - nasc
calc = (data - nasc) - 18
print('Ano atual {}' .format(data))

if idadereal < 18:
    print('Voce nasceu em {} e tem {} anos sua hora está chegando para se alistar, se prepare! Tempo que falta até que seja obrigatório o alistamento: {} ano(s)' .format(nasc, idadereal, abs(calc)))
elif idadereal == 18:
    print('Voce nasceu em {} e tem {} anos o alistamento é obrigatório! Está na hora de se alistar! ' .format(nasc, idadereal))
else:
    print('Voce nasceu em {} e tem {} anos, voce está {} anos atrasado! corra para regularizar a sua situacao com o nosso pais!' .format(nasc, idadereal, abs(calc)))

    
    # OUTRA FORMA DE SE FAZER
#idade = int(input('Digite sua idade para fazermos a verificacao: '))
#obg = int(idade - 18)

#if idade < 18:
    #print('Sua hora está chegando para se alistar, se prepare! Tempo que falta até que seja obrigatório o alistamento: {} anos' .format(abs(obg)))
#elif idade == 18:
    #print('Está na hora de se alistar! vc está com {} ano(s) e agora é obrigatório!' .format(idade))
#else:
    #print('Já passou da hora de se alistar! voce está {} anos atrasado, corra para regularizar sua situação com o nosso pais!' .format(abs(obg)))





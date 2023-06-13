# Programa que leia duas notas de um aluno e calculke sua media, mostrando uma mensagem no final
# de acordo com a media atingida
# media < 5: reprovado
# media >=5 && 6.9: recuperacao
# media >= 7: aprovado

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2)/2

if media < 5:
    print('Sua média foi de: {} vc está reprovado!' .format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi de: {} vc está de recuperação' .format(media))
else:
    print('Sua média foi de: {} vc está aprovado! meus parabéns!' .format(media))

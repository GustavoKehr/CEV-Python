
soma = qtValores = media = maior = menor = 0

resp = 'S'
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    qtValores += 1
    if qtValores == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N]').upper().strip()[0])
media = soma/qtValores
print('Digitou {} '
      'números e a média é {:.2f}, o maior número foi {} e o menor {}' .format(qtValores, media, maior, menor))



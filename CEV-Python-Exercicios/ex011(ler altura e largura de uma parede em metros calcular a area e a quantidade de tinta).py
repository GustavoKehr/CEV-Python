# programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta, pinta uma area de 2m**2

al = float(input('Digite a altura da sua parede: '))
la = float(input('Digite a largura da sua parede: '))
mq = al * la
lt = mq/2

print('Com a altura de {}m e a largura de {}m, a metragem quadrada da parede é {:.2f}m².' .format(al, la, mq, end=''))
print('A quantidade de tinta necessária para pinta-la é de {:.2f}L' .format(lt))



num = 0
c = 0
soma = 0
num = int(input('Digite um número [999 para parar]'))

while num != 999:
    soma += num
    c += 1
    num = int(input('Digite um número [999 para parar]'))
print('STOPED')
print('You typed {} numbers and the total is {}' .format(c, soma))

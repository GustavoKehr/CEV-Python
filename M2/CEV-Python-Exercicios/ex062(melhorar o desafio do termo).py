primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
maximo = 10
c = 1
total = 0
adicionar = 10
while adicionar != 0:
    total += adicionar
    while c <= total:
        print('{} -> ' .format(primeiroTermo), end='')
        primeiroTermo += razao
        c += 1
    print('PAUSA')
    adicionar = int(input('Quantos termos deseja adicionar? '))
print('Progressao finalizada com {} termos mostrados' .format(total))

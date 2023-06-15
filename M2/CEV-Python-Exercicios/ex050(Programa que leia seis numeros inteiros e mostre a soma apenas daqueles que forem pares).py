# Programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares
# Se o valor digitado for impar, desconsidere-o
s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite o {} valor: ') .format(c))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma dos numeros digitados {} e forem pares é de: {}' .format(cont, s))



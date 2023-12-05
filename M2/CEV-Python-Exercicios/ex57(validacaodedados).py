## Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F"
## caso esteja errado, [eça a digitação novamente ate ter um valor correto.

sex = str(input('Digite o seu sexo [M ou F]')).strip().upper()[0]
while sex not in 'MF':
    sex = str(input('Valor incorreto, digite novamente com os caracteres M ou F para o seu respectivo sexo:\n')).strip().upper()[
        0]
print('Sexo {} registrado com sucesso'.format(sex))

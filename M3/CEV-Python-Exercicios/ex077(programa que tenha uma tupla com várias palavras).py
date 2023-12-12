# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

nomes = ('Gustavo', 'Lucas', 'Lionel', 'Pedri', 'Gavi', 'Lewandowski', 'Vinicius', 'Rodrygo', 'Ter Stegen')

for nome in nomes:
    print(f'\nNo nome {nome:-<12} temos as vogais -> ', end='')
    for letra in nome:
        if letra.lower() in 'aeiou':
            print(f'{letra:>2}', end='')

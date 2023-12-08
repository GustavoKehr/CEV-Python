# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Mundial de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Milan.

mundialDeClubes = ('Barcelona', 'Corinthians', 'Sao Paulo', 'Real Madrid', 'Milan', 'Inter de Milao',
                   'Manchester City', 'Manchester United', 'Liverpool', 'Chealsea', 'Athletico Paranaense', 'Arsenal',
                   'Tottenham', 'Aston Villa', 'Newcastle', 'Girona', 'Atletico de Madrid', 'Bayern de Munich',
                   'Borussia Dortmund', 'Napoli')

# for pos, times in enumerate(mundialDeClubes[4]):
#     print(f'O Mlian está na posicao {pos}')
print(f'Os 5 primeiros times sao: {mundialDeClubes[0:5]}\nOs quatro ultimos colocados sao: {mundialDeClubes[-4:]}')
# print(f'Times em ordem alfabética: {sorted(mundialDeClubes)}')
pos = enumerate(mundialDeClubes)
print(f'O Milan está em -> {mundialDeClubes.index("Milan")}° lugar')





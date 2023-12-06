# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
# ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

totalGasto = produtoMil = itemCadastrados = 0
produtoMaisBarato = 9999999999999
nomeProdutoBarato = ''

while True:
    nomeProduto = str(input('Digite o nome do produto a ser cadastrado: '))
    precoProduto = float(input('Digite o preço do produto a ser cadastrado: '))
    totalGasto += precoProduto
    if precoProduto > 1000:
        produtoMil += 1
    itemCadastrados += 1
    if precoProduto < produtoMaisBarato:
        produtoMaisBarato = precoProduto
        nomeProdutoBarato = nomeProduto
    continuar = str(input('Deseja continuar? [S/N]').strip()[0].upper())
    while continuar not in 'S':
        print('=-'*40)
        print(f'{itemCadastrados} Itens cadastrados\nO total gasto foi {totalGasto:.2f}\n{produtoMil} '
              f'produtos acima de R$1000')
        print(f'{nomeProdutoBarato} Foi o produto mais barato cadastrado R$ {produtoMaisBarato:.2f}')
        print('=-' * 40)
        break




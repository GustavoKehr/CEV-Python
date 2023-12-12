# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Computador', 7500, 'Monitor', 1650, 'Teclado', 350, 'Mouse', 250, 'MousePad', 100, 'Controle', 350,
            'Headset', 375)

listaProdutos = zip(produtos[0::2], produtos[1::2])

for produto, preco in listaProdutos:
    print(f'{produto:-<30} R$ {preco:>3}')




# lanche = ['Hamburguer', 'Suco', 'Pizza',  'Pudim']
# print(lanche)
# lanche[3] = 'Picole'
# print(lanche)
# lanche.append('HotDog')
# print(lanche)
# lanche.insert(0, 'Sushi')
# print(lanche)
# lanche.pop(3)  # ou del lanche[3] ou lanche.remove('Pizza') | del e pop indica o indice, o remove indica o
# # valor(conteudo) | lanche.pop() sem parametro elimina o ultimo indice da lista
# print(lanche)
# # ----------- #
# # Criar lista com range
# valores = list(range(4, 11))
# print(valores)
# valoresAlternados = [8,2,5,4,9,3,0]
# valoresAlternados.sort() # se eu ordenar decrescente = valoresAlternados.sort(reverse = True)
# print(valoresAlternados)
# print(len(valores))
# if 5 in valores:
#     valores.remove(5)
# else:
#     print('Valor 5 nao encontrado!')
# print(valores)
# valores = []
# valores.append(9)
# valores.append(5)
# valores.append(4)
#
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
#
# for c, v in enumerate(valores):
#     print(f'posicao {c} valor {v}')

# a = [2, 3, 4, 7]
# b = a
# print(a)
# print(b)
# print('-'*15)
# # Assim é criado uma ligacao entre as listas
# a = [2, 3, 4, 7]
# b = a
# b[2] = 8
# print(a)
# print(b)
# print('-'*15)
# # Assim é criado uma copia da lista
# a = [2, 3, 4, 7]
# b = a[:]
# b[2] = 8
# print(a)
# print(b)


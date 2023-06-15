# Programa que leia uma frase qualquer e digas se ela é palindromo, desconsiderando os espacos

f = input('Digite uma frase para sabermos se ela é palindromo ou n: ').strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j) - 1, -1, -1):
    i += j[l]
print(j, i)
if i == j:
    print('Palindromo')
else:
    print('N é palindromo')

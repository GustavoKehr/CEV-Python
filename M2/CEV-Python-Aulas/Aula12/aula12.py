nome = input("Digite seu nome: ")
if nome == 'Gustavo':
    print('Bomdia {}' .format(nome))
elif nome == 'Pedro' or nome == 'Cintia' or nome == 'Jessica' or nome == 'Gabriela':
    print('Nome bem popular em {}' .format(nome))
else:
    print('Nao tenha um bom dia {}' .format(nome))

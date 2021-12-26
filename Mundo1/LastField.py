import random

print('Vamos Iniciar o Game!\n')

def menu_person():
    nome = input('Defina seu Nome: ')
    tipo = input('Tipo: ')
    classe = input('Classe: ')
    arma = input('Arma: ')
    print()
def introducao_Game():
    print('Bem-Vindo(a) a Cidade de LastField\nAqui você encontra de tudo uma das maiores cidades de comercio do Continente\n')

menu_person()

iniciar = input('Você está pronto? (S/N)\n')

if iniciar == 'N' or iniciar == 'n':
    menu_person()

elif iniciar == 'S' or iniciar == 's':
    introducao_Game()

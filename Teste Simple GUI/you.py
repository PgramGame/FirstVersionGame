import PySimpleGUI as sg

class TelaPython:
    def __init__(self):

        layout = [
            [sg.T('Nome'), sg.I(key='nome')],
            [sg.T('Idade'), sg.I(key='idade')],
            [sg.T('Quais provedores')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Email', key='email'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.B('Enviar Dados')],
            [sg.Output(size=(50,25))]
        ]
        
        self.janela = sg.Window('Dados do Usuário').layout(layout)

        self.button, self.values = self.janela.Read()
    
    def Iniciar(self):
        while True:

            self.button, self.values = self.janela.Read()

            nome = self.values['nome']
            idade = self.values['idade']
            gmail = self.values['gmail']
            email = self.values['email']
            yahoo = self.values['yahoo']
            print(nome, idade, gmail, email, yahoo)
        


# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('Não')]
        ]
    
    def Iniciar(self):
        # criar uma janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agrecemos a sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')
    
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
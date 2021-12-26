import PySimpleGUI as sg

class TelaPython:
    def __init__(self):

        _00_goha = r'.\Imagens PGRam\Card Person\0_Goha.png'
        self.Numero_0 = {'Id': 0, 'Nome': 'Goha', 'Classe': 'Guerreiro',  'Vida': 500,
                        'Ataque': 500, 'Defesa': 600, 'Força': 150, 'Magia': 0, 'Regeneracao': 20}

        info_label_jog = [
                [sg.Output(echo_stdout_stderr=True,background_color='#363636', text_color='white', size=(33, 15))]
            ]

        frame_vida = [[sg.Text((f'Vida: {self.Numero_0["Vida"]}'), size=(13, 0))], ]
        frame_seu = [[sg.Frame('', frame_vida)]]


        layout = [
            [sg.Fr('', frame_seu), sg.Fr('', info_label_jog)],
            [sg.B('button')]
        ]
        
        self.janela = sg.Window('Dados do Usuário').layout(layout)

    
    def Iniciar(self):

        _00_goha = r'.\Imagens PGRam\Card Person\0_Goha.png'
        self.Numero_0 = {'Id': 0, 'Nome': 'Goha', 'Classe': 'Guerreiro',  'Vida': 500,
                        'Ataque': 500, 'Defesa': 600, 'Força': 150, 'Magia': 0, 'Regeneracao': 20}
        while True:
        
            def layout(self):
            

                info_label_jog = [
                        [sg.Output(echo_stdout_stderr=True,background_color='#363636', text_color='white', size=(33, 15))]
                    ]

                frame_vida = [[sg.Text((f'Vida: {self.Numero_0["Vida"]}'), size=(13, 0))], ]
                frame_seu = [[sg.Frame('', frame_vida)]]


                layout = [
                    [sg.Fr('', frame_seu), sg.Fr('', info_label_jog)],
                    [sg.B('button')]
                ]
            
            layout(self)
            self.janela = sg.Window('Dados do Usuário').layout(layout)

            self.button, self.values = self.janela.Read()

            if self.button == sg.WINDOW_CLOSED:
                exit()

            if self.button == 'button':
                print('a')
                self.Numero_0["Vida"] = self.Numero_0["Vida"] - 100
        



def funciona():

    _00_goha = r'.\Imagens PGRam\Card Person\0_Goha.png'
    Numero_0 = {'Id': 0, 'Nome': 'Goha', 'Classe': 'Guerreiro',  'Vida': 500,
                    'Ataque': 500, 'Defesa': 600, 'Força': 150, 'Magia': 0, 'Regeneracao': 20}
    def janelaaa(Numero_0):
        while True:
            

            info_label_jog = [
                    [sg.Output(echo_stdout_stderr=True,background_color='#363636', text_color='white', size=(33, 15))]
                ]

            frame_vida = [
                [sg.Text((f'Vida: {Numero_0["Vida"]}'), size=(13, 0))]
                ]

            frame_seu = [
                [sg.Frame('', frame_vida)]
                ]

            barra_time = [
                    [sg.Text('Especial da Arma')],
                    [sg.ProgressBar(1000, orientation='h', size=(11.5, 10), key='progressbar')],
                    
                ]

            layout = [
                [sg.Fr('', frame_seu), sg.Fr('', info_label_jog)],
                [sg.B('button'), sg.B('esp_arm')],
                [sg.Fr('', barra_time)]
            ]
            

            
            janela = sg.Window('Dados do Usuário').layout(layout)
            atkPes_bar = janela['progressbar']


            button, values = janela.Read()

            if button == sg.WINDOW_CLOSED:
                exit()
            
            if Numero_0["Vida"] < 0:
                Numero_0["Vida"] = 0
                

            else:

                if button == 'button' and Numero_0["Vida"] > 0:
                    print('a')
                    Numero_0["Vida"] = Numero_0["Vida"] - 100

                if button == 'esp_arm' and Numero_0["Vida"] > 0:
            
                        print('Especial foi usado')
                        for i in range(1000):

                            button, values = janela.Read(timeout=10)
                            if button == sg.WINDOW_CLOSED:
                                exit()
                            
                            atkPes_bar.UpdateBar(i + 1)
                            
                            if i == 999:
                                break
                            #janelaaa(Numero_0)

    janelaaa(Numero_0)


funciona()
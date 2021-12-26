import PySimpleGUI as sg
from random import randint

sg.SetOptions(background_color='#363636',
              text_element_background_color='#363636',
              element_background_color='#363636',
              scrollbar_color=None,
              input_elements_background_color='#F7F3EC',
              button_color=('white', '#4F4F4F'))


class battle():

    def tela(self):

        layout_Colum_C = [
            [sg.Text('Battle Game War Monster', justification='center')],
            [sg.Button('Selecionar Heroi', key='_select_', size=(15, 3))],

        ]

        layout = [
            [sg.Column(layout_Colum_C, element_justification='center')]

        ]

        Janela = sg.Window('Tela Inicial', layout,
                           element_justification='center', size=(250, 150))

        events, values = Janela.Read()

        if events == sg.WINDOW_CLOSED:
            exit()

        if events == '_select_':
            Janela.close()
            Inicier.personagens()
    

    def personagens(self):

        # BLOCO 00 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

        _00_goha = r'.\Imagens PGRam\Card Person\0_Goha.png'
        Numero_0 = {'Id': 0, 'Nome': 'Goha', 'Classe': 'Guerreiro',  'Vida': 3100,
                    'Ataque': 1700, 'Defesa': 600, 'Força': 150, 'Magia': 0, 'Regeneracao': 20}
        button_block = [
            [sg.Button('Goha', size=(15, 0), key='_bgoha_')],
        ]
        block_0 = [
            [sg.Image(_00_goha)],
            [sg.Text((Numero_0['Classe']))],
            [sg.Frame('', button_block)],
        ]

        # BLOCO 01 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

        _01_JanPier = r'.\Imagens PGRam\Card Person\1_JanPier.png'
        Numero_1 = {'Id': 1, 'Nome': 'Jan Pier', 'Classe': 'Mago', 'Vida': 2900,
                    'Ataque': 1340, 'Defesa': 920, 'Força': 0, 'Magia': 1340, 'Regeneracao': 38}
        button_block = [
            [sg.Button('Jan Pier', size=(15, 0), key='_bJanPier_')],
        ]
        block_01 = [
            [sg.Image(_01_JanPier)],
            [sg.Text((Numero_1['Classe']))],
            [sg.Frame('', button_block)],
        ]

        # BLOCO 02 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

        _02_AlphaJoel = r'.\Imagens PGRam\Card Person\2_AlphaJoel.png'
        Numero_2 = {'Id': 2, 'Nome': 'Alpha Joel', 'Classe': 'Guerreiro', 'Vida': 3000,
                    'Ataque': 1200, 'Defesa': 750, 'Força': 1200, 'Magia': 0, 'Regeneracao': 55}
        button_block = [
            [sg.Button('Alpha Joel', size=(15, 0), key='_balphaJoel_')],
        ]
        block_02 = [
            [sg.Image(_02_AlphaJoel)],
            [sg.Text((Numero_2['Classe']))],
            [sg.Frame('', button_block)],
        ]

        # BLOCO 03 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

        _208008_Amigato = r'.\Imagens PGRam\Card Person\208008_Amigato.png'
        Numero_3 = {'Id': 208008, 'Nome': 'Amigato', 'Classe': 'Guerreiro', 'Vida': 3500,
                    'Ataque': 1750, 'Defesa': 2000, 'Força': 750, 'Magia': 0, 'Regeneracao': 35}

        button_block = [
            [sg.Button('Amigato', size=(15, 0), key='_bamigato_')],
        ]
        block_3 = [
            [sg.Image(_208008_Amigato)],
            [sg.Text((Numero_3['Classe']))],
            [sg.Frame('', button_block)],
        ]

        # BLOCO 04 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

        _04_Barnabas = r'.\Imagens PGRam\Card Person\4_Barnabas.png'
        Numero_4 = {'Id': 4, 'Nome': 'Barnabas', 'Classe':  'Guerreiro', 'Vida': 3250, 'Ataque': 1450, 'Defesa': 950,
                    'Força': 1075, 'Magia': 0, 'Regeneracao': 40}
        button_block = [
            [sg.Button('Barnabas', size=(15, 0), key='_bbarnabas_')],
        ]
        block_4 = [
            [sg.Image(_04_Barnabas)],
            [sg.Text((Numero_4['Classe']))],
            [sg.Frame('', button_block)],
        ]
        # BLOCO 05 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

        _05_Evolvingeye = r'.\Imagens PGRam\Card Person\5_Evolvingeye.png'
        Numero_5 = {'Id': 5, 'Nome': 'Evolvingeye', 'Classe': 'Bolseiro', 'Vida': 2800,
                    'Ataque': 1300, 'Defesa': 950, 'Força': 1300, 'Magia': 1400, 'Regeneracao': 40}
        button_block = [
            [sg.Button('Evolvingeye', size=(15, 0), key='_bevolvingeye_')],
        ]
        block_5 = [
            [sg.Image(_05_Evolvingeye)],
            [sg.Text((Numero_5['Classe']))],
            [sg.Frame('', button_block)],
        ]

        layout = [
            [sg.Frame('', block_0), sg.Frame(
                '', block_01), sg.Frame('', block_5)],
            [sg.Frame('', block_02), sg.Frame(
                '', block_3), sg.Frame('', block_4)]
        ]

        Janela = sg.Window('Tela Seleção', layout)

        events, values = Janela.Read()

        if events == sg.WINDOW_CLOSED:
            exit()

        lista = []
        lista2 = []

        if True:
            if events == '_bgoha_':
                img_esc = _00_goha
                hero_esc = Numero_0
                lista.append(img_esc)
                lista.append(hero_esc)

            if events == '_bbarnabas_':
                img_esc = _04_Barnabas
                hero_esc = Numero_4
                lista.append(img_esc)
                lista.append(hero_esc)

            if events == '_bamigato_':
                hero_esc = Numero_3
                img_esc = _208008_Amigato
                lista.append(img_esc)
                lista.append(hero_esc)

            if events == '_balphaJoel_':
                hero_esc = Numero_2
                img_esc = _02_AlphaJoel
                lista.append(img_esc)
                lista.append(hero_esc)

            if events == '_bJanPier_':
                hero_esc = Numero_1
                img_esc = _01_JanPier
                lista.append(img_esc)
                lista.append(hero_esc)

            if events == '_bevolvingeye_':
                img_esc = _05_Evolvingeye
                hero_esc = Numero_5
                lista.append(img_esc)
                lista.append(hero_esc)

        VA = hero_esc['Id']

        ram = randint(0, 5)

        if VA == ram:
            ram = randint(VA, 5)

        if True:
            if ram == 0:
                img_esc = _00_goha
                hero_esc = Numero_0
                lista2.append(img_esc)
                lista2.append(hero_esc)

            if ram == 1:
                hero_esc = Numero_1
                img_esc = _01_JanPier
                lista2.append(img_esc)
                lista2.append(hero_esc)

            if ram == 2:
                hero_esc = Numero_2
                img_esc = _02_AlphaJoel
                lista2.append(img_esc)
                lista2.append(hero_esc)

            if ram == 3:
                hero_esc = Numero_3
                img_esc = _208008_Amigato
                lista2.append(img_esc)
                lista2.append(hero_esc)

            if ram == 4:
                img_esc = _04_Barnabas
                hero_esc = Numero_4
                lista2.append(img_esc)
                lista2.append(hero_esc)

            if ram == 5:
                img_esc = _05_Evolvingeye
                hero_esc = Numero_5
                lista2.append(img_esc)
                lista2.append(hero_esc)

        Janela.Close()
        Inicier.zonabattle(lista, lista2)

    def zonabattle(self, lista, lista2):

        img_battle = r'.\Imagens PGRam\batalhaimg.png'

        hero_esc = lista[1]
        img_esc = lista[0]

        img_esc_ini = lista2[0]
        hero_esc_ini = lista2[1]

        while True:
            # ==============================INIMIGO===================================================

            frame_name = [
                [sg.Text((f'Nome: {hero_esc_ini["Nome"]}'), size=(13, 0))], ]
            frame_class = [
                [sg.Text((f'Classe: {hero_esc_ini["Classe"]}'), size=(13, 0))], ]
            frame_vida = [
                [sg.Text((f'Vida: {hero_esc_ini["Vida"]}'), size=(13, 0))], ]
            frame_ataque = [
                [sg.Text((f'Ataque: {hero_esc_ini["Ataque"]}'), size=(13, 0))], ]
            frame_defesa = [
                [sg.Text((f'Defesa: {hero_esc_ini["Defesa"]}'), size=(13, 0))], ]
            frame_forca = [
                [sg.Text((f'Força: {hero_esc_ini["Força"]}'), size=(13, 0))], ]
            frame_magia = [
                [sg.Text((f'Magia: {hero_esc_ini["Magia"]}'), size=(13, 0))], ]
            frame_regeneracao = [
                [sg.Text((f'Regeneração: {hero_esc_ini["Regeneracao"]}'), size=(13, 0))], ]
            frame_img_inimigo = [[sg.Image(img_esc_ini)], ]

            frame_inimigo = [
                [sg.Text(f'Dados do {hero_esc_ini["Nome"]}')],
                [sg.T()],
                [sg.Frame('', frame_name), sg.Frame('', frame_class)],
                [sg.Frame('', frame_vida), sg.Frame('', frame_defesa)],
                [sg.Frame('', frame_ataque), sg.Frame('', frame_magia)],
            ]

            frame_name = [
                [sg.Text((f'Nome: {hero_esc["Nome"]}'), size=(13, 0))], ]
            frame_class = [
                [sg.Text((f'Classe: {hero_esc["Classe"]}'), size=(13, 0))], ]
            frame_vida = [
                [sg.Text((f'Vida: {hero_esc["Vida"]}'), size=(13, 0))], ]
            frame_ataque = [
                [sg.Text((f'Ataque: {hero_esc["Ataque"]}'), size=(13, 0))], ]
            frame_defesa = [
                [sg.Text((f'Defesa: {hero_esc["Defesa"]}'), size=(13, 0))], ]
            frame_forca = [
                [sg.Text((f'Força: {hero_esc["Força"]}'), size=(13, 0))], ]
            frame_magia = [
                [sg.Text((f'Magia: {hero_esc["Magia"]}'), size=(13, 0))], ]
            frame_regeneracao = [
                [sg.Text((f'Regeneração: {hero_esc["Regeneracao"]}'), size=(13, 0))], ]
            frame_img_jogador = [[sg.Image(img_esc)], ]

            frame_jogador = [
                [sg.Text(f'Dados do {hero_esc["Nome"]}')],
                [sg.T()],
                [sg.Frame('', frame_name), sg.Frame('', frame_class)],
                [sg.Frame('', frame_vida), sg.Frame('', frame_defesa)],
                [sg.Frame('', frame_ataque), sg.Frame('', frame_magia)],
            ]
            # ==========================Informações==============================

            info_label_jog = [
                [sg.Output(background_color='#363636',
                           text_color='white', size=(33, 15))]
            ]

            barra_time = [
                [sg.Text('Especial da Arma')],
                [sg.ProgressBar(1000, orientation='h', size=(
                    11.5, 10), key='progressbar')],
                [sg.Text('Ataque Pesado')],
                [sg.ProgressBar(1000, orientation='h', size=(
                    11.5, 10), key='progressbar2')],
            ]

            # ===========================Botões==================================

            but_battle = [
                [sg.Button('Ataque', key='atk', size=(25, 0))],
                [sg.Button('Defesa', key='def', size=(18, 0)), sg.Button('Evaziva', key='evaziva', size=(
                    18, 0))]
            ]

            # ===========================Colunas==================================

            frame_columE = [
                [sg.Frame('', frame_jogador, element_justification='center'),
                 sg.Frame('', frame_img_jogador)],
                #[sg.Frame('', barra_time)],

            ]

            frame_columC = [
                [sg.T()],
                [sg.Image(img_battle)],
                [sg.T()],
                [sg.Frame('', but_battle, element_justification='center')],

            ]
            frame_columD = [
                [sg.Frame('', frame_img_inimigo),  sg.Frame(
                    '', frame_inimigo, element_justification='center')],

            ]

            # ===========================Frame Final==================================

            layout_frame = [
                [sg.Col(frame_columE), sg.VSeparator(),
                 sg.Col(frame_columC,
                        element_justification='center'), sg.VSeparator(),
                 sg.Col(frame_columD)]
            ]

            Janela = sg.Window('Tela de Batalha',
                               layout_frame, size=(1475, 500))

            '''atkPes_bar = Janela['progressbar']
            Esp_bar = Janela['progressbar2']'''

            events, values = Janela.Read()

            if events == sg.WINDOW_CLOSED:
                exit()

            def janela_win(self):
    
                img_vito = r'.\Imagens PGRam\vitoria_img.png'

                layout = [
                    [sg.Image(img_vito)],
                    [sg.Button('Nova Batalha'), sg.Button('Sair')],
                ]

                Janela = sg.Window('Você Ganhou', layout, element_justification='center')

                events, values = Janela.Read()

                if events == sg.WINDOW_CLOSED:
                    exit()

            def atk_ini(self):

                select_action = randint(1, 1)

                if select_action == 1:

                    ataque_total = hero_esc_ini["Ataque"]
                    defesa_total = hero_esc["Defesa"]
                    vida = hero_esc["Vida"]

                    print(f'Ataque do Inimigo é: {ataque_total}')

                    ataque = randint(0, ataque_total)
                    print(f'Ele atacou: {ataque}')

                    if ataque > (ataque_total / 2):
                        print('Ataque CRÍTICO do Inimigo')

                    elif ataque < ((ataque_total / 2)/2):
                        print('Ataque Fraco do Inimigo')

                    elif ataque <= (ataque_total / 2):
                        print('Ataque Médio do Inimigo')

                    valor = 0

                    if valor == 0:

                        defesa = randint(0, defesa_total)
                        total_atk = ataque - defesa
                        print(f'Heroi defendeu: {defesa}')

                    else:
                        total_atk = 0

                    # Dano Real do Heroi

                    if total_atk < 0:
                        total_atk = 0
                    print(f'Dano do inimigo foi: {total_atk}')

                    _hit_ = vida - total_atk

                    hero_esc["Vida"] = _hit_
                    print(f"Vida do Heroi: {hero_esc['Vida']}")
                    print('\n')

            def basic_atk(self):

                # =======================ATAQUE==============================

                if hero_esc_ini['Vida'] >= 0:

                    if events == 'atk':
                        print('\n')

                        valor = 0
                        ataque_total = hero_esc["Ataque"]
                        defesa_total_ini = hero_esc_ini["Defesa"]
                        vida = hero_esc_ini["Vida"]

                        print(f'Seu ataque é: {ataque_total}')

                        ataque = randint(0, ataque_total)
                        print(f'Você atacou: {ataque}')

                        if ataque > (ataque_total / 2):
                            print('Ataque CRÍTICO')

                        elif ataque < ((ataque_total / 2)/2):
                            print('Ataque Fraco')

                        elif ataque <= (ataque_total / 2):
                            print('Ataque Médio')

                        # Definidor de Evaziva do Inimigo

                        evaziva = randint(0, 1)

                        if evaziva == 1:
                            print('Evaziva Bem sucedida do Inimigo')
                            valor = 1

                        else:
                            print('Evaziva Mal sucedida do Inimigo')

                        # Defesa vs Ataque do Heroi
                        if valor == 0:
                            defesa_ini = randint(0, defesa_total_ini)
                            total_atk = ataque - defesa_ini
                            print(f'Inimigo defendeu: {defesa_ini}')
                        else:
                            total_atk = 0

                    # Dano Real do Heroi

                        if total_atk < 0:
                            total_atk = 0
                        print(f'Seu Dano foi: {total_atk}')

                        _hit_ = vida - total_atk

                        hero_esc_ini["Vida"] = _hit_
                        print(f"Vida do Inimigo: {hero_esc_ini['Vida']}")

                        print('\n')
                        Janela.Close()
                        
                        if valor == 0:
                            Janela.Close()
                            atk_ini(self)
                            Janela.Close()

                        

                        # ==========================DEFESA================================

                    elif events == 'def':
                        defesa_total = hero_esc["Defesa"]
                        print(f'Sua defesa é: {defesa_total}')

                        defesa = randint(0, defesa_total)
                        print(f'Você defendeu: {defesa}')

                        if defesa > (defesa_total / 2):
                            print('Defesa CRÍTICA')

                        elif defesa < ((defesa_total / 2)/2):
                            print('Defesa Fraca')

                        elif defesa <= (defesa_total / 2):
                            print('Defesa Média')
                        print('\n')
                        Janela.Close()
                        atk_ini(self)

                        # ========================EVAZIVA==========================

                    elif events == 'evaziva':
                        evaziva = randint(0, 1)

                        if evaziva == 1:
                            print('Evaziva Bem sucedida')

                        else:
                            print('Evaziva Mal sucedida')
                            atk_ini(self)
                            Janela.Close()
                        print('\n')

                else:
                    hero_esc_ini['Vida'] = 0
                    print('Inimigo Derrotado')
                    janela_win(self)
                    Janela.Close()

            basic_atk(self)


Inicier = battle()
Inicier.tela()

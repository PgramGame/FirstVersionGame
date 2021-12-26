import PySimpleGUI as sg
from random import randint

sg.SetOptions(background_color='#363636',
              text_element_background_color='#363636',
              element_background_color='#363636',
              scrollbar_color=None,
              input_elements_background_color='#F7F3EC',
              button_color=('white', '#4F4F4F'))


def menu():

    # Layout 1
    text_title = [
        [sg.Text('PGRam', justification='center', text_color='yellow')],
    ]

    Login_tela = [
        [sg.Text('Login', size=(5, 0)), sg.Input(size=(20, 0), key='login', readonly=True)],
        [sg.Text('Senha', size=(5, 0)), sg.Input(
            size=(20, 0), key='senha', password_char='*')],
        [sg.Checkbox('Salvar login', key='save_log')],
        [sg.Button('Entrar'), sg.Button('Fazer Cadastro')]
    ]

    layout_f = [
        [sg.Column(text_title, justification='center')],
        [sg.Column(Login_tela, justification='center')],
    ]

    # Janela
    janela = sg.Window('Tela de Login', layout_f, size=(300, 200))

    events, values = janela.read()

    if events == 'Fazer Cadastro':
        janela.close()
        cadastro()

    if events == ('Entrar'):
        janela.close()
        card_page(000, 'Admin', 'Admin')

    elif events == sg.WINDOW_CLOSED:
        exit()


def dados_page(vida_jogador, vida_inimigo, result_dfs_jogador, result_dfs_inimigo, result_atk_jogador, result_atk_inimigo, ataque_jogador,
               ataque_inimigo, ataque_damage_jogador, ataque_damage_inimigo, defesa_jogador, defesa_inimigo, defesa_damage_jogador, defesa_damage_inimigo,):

    gif_dado_d6 = r'.\Imagens PGRam\dado_png.png'

    img_esc = r'.\Imagens PGRam\dado_png.png'

    img_Batlte = [
        [sg.Image(img_esc)],
    ]

    img_Batlte2 = [
        [sg.Image(img_esc)],
    ]

    info_dados = [

        [sg.Text(f'Vida Total: {vida_jogador}', size=(15, 0)), sg.T(
            f'Vida Atual: {result_atk_jogador}', size=(15, 0))],

        [sg.T(f'Ataque Total: {ataque_jogador}', size=(15, 0)), sg.T(
            f'Defesa Total: {defesa_jogador}', size=(15, 0))],

        [sg.T(f'Ataque Dado: {ataque_damage_jogador}', size=(15, 0)), sg.T(
            f'Defendida: {defesa_damage_jogador}', size=(15, 0))],

        [sg.T(f'ATAQUE: {ataque_damage_jogador}', text_color='Green'), sg.T(
            f'DANO SOFRIDO: {result_dfs_jogador}', text_color='Red')],
    ]

    info_dados2 = [
        [sg.Text(f'Vida Total: {vida_inimigo}', size=(15, 0)), sg.T(
            f'Vida Atual: {result_atk_inimigo}', size=(15, 0))],

        [sg.T(f'Ataque Total: {ataque_inimigo}', size=(15, 0)), sg.T(
            f'Defesa Total: {defesa_inimigo}', size=(15, 0))],

        [sg.T(f'Ataque Dado: {ataque_damage_inimigo}', size=(15, 0)), sg.T(
            f'Defendida: {defesa_damage_inimigo}', size=(15, 0))],

        [sg.T(f'ATAQUE: {ataque_damage_inimigo}', text_color='Green'), sg.T(
            f'DANO SOFRIDO: {result_dfs_inimigo}', text_color='Red')],
    ]

    image_dado = [
        [sg.Image(gif_dado_d6)],
        [sg.Image(gif_dado_d6)],
    ]

    layout = [
        [sg.Text('Area de Dados', text_color='yellow')]
    ]

    button_layout = [
        [sg.T('')],
        [sg.Button('Rodar dados', key='rodar_dados')]
    ]

    layout_info_colum = [
        [sg.Column(img_Batlte), sg.Column(info_dados, size=(255, 225))],

    ]

    layout_info_colum_ant = [
        [sg.Column(img_Batlte2), sg.Column(info_dados2, size=(255, 215))],

    ]

    layout_f = [
        [sg.Column(layout, justification='center', size=(100, 40))],
        [sg.Frame('', image_dado, element_justification='Right', size=(
            100, 100)), sg.Frame('VOCÊ', layout_info_colum, size=(100, 100)), sg.Frame('INIMIGO', layout_info_colum_ant, size=(100, 100))],
        [sg.Column(button_layout, justification='center')],
    ]

    janela = sg.Window('Menu da Batalha', layout_f, size=(1400, 700))

    while True:

        events, values = janela.Read()

        if events == dados_D6:
            D6 = randint(1, 6)

        if events == sg.WINDOW_CLOSED:
            exit()


def card_page(ID, name, sobrenome):

    frame_layout = [
        
        [sg.Image((r'.\Imagens PGRam\foto-perfil-masc.png'), size=(200, 200))],
        [sg.Text(f'Nome: {name}', size=(15, 0))],
        [sg.Text(f'Sobrenome: {sobrenome}', size=(15, 0))],
        [sg.T('',size=(40,25))],
    ]
    layout_e = [
        [sg.Frame(f'Perfil', frame_layout)],
    ]

    frame_layout2 = [
        [sg.T('',size=(40,25))]

    ]
    layout_d = [
        [sg.Frame('Noticias', frame_layout2, )],
    ]

    button_layout = [
        [sg.Image((r'.\gif-livro.gif'))],
        [sg.Button('Abrir Card', size=(15, 0)), sg.Button(
            'Batalha', key='_Dados_', size=(15, 0)), sg.Button('Criar Card', key='_CreatCard_', size=(15, 0))],
    ]


    layout_colun = [
        [sg.Column(layout_e), sg.Column(button_layout, justification='center'), sg.Column(layout_d)],
    ]

    janela = sg.Window('Tela de Card', layout_colun)

    while True:

        events, values = janela.Read()

        if events == sg.WINDOW_CLOSED:
            exit()

        if events == '_CreatCard_':
            sistm_person()
            janela.close()

        if events == '_Dados_':
            sistm_ataque()
            janela.close()


def cadastro():

    ID = randint(1, 999)

    text_title_cad = [
        [sg.Text('PGRam', justification='center', text_color='yellow')],
        [sg.Text()]
    ]

    layout_cadastro = [
        [sg.Text('Nome:', size=(5, 0)), sg.Input(size=(15, 0), key='name'), sg.Text(
            'Sobrenome:', size=(9, 0)), sg.Input(size=(15, 0), key='sobrenome')],
        [sg.Text('Email:', size=(5, 0)), sg.Input(size=(15, 0), key='email'),
         sg.Text('Senha:', size=(9, 0)), sg.Input(size=(15, 0), password_char='*', key='senha')],
        [sg.Text(), sg.HSeparator(), sg.Text()],
        [sg.Text('Data de Nascimento:'), sg.Text(size=(10, 0)), sg.CalendarButton(
            'Definir Data', format='%d/%m/%Y', key='nascimento')],
        [sg.Text('Gênero'), sg.Checkbox('Feminino', key='feminino'), sg.Checkbox(
            'Masculino', key='masculino'), sg.Checkbox('Personalizado', key='personalizado')],
    ]

    button_cadastro = [
        [sg.Button('Cadastre-se', size=(0, 0), )],
    ]

    layout_f = [
        [sg.Column(text_title_cad, justification='center')],
        [sg.Column(layout_cadastro, justification='center')],
        [sg.Text(), sg.HSeparator(), sg.Text()],
        [sg.Column(button_cadastro, justification='center')],
    ]

    janela = sg.Window('Cadastro', layout_f, size=(500, 300))

    while True:
        events, values = janela.Read()

        name = values['name']
        email = values['email']
        senha = values['senha']
        feminino = values['feminino']
        sobrenome = values['sobrenome']
        masculino = values['masculino']
        nascimento = values['nascimento']
        personalizado = values['personalizado']

        print(name, sobrenome, email, nascimento)

        if events == sg.WINDOW_CLOSED:
            exit()

        if events == 'Cadastre-se':
            janela.close()
            card_page(ID, name, sobrenome)


def sistm_person():

    # BLOCO 00 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _00_goha = r'.\Imagens PGRam\Card Person\0_Goha.png'
    Numero_0 = {'Nome': 'Goha', 'Classe': 'Guerreiro',  'Vida': 3100,
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
    Numero_1 = {'Nome': 'Jan Pier', 'Classe': 'Mago', 'Vida': 2900,
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
    Numero_2 = {'Nome': 'Alpha Joel', 'Classe': 'Guerreiro', 'Vida': 3000,
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

    _03_Tiwi = r'.\Imagens PGRam\Card Person\3_Tiwi.png'
    Numero_3 = {'Nome': 'Tiwi', 'Classe': 'Arqueiro', 'Vida': 2900, 'Ataque': 1300, 'Defesa': 900,
                'Força': 900, 'Magia': 200, 'Regeneracao': 30}
    button_block = [
        [sg.Button('Tiwi', size=(15, 0), key='_btiwi_')],
    ]
    block_3 = [
        [sg.Image(_03_Tiwi)],
        [sg.Text((Numero_3['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 04 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _04_Barnabas = r'.\Imagens PGRam\Card Person\4_Barnabas.png'
    Numero_4 = {'Nome': 'Barnabas', 'Classe':  'Guerreiro', 'Vida': 3250, 'Ataque': 1450, 'Defesa': 950,
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
    Numero_5 = {'Nome': 'Evolvingeye', 'Classe': 'Bolseiro', 'Vida': 2800,
                'Ataque': 1300, 'Defesa': 950, 'Força': 1300, 'Magia': 1400, 'Regeneracao': 40}
    button_block = [
        [sg.Button('Evolvingeye', size=(15, 0), key='_bevolvingeye_')],
    ]
    block_5 = [
        [sg.Image(_05_Evolvingeye)],
        [sg.Text((Numero_5['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 06 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _06_Damalto = r'.\Imagens PGRam\Card Person\6_Damalto.png'
    Numero_6 = {'Nome': 'Damalto', 'Classe':  'Tanque', 'Vida': 7000, 'Ataque': 1380, 'Defesa': 950,
                'Força': 1380, 'Magia': 0, 'Regeneracao': 60}
    button_block = [
        [sg.Button('Damalto', size=(15, 0), key='_bdamalto_')],

    ]
    block_6 = [
        [sg.Image(_06_Damalto)],
        [sg.Text((Numero_6['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 07 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _07_Bjornaraa = r'.\Imagens PGRam\Card Person\7_Bjornaraa.png'
    Numero_7 = {'Nome': 'Bjornaraa', 'Classe':  'Guerreiro', 'Vida': 3500, 'Ataque': 1200, 'Defesa': 850,
                'Força': 1200, 'Magia': 0, 'Regeneracao': 30}
    button_block = [
        [sg.Button('Bjornaraa', size=(15, 0), key='_bbjornaraa_')],
    ]
    block_7 = [
        [sg.Image(_07_Bjornaraa)],
        [sg.Text((Numero_7['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 08 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _08_Krisyiu = r'.\Imagens PGRam\Card Person\8_Krisyiu.png'
    Numero_8 = {'Nome': 'Krisyiu', 'Classe':  'Guerreiro', 'Vida': 3550, 'Ataque': 1350, 'Defesa': 800,
                'Força': 1250, 'Magia': 0, 'Regeneracao': 32}
    button_block = [
        [sg.Button('Krisyiu', size=(15, 0), key='_bkrisyiu_')],
    ]
    block_8 = [
        [sg.Image(_08_Krisyiu)],
        [sg.Text((Numero_8['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 09 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _09_Oliver = r'.\Imagens PGRam\Card Person\9_Oliver.png'
    Numero_9 = {'Nome': 'Oliver', 'Classe':  'Ladrão', 'Vida': 2700, 'Ataque': 1100, 'Defesa': 960,
                'Força': 1100, 'Magia': 0, 'Regeneracao': 30}
    button_block = [
        [sg.Button('Oliver', size=(15, 0), key='_boliver_')],
    ]
    block_9 = [
        [sg.Image(_09_Oliver)],
        [sg.Text((Numero_9['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 10 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _10_Peculiar = r'.\Imagens PGRam\Card Person\10_Peculiar.png'
    Numero_10 = {'Nome': 'Peculiar', 'Classe': 'Curandeira', 'Vida': 3250,
                 'Ataque': 1350, 'Defesa': 980, 'Força': 1350, 'Magia': 0, 'Regeneracao': 90}
    button_block = [
        [sg.Button('Peculiar', size=(15, 0), key='_bpeculiar_')],
    ]
    block_10 = [
        [sg.Image(_10_Peculiar)],
        [sg.Text((Numero_10['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 11 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _11_Miguelleon = r'.\Imagens PGRam\Card Person\11_Miguelleon.png'
    Numero_11 = {'Nome': 'Miguelleon', 'Classe':  'Mago', 'Vida': 3000, 'Ataque': 1400, 'Defesa': 1000,
                 'Força': 1250, 'Magia': 1400, 'Regeneracao': 50}
    button_block = [
        [sg.Button('Miguelleon', size=(15, 0), key='_bmiguelleon_')],
    ]
    block_11 = [
        [sg.Image(_11_Miguelleon)],
        [sg.Text((Numero_11['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 12 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _12_Alx = r'.\Imagens PGRam\Card Person\12_Alx.png'
    Numero_12 = {'Nome': 'Alx', 'Classe':  'Guerreiro', 'Vida': 3100, 'Ataque': 1500, 'Defesa': 850,
                 'Força': 1500, 'Magia': 0, 'Regeneracao': 45}
    button_block = [
        [sg.Button('Alx', size=(15, 0), key='_balx_')],
    ]
    block_12 = [
        [sg.Image(_12_Alx)],
        [sg.Text((Numero_12['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 13 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _13_Ayla = r'.\Imagens PGRam\Card Person\13_Ayla.png'
    Numero_13 = {'Nome': 'Ayla', 'Classe': 'Arqueira', 'Vida': 2750,
                 'Ataque': 1350, 'Defesa': 880, 'Força': 1350, 'Magia': 0, 'Regeneracao': 40}

    button_block = [
        [sg.Button('Ayla', size=(15, 0), key='_bayla_')],
    ]
    block_13 = [
        [sg.Image(_13_Ayla)],
        [sg.Text((Numero_13['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 14 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _14_Jmoodaliar = r'.\Imagens PGRam\Card Person\14_Jmoodaliar.png'
    Numero_14 = {'Nome': 'Jmoodaliar', 'Classe': 'Anciao', 'Vida': 2800,
                 'Ataque': 1400, 'Defesa': 960, 'Força': 1400, 'Magia': 0, 'Regeneracao': 60}
    button_block = [
        [sg.Button('Jmoodaliar', size=(15, 0), key='_bjmoodaliar_')],
    ]
    block_14 = [
        [sg.Image(_14_Jmoodaliar)],
        [sg.Text((Numero_14['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 15 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _15_Davide = r'.\Imagens PGRam\Card Person\15_Davide.png'
    Numero_15 = {'Nome': 'Davide', 'Classe': 'Guerreiro', 'Vida': 3550,
                 'Ataque': 1300, 'Defesa': 900, 'Força': 1300, 'Magia': 0, 'Regeneracao': 45}
    button_block = [
        [sg.Button('Davide', size=(15, 0), key='_bdavide_')],
    ]
    block_15 = [
        [sg.Image(_15_Davide)],
        [sg.Text((Numero_15['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 16 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _16_Kinroman = r'.\Imagens PGRam\Card Person\16_Kinroman.png'
    Numero_16 = {'Nome': 'Kinroman', 'Classe': 'Anciao', 'Vida': 2800,
                 'Ataque': 1450, 'Defesa': 920, 'Força': 1450, 'Magia': 0, 'Regeneracao': 64}
    button_block = [
        [sg.Button('Kinroman', size=(15, 0), key='_bkinroman_')],
    ]
    block_16 = [
        [sg.Image(_16_Kinroman)],
        [sg.Text((Numero_16['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 17 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _17_Rex = r'.\Imagens PGRam\Card Person\17_Rex.png'
    Numero_17 = {'Nome': 'Rex', 'Classe': 'Mago', 'Vida': 3100, 'Ataque': 1450,
                 'Defesa': 940, 'Força': 0, 'Magia': 1450, 'Regeneracao': 42}
    button_block = [
        [sg.Button('Rex', size=(15, 0), key='_brex_')],
    ]
    block_17 = [
        [sg.Image(_17_Rex)],
        [sg.Text((Numero_17['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 18 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _18_Sadrak = r'.\Imagens PGRam\Card Person\18_Sadrak.png'
    Numero_18 = {'Nome': 'Sadrak', 'Classe': 'Arqueiro', 'Vida': 2950,
                 'Ataque': 1240, 'Defesa': 955, 'Força': 1240, 'Magia': 0, 'Regeneracao': 43}
    button_block = [
        [sg.Button('Sadrak', size=(15, 0), key='_bsadrak_')],
    ]
    block_18 = [
        [sg.Image(_18_Sadrak)],
        [sg.Text((Numero_18['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 19 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _19_RomPommie = r'.\Imagens PGRam\Card Person\19_RomPommie.png'
    Numero_19 = {'Nome': 'Rom Pommie', 'Classe': 'Mago', 'Vida': 3000,
                 'Ataque': 1400, 'Defesa': 950, 'Força': 0, 'Magia': 1400, 'Regeneracao': 50}
    button_block = [
        [sg.Button('Rom Pommie', size=(15, 0), key='_bRomPommie_')],
    ]
    block_19 = [
        [sg.Image(_19_RomPommie)],
        [sg.Text((Numero_19['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 20 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _20_Bornart = r'.\Imagens PGRam\Card Person\20_Bornart.png'
    Numero_20 = {'Nome': 'Bornart', 'Classe': 'Guerreiro', 'Vida': 3250,
                 'Ataque': 1400, 'Defesa': 800, 'Força': 1400, 'Magia': 0, 'Regeneracao': 60}
    button_block = [
        [sg.Button('Bornart', size=(15, 0), key='_bbornart_')],
    ]
    block_20 = [
        [sg.Image(_20_Bornart)],
        [sg.Text((Numero_20['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 21 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _21_Pressio = r'.\Imagens PGRam\Card Person\21_Pressio.png'
    Numero_21 = {'Nome': 'Pressio', 'Classe': 'Guerreiro', 'Vida': 3000,
                 'Ataque': 1500, 'Defesa': 950, 'Força': 1500, 'Magia': 0, 'Regeneracao': 60}
    button_block = [
        [sg.Button('Pressio', size=(15, 0), key='_bpressio_')],
    ]
    block_21 = [
        [sg.Image(_21_Pressio)],
        [sg.Text((Numero_21['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 22 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _22_Logan = r'.\Imagens PGRam\Card Person\22_Logan.png'
    Numero_22 = {'Nome': 'Logan', 'Classe': 'Tanque', 'Vida': 7287,
                 'Ataque': 1400, 'Defesa': 900, 'Força': 1400, 'Magia': 0, 'Regeneracao': 32}
    button_block = [
        [sg.Button('Logan', size=(15, 0), key='_blogan_')],
    ]
    block_22 = [
        [sg.Image(_22_Logan)],
        [sg.Text((Numero_22['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 23 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _23_BasitRather = r'.\Imagens PGRam\Card Person\23_BasitRather.png'
    Numero_23 = {'Nome': 'Basit Rather', 'Classe': 'Mago', 'Vida': 3200,
                 'Ataque': 1600, 'Defesa': 930, 'Força': 0, 'Magia': 1300, 'Regeneracao': 49}
    button_block = [
        [sg.Button('Basit Rather', size=(15, 0), key='_bbasitRather_')],
    ]
    block_23 = [
        [sg.Image(_23_BasitRather)],
        [sg.Text((Numero_23['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 24 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _24_Field = r'.\Imagens PGRam\Card Person\24_Field.png'
    Numero_24 = {'Nome': 'Field', 'Classe': 'Tanque', 'Vida': 8000,
                 'Ataque': 1100, 'Defesa': 850, 'Força': 1100, 'Magia': 0, 'Regeneracao': 30}
    button_block = [
        [sg.Button('Field', size=(15, 0), key='_bfield_')],
    ]
    block_24 = [
        [sg.Image(_24_Field)],
        [sg.Text((Numero_24['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 25 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _25_Jesper = r'.\Imagens PGRam\Card Person\25_Jesper.png'
    Numero_25 = {'Nome': 'Jesper', 'Classe': 'Guerreiro', 'Vida': 3350,
                 'Ataque': 1410, 'Defesa': 920, 'Força': 1410, 'Magia': 0, 'Regeneracao': 55}
    button_block = [
        [sg.Button('Jesper', size=(15, 0), key='_bjesper_')],
    ]
    block_25 = [
        [sg.Image(_25_Jesper)],
        [sg.Text((Numero_25['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 26 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _26_BillyLord = r'.\Imagens PGRam\Card Person\26_BillyLord.png'
    Numero_26 = {'Nome': 'Billy Lord', 'Classe': 'Anciao', 'Vida': 3100,
                 'Ataque': 1500, 'Defesa': 840, 'Força': 1500, 'Magia': 0, 'Regeneracao': 65}
    button_block = [
        [sg.Button('Billy Lord', size=(15, 0), key='_bbillyLord_')],
    ]
    block_26 = [
        [sg.Image(_26_BillyLord)],
        [sg.Text((Numero_26['Classe']))],
        [sg.Frame('', button_block)],
    ]

    # BLOCO 27 Definidor de IMG é ATRIBUTOS para cada PERSONAGEM

    _27_Fahr = r'.\Imagens PGRam\Card Person\27_Fahr.png'
    Numero_27 = {'Nome': 'Fahr', 'Classe': 'Tanque', 'Vida': 7341,
                 'Ataque': 1250, 'Defesa': 860, 'Força': 1250, 'Magia': 0, 'Regeneracao': 31}
    button_block = [
        [sg.Button('Fahr', size=(15, 0), key='_bfahr_')],
    ]
    block_27 = [
        [sg.Image(_27_Fahr)],
        [sg.Text((Numero_27['Classe']))],
        [sg.Frame('', button_block)],
    ]

# JANELA OPEN 01
    def aba1():
        layout_frames = [

            [sg.Frame('Card', block_0, ), sg.Frame('Card', block_3), sg.Frame('Card', block_4), sg.Frame(
                'Card', block_6)],

            [sg.Frame('Card', block_11), sg.Frame('Card', block_9), sg.Frame('Card', block_12), sg.Frame(
                'Card', block_13)],
        ]

        layout_button = [
            [sg.Button('Proximo', size=(15, 2))]
        ]

        layout_Colunas = [
            [sg.Column(layout_frames)],
            [sg.HSeparator()],
            [sg.Column(layout_button, justification='center')],
        ]

        janela = sg.Window('Criador de Cartas 1/3', layout_Colunas)

        while True:

            events, values = janela.Read()

            # Aréa de SELEÇÃO DE DADOS

            if events == '_bgoha_':
                hero_esc = Numero_0
                img_esc = _00_goha
                info_heros(hero_esc, img_esc)

            elif events == '_btiwi_':
                hero_esc = Numero_3
                img_esc = _03_Tiwi
                info_heros(hero_esc, img_esc)

            elif events == '_bbarnabas_':
                img_esc = _04_Barnabas
                hero_esc = Numero_4
                info_heros(hero_esc, img_esc)

            elif events == '_bdamalto_':
                img_esc = _06_Damalto
                hero_esc = Numero_6
                info_heros(hero_esc, img_esc)

            elif events == '_boliver_':
                img_esc = _09_Oliver
                hero_esc = Numero_9
                info_heros(hero_esc, img_esc)

            elif events == '_balx_':
                img_esc = _12_Alx
                hero_esc = Numero_12
                info_heros(hero_esc, img_esc)

            elif events == '_bayla_':
                img_esc = _13_Ayla
                hero_esc = Numero_13
                info_heros(hero_esc, img_esc)

            elif events == '_bmiguelleon_':
                hero_esc = Numero_11
                img_esc = _11_Miguelleon
                info_heros(hero_esc, img_esc)

            if events == sg.WINDOW_CLOSED:
                exit()

            if events == 'Proximo':
                janela.close()
                aba2()

            # JANELA OPEN 02
    def aba2():

        layout_frames2 = [

            [sg.Frame('Card', block_02), sg.Frame('Card', block_01),
             sg.Frame('Card', block_14), sg.Frame('Card', block_16)],
            [sg.Frame('Card', block_18), sg.Frame('Card', block_22),
             sg.Frame('Card', block_24), sg.Frame('Card', block_27)],
        ]

        layout_button2 = [
            [sg.Button('Anterior', size=(15, 2)),
                sg.Button('Proximo', size=(15, 2))]
        ]

        layout_Colunas2 = [
            [sg.Column(layout_frames2)],
            [sg.HSeparator()],
            [sg.Column(layout_button2, justification='center')],
        ]

        janela2 = sg.Window('Criador de Cartas 2/4', layout_Colunas2)

        while True:

            events, values = janela2.Read()

            if events == 'Proximo':
                janela2.close()
                aba3()

            if events == 'Anterior':
                janela2.close()
                sistm_person()

            if events == sg.WINDOW_CLOSED:
                exit()

            elif events == '_balphaJoel_':
                hero_esc = Numero_2
                img_esc = _02_AlphaJoel
                info_heros(hero_esc, img_esc)

            elif events == '_bJanPier_':
                hero_esc = Numero_1
                img_esc = _01_JanPier
                info_heros(hero_esc, img_esc)

            elif events == '_bjmoodaliar_':
                hero_esc = Numero_14
                img_esc = _14_Jmoodaliar
                info_heros(hero_esc, img_esc)

            elif events == '_bkinroman_':
                hero_esc = Numero_16
                img_esc = _16_Kinroman
                info_heros(hero_esc, img_esc)

            elif events == '_bsadrak_':
                hero_esc = Numero_18
                img_esc = _18_Sadrak
                info_heros(hero_esc, img_esc)

            elif events == '_blogan_':
                hero_esc = Numero_22
                img_esc = _22_Logan
                info_heros(hero_esc, img_esc)

            elif events == '_bfield_':
                hero_esc = Numero_24
                img_esc = _24_Field
                info_heros(hero_esc, img_esc)

            elif events == '_bfahr_':
                hero_esc = Numero_27
                img_esc = _27_Fahr
                info_heros(hero_esc, img_esc)

            # JANELA OPEN 03
    def aba3():

        layout_frames3 = [

            [sg.Frame('Card', block_7), sg.Frame('Card', block_8),
             sg.Frame('Card', block_21), sg.Frame('Card', block_5)],
            [sg.Frame('Card', block_15), sg.Frame('Card', block_19),
             sg.Frame('Card', block_10), sg.Frame('Card', block_20)],
        ]

        layout_button3 = [
            [sg.Button('Anterior', size=(15, 2)),
                sg.Button('Proximo', size=(15, 2))],

        ]

        layout_Colunas3 = [
            [sg.Column(layout_frames3)],
            [sg.HSeparator()],
            [sg.Column(layout_button3, justification='center')],
        ]

        janela3 = sg.Window('Criador de Cartas 3/4', layout_Colunas3)

        while True:

            events, values = janela3.Read()

            if events == 'Proximo':
                janela3.close()
                aba4()

            if events == 'Anterior':
                janela3.close()
                sistm_person()

            if events == sg.WINDOW_CLOSED:
                exit()

            elif events == '_bpressio_':
                img_esc = _21_Pressio
                hero_esc = Numero_21
                info_heros(hero_esc, img_esc)

            elif events == '_bbornart_':
                img_esc = _20_Bornart
                hero_esc = Numero_20
                info_heros(hero_esc, img_esc)

            elif events == '_bRomPommie_':
                img_esc = _19_RomPommie
                hero_esc = Numero_19
                info_heros(hero_esc, img_esc)

            elif events == '_bdavide_':
                img_esc = _15_Davide
                hero_esc = Numero_15
                info_heros(hero_esc, img_esc)

            elif events == '_bpeculiar_':
                img_esc = _10_Peculiar
                hero_esc = Numero_10
                info_heros(hero_esc, img_esc)

            elif events == '_bkrisyiu_':
                img_esc = _08_Krisyiu
                hero_esc = Numero_8
                info_heros(hero_esc, img_esc)

            elif events == '_bbjornaraa_':
                img_esc = _07_Bjornaraa
                hero_esc = Numero_7
                info_heros(hero_esc, img_esc)

            elif events == '_bevolvingeye_':
                img_esc = _05_Evolvingeye
                hero_esc = Numero_5
                info_heros(hero_esc, img_esc)
    def aba4():

        layout_frames4 = [

            [sg.Frame('Card', block_17), sg.Frame('Card', block_23)],
            [sg.Frame('Card', block_25), sg.Frame('Card', block_26)],
        ]

        layout_button4 = [
            [sg.Button('Anterior', size=(15, 2))],

        ]

        layout_Colunas4 = [
            [sg.Column(layout_frames4)],
            [sg.HSeparator()],
            [sg.Column(layout_button4, justification='center')],
        ]

        janela4 = sg.Window('Criador de Cartas 4/4', layout_Colunas4)

        while True:

            events, values = janela4.Read()

            if events == 'Anterior':
                janela4.close()
                sistm_person()

            if events == sg.WINDOW_CLOSED:
                exit()

            elif events == '_bpressio_':
                img_esc = _21_Pressio
                hero_esc = Numero_21
                info_heros(hero_esc, img_esc)

            elif events == '_bbornart_':
                img_esc = _20_Bornart
                hero_esc = Numero_20
                info_heros(hero_esc, img_esc)

            elif events == '_bRomPommie_':
                img_esc = _19_RomPommie
                hero_esc = Numero_19
                info_heros(hero_esc, img_esc)

            elif events == '_bdavide_':
                img_esc = _15_Davide
                hero_esc = Numero_15
                info_heros(hero_esc, img_esc)


    aba1()


def info_heros(hero_esc, img_esc):

    frame_name = [[sg.Text((f'Nome: {hero_esc["Nome"]}'), size=(13, 0))], ]
    frame_class = [
        [sg.Text((f'Classe: {hero_esc["Classe"]}'), size=(13, 0))], ]
    frame_vida = [[sg.Text((f'Vida: {hero_esc["Vida"]}'), size=(13, 0))], ]
    frame_ataque = [
        [sg.Text((f'Ataque: {hero_esc["Ataque"]}'), size=(13, 0))], ]
    frame_defesa = [
        [sg.Text((f'Defesa: {hero_esc["Defesa"]}'), size=(13, 0))], ]
    frame_forca = [[sg.Text((f'Força: {hero_esc["Força"]}'), size=(13, 0))], ]
    frame_magia = [[sg.Text((f'Magia: {hero_esc["Magia"]}'), size=(13, 0))], ]
    frame_regeneracao = [
        [sg.Text((f'Regeneração: {hero_esc["Regeneracao"]}'), size=(13, 0))], ]
    frame_img = [[sg.Image(img_esc)], ]

    frame_geral = [
        [sg.Text(f'Dados do {hero_esc["Nome"]}')],
        [sg.T()],
        [sg.Frame('', frame_name), sg.Frame('', frame_class)],
        [sg.Frame('', frame_vida), sg.Frame('', frame_regeneracao)],
        [sg.Frame('', frame_ataque), sg.Frame('', frame_defesa)],
        [sg.Frame('', frame_forca), sg.Frame('', frame_magia)],
    ]
    layout_frame = [
        [sg.Frame('', frame_img), sg.Frame('', frame_geral,
                                           size=(143, 187), element_justification='center')]
    ]

    janela = sg.Window('Dados do Personagem', layout_frame, size=(500, 500))

    events, values = janela.Read()


#def sistm_ataque():


menu()

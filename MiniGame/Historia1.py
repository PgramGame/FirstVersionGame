import PySimpleGUI as sg
from random import randint

sg.SetOptions(background_color='#363636',
              text_element_background_color='#363636',
              element_background_color='#363636',
              scrollbar_color=None,
              input_elements_background_color='#F7F3EC',
              button_color=('white', '#4F4F4F'))

#class historia1():

def tela():

    entrada_vila = r'.\Imagens PGRam\f6812-img5efd7b34399d36.69655884.png'

    ColumC = [
        [sg.Image(entrada_vila)]

    ]

    ColumE = [
        [sg.T('Olá, seja bem vindo(a) a nossa querida Vila! ')],
    ]

    ColumD = [

    ]

    frame_columC = [
        [sg.Image(entrada_vila)]
        

    ]

    frame_columE = [
        [sg.Fr('Jovem Campones', ColumE)],
        

    ]

    frame_columD = [

    ]

    layout = [
        [sg.Col(frame_columE), sg.Col(frame_columC)]
    ]

    Janela = sg.Window('Fase 01',
                            layout, size=(1475, 500))

    events, values = Janela.Read()

    if events == sg.WINDOW_CLOSED:
        exit()

#Inicier = historia1()
tela()
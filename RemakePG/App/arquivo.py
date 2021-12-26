import PySimpleGUI as sg

layout = [[sg.Text('Informe seu Nome:'), sg.I('')],
          [sg.Text('Informe sua Classe:'), sg.I('')],
          [sg.Text('Informe sua Antencendencia:'), sg.I('')],
          [sg.Text('Informe sua Raça:'), sg.I('')],
          [sg.Text('Informe sua Classe:'), sg.I('')],

                ]

window = sg.Window('Window Title', layout)

while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break


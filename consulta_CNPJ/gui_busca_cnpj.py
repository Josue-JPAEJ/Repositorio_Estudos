import PySimpleGUI as sg


def tela_inicial():
    sg.theme('Dark2')

    cnpj = [
        [sg.Text('Informe um CNPJ   [apenas números]:', font='arial 12', pad=(0, 0))],
        [sg.Input(size=(14, 0), font='arial 12', pad=(0, 0), key='-CNPJ-', enable_events=True)],
    ]

    coluna1 = [
        [sg.Text('RAZAO SOCIAL:', font='arial 12')],
        [sg.Text('FANTASIA:', font='arial 12')],
        [sg.Text('TELEFONE:', font='arial 12')],
        [sg.Text('EMAIL:', font='arial 12')],
        [sg.Text('LOGRADOURO:', font='arial 12')],
        [sg.Text('NUMERO:', font='arial 12')],
        [sg.Text('BAIRRO:', font='arial 12')],
        [sg.Text('MUNICIPIO:', font='arial 12')],
        [sg.Text('CEP:', font='arial 12')],
        [sg.Text('UF:', font='arial 12')],
        [sg.Text('SITUACAO:', font='arial 12')],
        [sg.Text('PORTE:', font='arial 12')],
    ]

    coluna2 = [
        [sg.Input(font='arial 12 bold', key='-RAZAOSOCIAL-', size=(35, 1), disabled=True)],
        [sg.Input(font='arial 12 bold', key='-FANTASIA-', size=(35, 1), disabled=True)],
        [sg.Input(font='arial 12 bold', key='-TELEFONE-', size=(35, 1), disabled=True)],
        [sg.Input(font='arial 12 bold', key='-EMAIL-', size=(35, 1), disabled=True)],
        [sg.Input(font='arial 12 bold', key='-LOGRADOURO-', size=(35, 1), disabled=True)],
        [sg.Input(font='arial 12 bold', key='-NUMERO-', size=(35, 1), disabled=True)],
        [sg.Input(font='arial 12 bold', key='-BAIRRO-', size=(35, 1), disabled=True)],
        [sg.Input(font='arial 12 bold', key='-MUNICIPIO-', size=(35, 1), disabled=True)],
        [sg.Input(font='arial 12 bold', key='-CEP-', size=(35, 1), disabled=True)],
        [sg.Input(font='arial 12 bold', key='-UF-', size=(35, 1), disabled=True)],
        [sg.Input(font='arial 12 bold', key='-SITUACAO-', size=(35, 1), disabled=True)],
        [sg.Input(font='arial 12 bold', key='-PORTE-', size=(35, 1), disabled=True)]
    ]

    coluna3 = [
        [sg.Multiline(no_scrollbar=False, font='arial 12 bold', key='-TEXTBOX-', size=(50, 26), disabled=True)]
    ]

    botoes = [
        [sg.Button('Consultar', font='arial 12', size=(10, 1), pad=((0, 15), 0)),
         sg.CButton('Sair', font='arial 12', size=(8, 1))]
    ]

    progressbar = [
        [sg.ProgressBar(max_value=1000, orientation='h', size=(100, 20), key='-PROG-', visible=False)]
    ]

    layout = [
        [sg.VPush()],
        [sg.Column(cnpj, justification='center', element_justification='center')],
        [sg.Column(coluna1, pad=((0, 20), 0), justification='center', element_justification='left'),
         sg.Column(coluna2, pad=((0, 20), 0), justification='center', element_justification='center'),
         sg.Column(coluna3, pad=((0, 20), 0), justification='center', element_justification='center')],
        [sg.Column(botoes, justification='center')],
        [sg.Column(progressbar, justification='center')],
        [sg.VPush()]
    ]

    telaprin = sg.Window(
        'ConsultaCNPJ',
        element_padding=(0, 10),
        layout=layout,
        finalize=True,
        resizable=True,
        icon='icon_cnpj.ico'
    )

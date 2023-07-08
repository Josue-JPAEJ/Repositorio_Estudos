from gui_busca_cep import *
from consulta_cep import *

tela_inicial()

while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Consultar':
        cep = values['-CEP-']
        try:
            file_json = consulta(cep)
            logradouro = file_json['logradouro']
            bairro = file_json['bairro']
            localidade = file_json['localidade']
            uf = file_json['uf']
            ibge = file_json['ibge']
            ddd = file_json['ddd']

            window['-LOGRADOURO-'].update(logradouro)
            window['-BAIRRO-'].update(bairro)
            window['-LOCALIDADE-'].update(localidade)
            window['-UF-'].update(uf)
            window['-IBGE-'].update(ibge)
            window['-DDD-'].update(ddd)

        except:
            sg.popup('Verifique se o campo "CEP" foi preenchido corretamente\n'
                     'ou se tem conexão com a internet!', font='arial 12', title='Erro')

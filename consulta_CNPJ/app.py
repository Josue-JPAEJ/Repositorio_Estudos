import string
from gui_busca_cnpj import *
from consulta_cnpj import *

tela_inicial()


def preencher_textbox(filejson):
    new_text = ''

    for chave, valor in filejson.items():
        new_text = f'{new_text}\n\n{chave}: '
        if type(valor) is list:
            for item in valor:
                if type(item) is dict:
                    for chave2, valor2 in item.items():
                        new_text = f'{new_text}\n    {chave2}: {valor2}'
        else:
            new_text = f'{new_text}{valor}'

    return new_text.upper()


def carregar_progressbar():
    for i in range(1000):
        window['-PROG-'].update_bar(i + 1)


while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CNPJ-':

        cnpj = values['-CNPJ-']
        cnpj = cnpj.translate(str.maketrans('', '', string.punctuation))
        window['-CNPJ-'].update(cnpj)

        if len(cnpj) > 0:
            try:
                if not float(cnpj).is_integer():
                    sg.popup('Verifique se o campo "CNPJ" foi preenchido corretamente\n'
                             'Necessário conter somente números.', font='arial 12', title='Erro')
                    window['-CNPJ-'].update('')

            except Exception as erro:
                sg.popup(f"Verifique se o campo 'CNPJ' foi preenchido corretamente\n"
                         f"Necessário conter somente números. {erro}", font='arial 12', title='Erro')
                window['-CNPJ-'].update('')

        if len(cnpj) > 14:
            cnpj = cnpj[:14]
            window['-CNPJ-'].update(cnpj)

    if event == 'Consultar':
        cnpj = values['-CNPJ-']
        if len(cnpj) == 14:
            try:

                window['-PROG-'].update(visible=True)

                carregar_progressbar()

                file_json = consulta(cnpj)

                razao_social = file_json['nome']
                fantasia = file_json['fantasia']
                telefone = file_json['telefone']
                email = file_json['email']
                logradouro = file_json['logradouro']
                numero = file_json['numero']
                bairro = file_json['bairro']
                municipio = file_json['municipio']
                cep = file_json['cep']
                uf = file_json['uf']
                situacao = file_json['situacao']
                porte = file_json['porte']

                window['-RAZAOSOCIAL-'].update(razao_social)
                window['-FANTASIA-'].update(fantasia)
                window['-TELEFONE-'].update(telefone)
                window['-EMAIL-'].update(email)
                window['-LOGRADOURO-'].update(logradouro)
                window['-NUMERO-'].update(numero)
                window['-BAIRRO-'].update(bairro)
                window['-MUNICIPIO-'].update(municipio)
                window['-CEP-'].update(cep)
                window['-UF-'].update(uf)
                window['-SITUACAO-'].update(situacao)
                window['-PORTE-'].update(porte)

                window['-TEXTBOX-'].Update(preencher_textbox(file_json))

            except Exception as erro:
                sg.popup('Verifique se o campo "CNPJ" foi preenchido corretamente\n'
                         f'ou se tem conexão com a internet! {erro}', font='arial 12', title='Erro')
            finally:
                window['-PROG-'].update(visible=False)

        else:
            sg.popup('Verifique se o campo "CNPJ" foi preenchido corretamente\n'
                     'Necessário conter 14 números.', font='arial 12', title='Erro')

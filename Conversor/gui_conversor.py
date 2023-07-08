import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-INPUT-'),
        sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key='-UNITS-'),
        sg.Button('Convert', key='-CONVERT-')
    ],
    [sg.Text('Output', key='-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            output_string: str = 'Selecione uma opção válida'
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} km are {output} mile(s).'
                case 'kg to pound':
                    output = round(float(input_value) * 2.30462, 2)
                    output_string = f'{input_value} kg are {output} pound(s).'
                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} second(s) are {output} minute(s).'
            window['-OUTPUT-'].Update(output_string)
        else:
            window['-OUTPUT-'].Update('Please enter a number')

window.close()

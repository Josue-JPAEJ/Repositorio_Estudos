import PySimpleGUI as sg
import csv

headings = ['Name', 'Address', 'Phone Number', 'City']

header = [
    sg.Text('Name', pad=(0, 0), size=(15, 1), justification='c'),
    sg.Text('Address', pad=(0, 0), size=(30, 1), justification='c'),
    sg.Text('Phone Number', pad=(0, 0), size=(30, 1), justification='c'),
    sg.Text('City', pad=(0, 0), size=(15, 1), justification='c'),
]

layout = [
    header
]

for row in range(0, 15):
    current_row = [
        sg.Input(size=(15, 1), pad=(0, 0), key=(row, 0), enable_events=True),
        sg.Input(size=(30, 1), pad=(0, 0), key=(row, 1), enable_events=True),
        sg.Input(size=(30, 1), pad=(0, 0), key=(row, 2), enable_events=True),
        sg.Input(size=(15, 1), pad=(0, 0), key=(row, 3), enable_events=True)
    ]
    layout.append(current_row)

button_row = [sg.Button('Submit'), sg.Button('Generate CSV'), sg.Button('Clear')]
layout.append(button_row)

window = sg.Window('SpreadSheet', layout, font='Courier 12')


def generate_csv(headings, values):
    file = open('spreadssheets.csv', 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)

    writer.writerow(headings)

    for row in range(15):
        current_row = []
        for column in range(4):
            current_row.append(values[row, column])
        writer.writerow(current_row)

    file.close()


def clear_all(window):
    for row in range(15):
        for column in range(4):
            window[(row, column)].update('')

key_object = [(0, 0)]

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Submit':
        print(values[key_object[0]])

    elif event == 'Generate CSV':
        generate_csv(headings, values)
    elif event == 'Clear':
        clear_all(window)
    else:
        key_object = []
        key_object.append(event)

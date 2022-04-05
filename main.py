import PySimpleGUI as sg


layout = [
    [
        sg.Input(key="-INPUT-"),
        sg.Spin(["km to mile", "kg to pound", "sec to min"], key="-UNITS-"),
        sg.Button("Convert", key="-CONVERT-"),
    ],
    [sg.Text("Output", key="-OUTPUT-")],
]

window = sg.Window(title="Converter", layout=layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT-":
        input_value: str = values["-INPUT-"]
        if input_value.isnumeric():
            print(input_value)

window.close()

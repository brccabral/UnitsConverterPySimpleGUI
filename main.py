import PySimpleGUI as sg


layout = [
    [sg.Text("Text"), sg.Spin(["item 1", "item 2"])],
    [sg.Button("Button", key="-BUTTON1-")],
    [sg.Input()],
    [sg.Text("Test"), sg.Button("Button", key="-BUTTON2-")],
]

window = sg.Window(title="Converter", layout=layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-BUTTON1-":
        print("Button pressed")
    elif event == "-BUTTON2-":
        print("Test Button pressed")

window.close()

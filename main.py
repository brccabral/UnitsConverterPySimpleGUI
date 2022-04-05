import PySimpleGUI as sg


layout = [
    [sg.Text("Text", enable_events=True, key="-TEXT1-"), sg.Spin(["item 1", "item 2"])],
    [sg.Button("Button", key="-BUTTON1-")],
    [sg.Input(key="-INPUT-")],
    [sg.Text("Test", key="-TEXT2-"), sg.Button("Button", key="-BUTTON2-")],
]

window = sg.Window(title="Converter", layout=layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-BUTTON1-":
        print(values)
        print(values["-INPUT-"])
        window["-TEXT1-"].update(values["-INPUT-"])
        window["-TEXT2-"].update(visible=False)
    elif event == "-BUTTON2-":
        print("Test Button pressed")
    elif event == "-TEXT-":
        print("text was pressed")

window.close()

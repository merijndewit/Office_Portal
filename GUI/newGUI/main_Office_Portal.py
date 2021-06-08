import PySimpleGUI as gui
import Layouts

staticLayout = [[gui.Column(Layouts.Introduction, key='-PG0-'), gui.Column(Layouts.Dependencies, visible=False, key='-PG1-')],
          [gui.Button('prevPage'),gui.Button('nextPage'), gui.Button('Exit')]]

window = gui.Window('Office Portals', staticLayout, size = (640,480),resizable = False , element_justification = "center")

staticLayout = 0
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'nextPage':
        window[f'-PG{staticLayout}-'].update(visible=False)
        staticLayout = staticLayout + 1 if staticLayout < 1 else 1
        window[f'-PG{staticLayout}-'].update(visible=True)
    elif event == 'prevPage':
        window[f'-PG{staticLayout}-'].update(visible=False)
        staticLayout = staticLayout - 1 if staticLayout > 0 else 0
        window[f'-PG{staticLayout}-'].update(visible=True)
window.close()
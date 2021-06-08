import PySimpleGUI as gui
import Layouts

window = gui.Window('Office Portals', Layouts.Introduction, size = (640,480),resizable = True , element_justification = "center", finalize = True)

while True:
    event, values = window.read()
    print(event, values)
    if event in (gui.WIN_CLOSED, 'Exit'):
        break

window.close()
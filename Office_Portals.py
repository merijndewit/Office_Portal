import PySimpleGUI as gui
import Office_Portals_Start_Streaming as ststream
import Get_PI_Info as getpi

layout = [[gui.Text('Office Portals', font=("Helcentica", 20))],
          [gui.Text('A nerdy solution to make distant colleagues feel nearby', font=("Helcentica", 12), size = (100, 1))],
           [gui.Text('PI`s IP:'),gui.Text(getpi.getip())],
            [gui.Text('Target IP:', font = ("Helcentica", 9)),gui.Input(key = 'targetip', size = (20,1))],
             [gui.Button("Start Streaming")],
         [gui.Exit()]]
window = gui.Window('Office Portals', layout, size = (480,360),resizable = True , element_justification = "center", finalize = True)
#window.Maximize()

while True:
    event, values = window.read()
    print(event, values)
    if event == 'Start Streaming':
        ststream.ip = values['targetip']
        ststream.stream()
    if event in (gui.WIN_CLOSED, 'Exit'):
        ststream.stopstream()
        break


window.close()
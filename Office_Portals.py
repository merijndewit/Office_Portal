import PySimpleGUI as gui
import Office_Portals_Start_Streaming as ststream
import Get_PI_Info as getpi

layout = [[gui.Text('Office Portals', font=("Helcentica", 20))],
          [gui.Text('A nerdy solution to make distant colleagues feel nearby', font=("Helcentica", 12))],
           [gui.Text('PI`s IP:'),gui.Text(getpi.getip())],
            [gui.Text('Target IP:', font = ("Helcentica", 9)),gui.Input(key = 'targetip', size = (20,1))],
             [gui.Text('PI camera CSI/USB'), gui.Checkbox(key = ("picam"), text = 'unchecked = CSI') ],
              [gui.Text('Target PI camera CSI/USB'), gui.Checkbox(key = ("targetpicam"), text = 'unchecked = CSI')],
               [gui.Button("Start Streaming")],
         [gui.Exit()]]
window = gui.Window('Office Portals', layout, size = (640,480),resizable = True , element_justification = "center", finalize = True)
#window.Maximize()

while True:
    event, values = window.read()
    print(event, values)
    if event == 'Start Streaming':
        piCSI = values['picam']
        ststream.ip = values['targetip']
        ststream.stream(piCSI)
    if event in (gui.WIN_CLOSED, 'Exit'):
        ststream.stopstream()
        break


window.close()
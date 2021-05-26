import PySimpleGUI as gui
import Office_Portals_Start_Streaming as ststream
import Office_Portals_Recieve_Stream as rcstream
import Get_PI_Info as getpi

layout = [[gui.Text('Office Portals', font=("Helcentica", 20))],
          [gui.Text('A nerdy solution to make distant colleagues feel nearby', font=("Helcentica", 12))],
           [gui.Text('PI`s IP:'),gui.Text(getpi.getip())],
            [gui.Text('Target IP:', font = ("Helcentica", 9)),gui.Input(key='targetip', size = (20,1))],
             [gui.Text('PI camera CSI/USB'), gui.Checkbox(key = ("picam"), text = 'unchecked = CSI') ],
              [gui.Text('Target PI camera CSI/USB'), gui.Checkbox(key = ("targetpicam"), text = 'unchecked = CSI')],
               [gui.Button("Start Streaming"), gui.Button("Stop Streaming")],
                [gui.Button("Start Recieving Stream"), gui.Button("Stop Revieving Stream")],
         [gui.Exit()]]
window = gui.Window('Office Portals', layout, size = (640,480),resizable = True , element_justification = "center", finalize = True)
# window.Maximize()

while True:
    event, values = window.read()
    print(event, values)
    if event == 'Start Streaming':
        ststream.piCSI = values['picam']
        ststream.ip = values['targetip']
        ststream.stream()
    if event == 'Start Recieving Stream':
        targetpiCSI = values['targetpicam']
        rcstream.recieveStream(targetpiCSI)
    if event == 'Stop Streaming':
        ststream.stopstream()
    if event == 'Stop Revieving Stream':
        rcstream.stopreceivingstream()
    if event in (gui.WIN_CLOSED, 'Exit'):
        ststream.stopstream()
        rcstream.stopreceivingstream()
        break


window.close()
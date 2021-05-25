import PySimpleGUI as gui
import Office_Portals_Start_Streaming as ststream

ststream.ip = "192.168.1.139" #set the target ip

layout = [[gui.Text('Office Portals', font=("Helcentica", 20))],
          [gui.Text('A nerdy solution to make distant colleagues feel nearby', font=("Helcentica", 12), s = (100, 12))],
            [gui.Button("Start Streaming")],
         [gui.Exit()]]
window = gui.Window('Office Portals', layout, size = (480,360),resizable = True , element_justification = "center", finalize = True)
#window.Maximize()

while True:
    event, values = window.read()
    print(event, values)
    if event == 'Start Streaming':
        ststream.stream()
    if event in (gui.WIN_CLOSED, 'Exit'):
        ststream.stopstream()
        break


window.close()
import PySimpleGUI as gui
import Office_Portals_Start_Streaming as ststream

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
        ststream.function( 1, 2)
    if event in (gui.WIN_CLOSED, 'Exit'):
        break
    
    
window.close()
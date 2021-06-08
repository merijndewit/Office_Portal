import PySimpleGUI as gui
import Office_Portals_Start_Streaming as ststream
import Office_Portals_Recieve_Stream as rcstream
import LED as led
import Get_PI_Info as getpi

layout = [[gui.Text('Office Portals', font=("Helcentica", 20))],
          [gui.Text('A nerdy solution to make distant colleagues feel nearby', font=("Helcentica", 12))],
           [gui.Text('PI`s IP:'),gui.Text(getpi.getip())],
            [gui.Text('Target IP:', font = ("Helcentica", 9)),gui.Input(key='targetip', size = (20,1))],
             [gui.Text('Target pixel width:', font = ("Helcentica", 9)),gui.Input(default_text='1920',key='targetwidth', size = (20,1))],
              [gui.Text('Target pixel height:', font = ("Helcentica", 9)),gui.Input(default_text='1080',key='targetheight', size = (20,1))],
               [gui.Text('Target fps:', font = ("Helcentica", 9)),gui.Input(default_text='20',key='targetfps', size = (20,1))],
                [gui.Text('Color'), gui.Checkbox(key = ("ledcolor"), text = 'unchecked = Orange')],
                 [gui.Text('Status:'), gui.Text('',key='Statustext')],
                  [gui.Button("Start Streaming"), gui.Button("Stop Streaming")],
                   [gui.Button("Start Recieving Stream"), gui.Button("Stop Revieving Stream")],
         [gui.Exit()]]
window = gui.Window('Office Portals', layout, size = (640,480),resizable = True , element_justification = "center", finalize = True)
# window.Maximize()

while True:
    event, values = window.read()
    print(event, values)

    if event == 'Start Streaming':
        color = values['ledcolor']
        led.setcolor(color)
        ststream.ip = values['targetip']
        ststream.vidwidth = values['targetwidth']
        ststream.vidheight = values['targetheight']
        ststream.vidfps = values['targetfps']
        ststream.stream()
    if event == 'Start Recieving Stream':
        rcstream.ip = values['targetip']
        rcstream.makespdfile()
    if event == 'Stop Streaming':
        ststream.stopstream()
    if event == 'Stop Revieving Stream':
        rcstream.stopreceivingstream()
    if event in (gui.WIN_CLOSED, 'Exit'):
        ststream.stopstream()
        rcstream.stopreceivingstream()
        break


window.close()
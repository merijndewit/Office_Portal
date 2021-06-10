import PySimpleGUI as gui
import Layouts
import Get_Dependencies as getdp
import Install_Dependencies as getD

gui.theme('Default1')
staticLayout = [[gui.Column(Layouts.Introduction, key='-PG0-'), gui.Column(Layouts.Dependencies, visible=False, key='-PG1-')],
          [gui.Button(key='prevPage', image_filename='Pictures/arrow_left.png', border_width=0), gui.Button(key='Exit', image_filename='Pictures/Exit_Button.png', border_width=0),gui.Button(key='nextPage', image_filename='Pictures/arrow_right.png', border_width=0)]]

window = gui.Window('Office Portals', staticLayout, size = (640,480),resizable = False , element_justification="center")

staticLayout = 0
while True:
    #Main
    event, values = window.read()
    print(event, values)
    #staticLayout
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
    #Introduction

    #Dependencies
    if event == 'checkGstreamer':
        window['Loading1'].update(visible=True)
        window['installGstreamer-tools'].update(visible=False)
        window.refresh()
        if getdp.checkGstreamer() == 0: #the function returns a 1 or a 0. 0 for when gstreamer-tools is not installed and 1 for when it is.
            #gstreamer-tools not installed
            window['installGstreamer-tools'].update(visible=True)
        else:
            #gstreamer-tools is installed
            window['gstreamer-toolsInstalled'].update(visible=True)
        window['Loading1'].update(visible=False)

    if event == 'checkRpicamsrc':
        window['Loading3'].update(visible=True)
        window['installRpicamsrc'].update(visible=False)
        window.refresh()
        if getdp.checkRpicamsrc() == 0: #the function returns a 1 or a 0. 0 for when gstreamer-tools is not installed and 1 for when it is.
            #gstreamer-tools not installed
            window['installRpicamsrc'].update(visible=True)
        else:
            #gstreamer-tools is installed
            window['rpicamsrcInstalled'].update(visible=True)
        window['Loading3'].update(visible=False)

    if event == 'checkGstreamerdev':
        window['Loading2'].update(visible=True)
        window['installGstreamerdev'].update(visible=False)
        window.refresh()
        if getdp.checkGstreamerdev() == 0: #the function returns a 1 or a 0. 0 for when gstreamer-tools is not installed and 1 for when it is.
            #gstreamer-tools not installed
            window['installGstreamerdev'].update(visible=True)
        else:
            #gstreamer-tools is installed
            window['gstreamerdevInstalled'].update(visible=True)
        window['Loading2'].update(visible=False)
    
    if event == 'installGstreamer-tools':
        getD.installGstreamertools()
    elif event == 'installRpicamsrc':
        getD.installRpicamsrc()
    elif event == 'installGstreamerdev':
        getD.installGstreamerdev()


window.close()
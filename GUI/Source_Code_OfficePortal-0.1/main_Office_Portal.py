import PySimpleGUI as gui
import Layouts
import Get_Dependencies as getdp
import Install_Dependencies as getD
import Make_Config_File as config
import Stream as RStream


window = gui.Window('Office Portals', Layouts.staticLayout, size = (640,480),resizable = False , element_justification="center")

staticLayout = 0
while True:
    #######################################################################################
    #Main
    #######################################################################################
    event, values = window.read()
    #staticLayout   
    if event in (None, 'Exit'):
        RStream.stopreceivingstream()
        RStream.stopstream()
        break
    if event == 'nextPage':
        window[f'-PG{staticLayout}-'].update(visible=False)
        window[f'-T{staticLayout}-'].update(visible=False)
        staticLayout = staticLayout + 1 if staticLayout < 5 else 5
        window[f'-PG{staticLayout}-'].update(visible=True)
        window[f'-T{staticLayout}-'].update(visible=True)
    elif event == 'prevPage':
        window[f'-T{staticLayout}-'].update(visible=False)
        window[f'-PG{staticLayout}-'].update(visible=False)
        staticLayout = staticLayout - 1 if staticLayout > 0 else 0
        window[f'-PG{staticLayout}-'].update(visible=True)
        window[f'-T{staticLayout}-'].update(visible=True)

    #######################################################################################
    #Dependencies
    #######################################################################################
    
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
        window['installGstreamer-tools'].update(visible=False)
        window['Loading1'].update(visible=True)
        window.refresh()
        getD.installGstreamertools()
        window['Loading1'].update(visible=False)
    elif event == 'installRpicamsrc':
        window['installRpicamsrc'].update(visible=False)
        window['Loading3'].update(visible=True)
        window.refresh()
        getD.installRpicamsrc()
        window['Loading3'].update(visible=False)
    elif event == 'installGstreamerdev':
        window['installGstreamerdev'].update(visible=False)
        window['Loading2'].update(visible=True)
        window.refresh()
        getD.installGstreamerdev()
        window['Loading2'].update(visible=False)
       
    #######################################################################################
    #receive stream
    #######################################################################################
    if event == 'nextPage' and staticLayout == 5:
        configspecs = ['otherIP', 'targetipWidth', 'targetipHeight','targetFramerate' , 'ledStrip', 'ledTexture', 'noRing', 'autoStart', 'streamBitrate', 'portSender', 'portReceiver']
        config.clearConfigfile()
        for i in range(len(configspecs)):
            varmakeconfig = dict(zip('config.', configspecs[i]))
            varmakeconfig = values[configspecs[i]]
            config.makeConfig(varmakeconfig)
        RStream.stream()
        if RStream.checkstream() == 0:
            window['streaming'].update(visible=True)
            window['notStreaming'].update(visible=False)
        else:
            window['notStreaming'].update(visible=True)
            window['streaming'].update(visible=False
            )
    if event == 'readyStream':
        RStream.makespdfile()
    if event == 'prevPage' and staticLayout == 4:
        RStream.stopreceivingstream()
        RStream.stopstream()
        
        

    

        


window.close()
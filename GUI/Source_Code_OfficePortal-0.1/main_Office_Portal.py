from tkinter.constants import TRUE
import PySimpleGUI as gui
import sys,os
import Layouts
import Get_Dependencies as getdp
import Install_Dependencies as getD
import Make_Config_File as config
import Stream as RStream
import Ring
import LED
import json
import threading

window = gui.Window('Office Portals', Layouts.staticLayout, size = (640,480),resizable = False , element_justification="center")

staticLayout = 0

if getattr(sys, 'frozen', False):
    cd = os.path.dirname(sys.executable)
else:
    cd = os.path.dirname(os.path.abspath(__file__))

def checkGstreamer():
    window['Loading1'].update(visible=True)
    window['installGstreamer-tools'].update(visible=False)
    window['gstreamer-toolsInstalled'].update(visible=False)
    window.refresh()
    if getdp.checkGstreamer == 0: #the function returns a 1 or a 0. 0 for when gstreamer-tools is not installed and 1 for when it is.
        #gstreamer-tools not installed
        window['installGstreamer-tools'].update(visible=True)
    else:
        #gstreamer-tools is installed
        window['gstreamer-toolsInstalled'].update(visible=True)
    window['Loading1'].update(visible=False)
    threading.Thread(target=checkGstreamerdev, args=(), daemon=True).start()


def checkGstreamerdev():
    window['Loading2'].update(visible=True)
    window['installGstreamerdev'].update(visible=False)
    window['gstreamerdevInstalled'].update(visible=False)
    window.refresh()
    if getdp.checkGstreamerdev() == 0: #the function returns a 1 or a 0. 0 for when gstreamer-tools is not installed and 1 for when it is.
        #gstreamer-tools not installed
        window['installGstreamerdev'].update(visible=True)
    else:
        #gstreamer-tools is installed
        window['gstreamerdevInstalled'].update(visible=True)
    window['Loading2'].update(visible=False)
    threading.Thread(target=checkRpicamsrc, args=(), daemon=True).start()


def checkRpicamsrc():
    window['Loading3'].update(visible=True)
    window['installRpicamsrc'].update(visible=False)
    window['rpicamsrcInstalled'].update(visible=False)
    window.refresh()
    if getdp.checkRpicamsrc() == 0: #the function returns a 1 or a 0. 0 for when gstreamer-tools is not installed and 1 for when it is.
        #gstreamer-tools not installed
        window['installRpicamsrc'].update(visible=True)
    else:
        #gstreamer-tools is installed
        window['rpicamsrcInstalled'].update(visible=True)
    window['Loading3'].update(visible=False)
    threading.Thread(target=checkRaspidmx, args=(), daemon=True).start()

def checkRaspidmx():
    window['Loading4'].update(visible=True)
    window['installRaspidmx'].update(visible=False)
    window['RaspidmxInstalled'].update(visible=False)
    
    window.refresh()
    if getdp.checkRaspidmx() == 0: #the function returns a 1 or a 0. 0 for when gstreamer-tools is not installed and 1 for when it is.
        #gstreamer-tools not installed
        window['installRaspidmx'].update(visible=True)
    else:
        #gstreamer-tools is installed
        window['RaspidmxInstalled'].update(visible=True)
        window['Loading4'].update(visible=False)

def installGstreamertools():
    window['installGstreamer-tools'].update(visible=False)
    window['Loading1'].update(visible=True)
    window.refresh()
    getD.installGstreamertools()
    window['Loading1'].update(visible=False)
    window['installRpicamsrc'].update(disabled=False)
    window['installGstreamerdev'].update(disabled=False)
    window['installRaspidmx'].update(disabled=False)


def installRpicamsrc():
    window['installRpicamsrc'].update(visible=False)
    window['Loading3'].update(visible=True)
    window.refresh()
    getD.installRpicamsrc()
    window['Loading3'].update(visible=False)
    window['installRpicamsrc'].update(disabled=False)
    window['installGstreamerdev'].update(disabled=False)
    window['installRaspidmx'].update(disabled=False)

def installGstreamerdev():
    window['installGstreamerdev'].update(visible=False)
    window['Loading2'].update(visible=True)
    window.refresh()
    getD.installGstreamerdev()
    window['Loading2'].update(visible=False)
    window['installRpicamsrc'].update(disabled=False)
    window['installGstreamerdev'].update(disabled=False)
    window['installRaspidmx'].update(disabled=False)

def installRaspidmx():
    window['installRaspidmx'].update(visible=False)
    window['Loading4'].update(visible=True)
    window.refresh()
    getD.installRaspidmx()
    window['Loading4'].update(visible=False)
    window['installRpicamsrc'].update(disabled=False)
    window['installGstreamerdev'].update(disabled=False)
    window['installRaspidmx'].update(disabled=False)

def readyStream():
    RStream.makespdfile()
    with open(cd + '/config.txt') as json_file:
        config = json.load(json_file)
        canStream = RStream.checkReceivestream() 
        if canStream == 0 and config['ledTexture'] == True:
            Ring.makeTexture()
        elif canStream == 0 and config['ledStrip'] == True:
           print('startled')
           LED.setcolor()

def makeConfig(values, configspecs):
    config.makeConfig(values, configspecs)
    RStream.stream()

def checkStream():
    if RStream.checkstream() == 0:
        window['streaming'].update(visible=True)
        window['notStreaming'].update(visible=False)
    else:
        window['notStreaming'].update(visible=True)
        window['streaming'].update(visible=False)


while True:
    #######################################################################################
    #Main
    #######################################################################################
    event, values = window.read()
    #staticLayout   
    if event in (None, 'Exit'):
        RStream.stopreceivingstream()
        RStream.stopstream()
        Ring.stopRing()
        LED.ledOff()
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
    ##############
    #Intro
    ##############
    if event == 'checkConfigButton' and os.path.isfile(cd + '/config.txt'):
        window['checkConfigText'].update(visible=False)
        window['checkConfigButton'].update(visible=False)
        window['configText'].update(visible=True)
        window['configButton'].update(visible=True)
    elif event == 'checkConfigButton':
        window['noConfig'].update(visible=True)

    if event == 'configButton':
        RStream.stream()
        if RStream.checkstream() == 0:
            window['streaming'].update(visible=True)
            window['notStreaming'].update(visible=False)
        else:
            window['notStreaming'].update(visible=True)
            window['streaming'].update(visible=False)
        window[f'-PG{staticLayout}-'].update(visible=False)
        window[f'-T{staticLayout}-'].update(visible=False)
        staticLayout = 5
        window[f'-PG{staticLayout}-'].update(visible=True)
        window[f'-T{staticLayout}-'].update(visible=True)

    #######################################################################################
    #Dependencies
    #######################################################################################
    
    if event == 'checkDependencies':
        threading.Thread(target=checkGstreamer, args=(), daemon=True).start()
    if event == 'installGstreamer-tools':
        window['installGstreamer-tools'].update(disabled=True)
        window['installRpicamsrc'].update(disabled=True)
        window['installGstreamerdev'].update(disabled=True)
        window['installRaspidmx'].update(disabled=True)
        threading.Thread(target=installGstreamertools, args=(), daemon=True).start()

    elif event == 'installRpicamsrc':
        window['installGstreamer-tools'].update(disabled=True)
        window['installRpicamsrc'].update(disabled=True)
        window['installGstreamerdev'].update(disabled=True)
        window['installRaspidmx'].update(disabled=True)
        threading.Thread(target=installRpicamsrc, args=(), daemon=True).start()
    elif event == 'installGstreamerdev':
        window['installGstreamer-tools'].update(disabled=True)
        window['installRpicamsrc'].update(disabled=True)
        window['installGstreamerdev'].update(disabled=True)
        window['installRaspidmx'].update(disabled=True)
        threading.Thread(target=installGstreamerdev, args=(), daemon=True).start()
    elif event == 'installRaspidmx':
        window['installGstreamer-tools'].update(disabled=True)
        window['installRpicamsrc'].update(disabled=True)
        window['installGstreamerdev'].update(disabled=True)
        window['installRaspidmx'].update(disabled=True)
        threading.Thread(target=installRaspidmx, args=(), daemon=True).start()

    ###########
    #options
    ###########
    if event == 'goTextureSettings':
        window['texturemenu'].update(visible=True)
        window[f'-PG{staticLayout}-'].update(visible=False)
        window['nbuttons'].update(visible=False)
    elif event == 'goLedSettings':
        window['ledstripmenu'].update(visible=True)
        window[f'-PG{staticLayout}-'].update(visible=False)
        window['nbuttons'].update(visible=False)
    if event == 'backFromTexture':
        window['texturemenu'].update(visible=False)
        window[f'-PG{staticLayout}-'].update(visible=True)
        window['nbuttons'].update(visible=True)
    elif event == 'backFromLed':
        window['ledstripmenu'].update(visible=False)
        window[f'-PG{staticLayout}-'].update(visible=True)
        window['nbuttons'].update(visible=True)

    if event == 'showColor':
        rgb = (values['customR'], values['customG'], values['customB'])
        LED.showColor(rgb)
    if event == 'backFromLed':
        LED.ledOff()
    #######################################################################################
    #receive stream
    #######################################################################################
    if event == 'nextPage' and staticLayout == 5:
        configspecs = ['otherIP', 'targetipWidth', 'targetipHeight','targetFramerate' , 'ledStrip', 'ledTexture', 'noRing', 'streamBitrate', 'portSender', 'portReceiver', 'blueLed', 'orangeLed', 'ring1080', 'ring720', 'customColor', 'slbrightness', 'customR', 'customG', 'customB', 'customTexture', 'customPath']       
    
        threading.Thread(target=makeConfig, args=(values, configspecs), daemon=True).start()
        threading.Thread(target=checkStream, args=(), daemon=True).start()

    if event == 'readyStream':
        threading.Thread(target=readyStream, args=(), daemon=True).start()
              
    if event == 'prevPage' and staticLayout == 4:
        RStream.stopreceivingstream()
        RStream.stopstream()
        Ring.stopRing()
        LED.ledOff()
        
window.close()
from typing import Text
import PySimpleGUI as gui
import getIP as getip


gui.theme('Default1')
gui.theme_background_color(('#ebfdff'))
gui.theme_element_background_color(('#ebfdff'))
gui.theme_input_background_color(('white'))
gui.theme_element_text_color(('#ebfdff'))
gui.theme_button_color(('#ebfdff'))

textBackground = gui.theme_background_color()
Introduction = [
        [gui.Text('Office Portals', font=("Helcentica", 20), background_color=textBackground)],
        [gui.Text('A nerdy solution to make distant colleagues feel nearby', font=("Helcentica", 12), background_color=textBackground)],
        [gui.Text('Welcome to Office Portal!', background_color=textBackground)],
        [gui.Text('Before we can start we need to do the setup first', background_color=textBackground)],
        [gui.Text('Click on the button next page to start the setup.', background_color=textBackground)]]  

Dependencies = [
        [gui.Text('Dependencies:', font=("Helcentica", 20), background_color=textBackground)],
        [gui.Text('To use Office Portal you need to have installed a few dependencies.', background_color=textBackground)],
        [gui.Text('Click on check to check if you have the dependency installed.', background_color=textBackground)],         
        [gui.Text('If you see a green check the dependency is installed.', background_color=textBackground)],
        [gui.Text('If you see a red cross the dependency is not installed.', background_color=textBackground)],
        [gui.Text('Click on the red cross to install the dependency.', background_color=textBackground)],
        [gui.Text('Gstreamer-Tools:', background_color=textBackground), gui.Button(key=('checkGstreamer'), button_text=('check')), gui.Button(visible = False ,key=('gstreamer-toolsInstalled'),  image_filename='Pictures/Green_Check.png', border_width=0), gui.Button(visible = False ,key=('installGstreamer-tools'), image_filename='Pictures/arrow_down.png', border_width=0), gui.Button(visible = False ,key=('Loading1'), image_filename='Pictures/loading.png', border_width=0)],
        [gui.Text('Gstreamer-dev packages:', background_color=textBackground), gui.Button(key=('checkGstreamerdev'), button_text=('check')), gui.Button(visible = False ,key=('gstreamerdevInstalled'),  image_filename='Pictures/Green_Check.png', border_width=0), gui.Button(visible = False ,key=('installGstreamerdev'), image_filename='Pictures/arrow_down.png', border_width=0), gui.Button(visible = False ,key=('Loading2'), image_filename='Pictures/loading.png', border_width=0)],
        [gui.Text('RpiCamSrc:', background_color=textBackground), gui.Button(key=('checkRpicamsrc'), button_text=('check')), gui.Button(visible = False ,key=('rpicamsrcInstalled'),  image_filename='Pictures/Green_Check.png', border_width=0), gui.Button(visible = False ,key=('installRpicamsrc'), image_filename='Pictures/arrow_down.png', border_width=0), gui.Button(visible = False ,key=('Loading3'), image_filename='Pictures/loading.png', border_width=0)]]

Options = [
        [gui.Text('Options:', font=("Helcentica", 20), background_color=textBackground)],
        [gui.Text('Here we have a few options we have to fill in correctly', font=('Helcentica',12), background_color=textBackground)],
        [gui.Text('Portal resolution:', background_color=textBackground)],
        [gui.Text('Sending stream spesifications:', font=('Helcentica',12), background_color=textBackground)],
        [gui.Text('Resolution of the other portal:', background_color=textBackground), gui.Input('1920', key='targetipWidth', size=(4,1)), gui.Text('x', background_color=textBackground), gui.Input('1080',key='targetipHeight', size=(4,1))],
        [gui.Text('Framerate:', background_color=textBackground), gui.Input('20', key=('targetFramerate'), size=(2,1))],
        [gui.Text('Portal ring potion (not ready):', background_color=textBackground, font=('Helcentica',12))],
        [gui.Text('Ledstrip:', background_color=textBackground), gui.Radio(text=None, group_id=('portalLed'), key=('ledStrip')), gui.Text('Texture:', background_color=textBackground), gui.Radio(text=None, group_id=('portalLed'), key=('ledTexture')), gui.Text('None:', background_color=textBackground), gui.Radio(text=None, group_id=('portalLed'), key=('noRing'), default=True)],
        [gui.Text('Startup program on boot:', background_color=textBackground), gui.Checkbox(key=('autoStart'), text=None)]]

advancedOptions = [
        [gui.Text('Advanced options', font=("Helcentica", 20), background_color=textBackground)],
        [gui.Text('Here we have a few advanced options.', font=('Helcentica',12), background_color=textBackground)],
        [gui.Text('You can just leave them as default.', font=('Helcentica',12), background_color=textBackground)],
        [gui.Text('Its reccomended to only change them if you have a problem', background_color=textBackground)], 
        [gui.Text('Bitrate stream:', background_color=textBackground), gui.Input('4000000', key=('streamBitrate'), size=(8,1))],
        [gui.Text('Port sender:', background_color=textBackground), gui.Input('5000', key=('portSender'), size=(8,1))],
        [gui.Text('Port receiver:', background_color=textBackground), gui.Input('5000', key=('portReceiver'), size=(8,1))]]

connectPI = [
        [gui.Text('Connect to the other PI', font=("Helcentica", 20), background_color=textBackground)],
        [gui.Text('Its time to connect to the other portal!', font=("Helcentica", 12), background_color=textBackground)],
        [gui.Text('This PIs IP:', background_color=textBackground), gui.Text(getip.getip())],
        [gui.Text('Enter here the ip from the other pi:', background_color=textBackground), gui.Input('192.168.x.xxx', key=('otherIP'), size=(15,1))],
        [gui.Text('(Only continue when youve entered the correct ip of the other pi)', background_color=textBackground)]]

receiveStream = [
        [gui.Text('Stream and Receive', font=("Helcentica", 20), background_color=textBackground)],
        [gui.Text('Click on the ready button if you are on this screen on both PIs', font=("Helcentica", 12), background_color=textBackground)],
        [gui.Image(filename='Pictures/officeportalconnect.png')],
        [gui.Button('Ready', key=('readyStream'))],
        [gui.Text('Streaming status:', font=("Helcentica", 12), background_color=textBackground), gui.Image(visible = False, key='notStreaming', filename='Pictures/Red_Cross.png'), gui.Image(visible = False, key='streaming',filename='Pictures/Green_Check.png')]]
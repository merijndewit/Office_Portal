from typing import Text
import PySimpleGUI as gui
import getIP as getip
import Theme
import sys,os

Theme.setTheme()

textBackground = gui.theme_background_color()
if getattr(sys, 'frozen', False):
    cwd = os.path.dirname(sys.executable)
else:
    cwd = os.path.dirname(os.path.abspath(__file__))

loadingGif = (cwd + '/Pictures/Loading.gif')

Introduction = [
        [gui.Text('A nerdy solution to make distant colleagues feel nearby', font=("Helcentica", 12), background_color=textBackground)],
        [gui.Text('Welcome to Office Portal!', background_color=textBackground)],
        [gui.Text('Before we can start we need to do the setup first', background_color=textBackground)],
        [gui.Text('Click on the button next page to start the setup.', background_color=textBackground)],
        [gui.Text('Click here to check for previous config:', key='checkConfigText', visible=True, background_color=textBackground),gui.Button('Load settings', key='checkConfigButton', visible=True, mouseover_colors=Theme.mouseOver), gui.Text('Config file found! press this botton to load the config and go to stream and receive:', key='configText', visible=False, background_color=textBackground), gui.Button('Load Config', key='configButton', visible=False, mouseover_colors=Theme.mouseOver), gui.Text('no config found', visible=False, key='noConfig', background_color=textBackground)]]

Dependencies = [
        [gui.Text('To use Office Portal you need to have installed a few dependencies.', background_color=textBackground)],
        [gui.Text('Click on check to check the current installed dependencies.', background_color=textBackground)],
        [gui.Button(key='checkDependencies' ,button_text='Check')],       
        [gui.Text('Gstreamer-Tools:', background_color=textBackground), gui.Image(visible = False, key=('gstreamer-toolsInstalled'), filename=(cwd + '/Pictures/Green_Check.png')), gui.Button(visible = False ,key=('installGstreamer-tools'), image_filename=(cwd + '/Pictures/arrow_down.png'), border_width=0, mouseover_colors=Theme.mouseOver), gui.Image(visible = False ,key=('Loading1'))],
        [gui.Text('Gstreamer-dev packages:', background_color=textBackground), gui.Image(visible = False ,key=('gstreamerdevInstalled'),  filename=(cwd + '/Pictures/Green_Check.png')), gui.Button(visible = False ,key=('installGstreamerdev'), image_filename=(cwd + '/Pictures/arrow_down.png'), border_width=0, mouseover_colors=Theme.mouseOver), gui.Image(visible = False ,key=('Loading2'))],
        [gui.Text('RpiCamSrc:', background_color=textBackground), gui.Image(visible = False ,key=('rpicamsrcInstalled'),  filename=(cwd + '/Pictures/Green_Check.png')), gui.Button(visible = False ,key=('installRpicamsrc'), image_filename=(cwd + '/Pictures/arrow_down.png'), border_width=0, mouseover_colors=Theme.mouseOver), gui.Image(visible = False ,key=('Loading3'))],
        [gui.Text('Raspidmx:', background_color=textBackground), gui.Image(visible = False ,key=('RaspidmxInstalled'),  filename=(cwd + '/Pictures/Green_Check.png')), gui.Button(visible = False ,key=('installRaspidmx'), image_filename=(cwd + '/Pictures/arrow_down.png'), border_width=0, mouseover_colors=Theme.mouseOver), gui.Image(visible = False ,key=('Loading4'))]]

Options = [
        [gui.Text('Here we have a few options we have to fill in correctly', font=('Helcentica',12), background_color=textBackground)],
        [gui.Text('Sending stream spesifications:', font=('Helcentica',12), background_color=textBackground)],
        [gui.Text('Resolution of the other portal:', background_color=textBackground), gui.Input('1920', key='targetipWidth', size=(4,1)), gui.Text('x', background_color=textBackground), gui.Input('1080',key='targetipHeight', size=(4,1))],
        [gui.Text('Framerate:', background_color=textBackground), gui.Input('20', key=('targetFramerate'), size=(2,1))],
        [gui.Text('Portal ring potion:', background_color=textBackground, font=('Helcentica',12))],
        [gui.Text('Color: Blue:', background_color=textBackground), gui.Radio(text=None, group_id=('colorLed'), key=('blueLed'), default=True), gui.Text('Orange:', background_color=textBackground), gui.Radio(text=None, group_id=('colorLed'), key=('orangeLed'))],
        [gui.Text('Choose one of these:', font=("Helcentica", 12), background_color=textBackground)],
        [gui.Text('Texture:', background_color=textBackground), gui.Radio(text=None, group_id=('portalLed'), key=('ledTexture')), gui.Button('Texture settings', key='goTextureSettings', mouseover_colors=Theme.mouseOver)],
        [gui.Text('Ledstrip:', background_color=textBackground), gui.Radio(text=None, group_id=('portalLed'), key=('ledStrip')), gui.Button('Led settings', key='goLedSettings', mouseover_colors=Theme.mouseOver)],
        [gui.Text('None:', background_color=textBackground), gui.Radio(text=None, group_id=('portalLed'), key=('noRing'), default=True)]]
  

advancedOptions = [
        [gui.Text('Here we have a few advanced options.', font=('Helcentica',12), background_color=textBackground)],
        [gui.Text('You can just leave them as default.', font=('Helcentica',12), background_color=textBackground)],
        [gui.Text('Its reccomended to only change them if you have a problem', background_color=textBackground)], 
        [gui.Text('Bitrate stream:', background_color=textBackground), gui.Input('4000000', key=('streamBitrate'), size=(8,1))],
        [gui.Text('Port sender:', background_color=textBackground), gui.Input('5000', key=('portSender'), size=(8,1))],
        [gui.Text('Port receiver:', background_color=textBackground, visible=False), gui.Input('5000', key=('portReceiver'), size=(8,1), visible=False)]]

connectPI = [
        [gui.Text('Its time to connect to the other portal!', font=("Helcentica", 12), background_color=textBackground)],
        [gui.Text('This PIs IP:', background_color=textBackground), gui.Text(getip.getip())],
        [gui.Text('Enter here the ip from the other pi:', background_color=textBackground), gui.Input('192.168.x.xxx', key=('otherIP'), size=(15,1))],
        [gui.Text('(Only continue when youve entered the correct ip of the other pi)', background_color=textBackground)],
        [gui.Image(filename=(cwd + '/Pictures/Connect_Image.png'))]]

receiveStream = [
        [gui.Text('Click on the ready button if you are on this screen on both PIs', font=("Helcentica", 12), background_color=textBackground)],
        [gui.Image(filename=(cwd + '/Pictures/officeportalconnect.png'))],
        [gui.Button('Ready', key=('readyStream'), mouseover_colors=Theme.mouseOver)],
        [gui.Text('Streaming status:', font=("Helcentica", 12), background_color=textBackground), gui.Image(visible = False, key='notStreaming', filename=(cwd + '/Pictures/Red_Cross.png')), gui.Image(visible = False, key='streaming',filename=(cwd + '/Pictures/Green_Check.png'))]]

navigationButtons = [
        [gui.Button(key='prevPage', image_filename=(cwd + '/Pictures/arrow_left.png'), border_width=0, mouseover_colors=Theme.mouseOver, visible=True), gui.Button(key='Exit', image_filename=(cwd + '/Pictures/Exit_Button.png'), border_width=0, mouseover_colors=Theme.mouseOver),gui.Button(key='nextPage', image_filename=(cwd + '/Pictures/arrow_right.png'), border_width=0, mouseover_colors=Theme.mouseOver)]]

ledstripMenu = [
        [gui.Text('Brightness:', background_color=textBackground), gui.Slider(range=(0,1), default_value=1, resolution=0.1, orientation='h', key='slbrightness')],
        [gui.Text('Click here to use a custom RGB color for the led strip:', background_color=textBackground), gui.Checkbox(text=None, key='customColor')],
        [gui.Text('Custom RGB:', background_color=textBackground), gui.Input('255', key=('customR'), size=(3,1)), gui.Input('255', key=('customG'), size=(3,1)), gui.Input('255', key=('customB'), size=(3,1)), gui.Button('show color', key='showColor')],
        [gui.Button('Back', key='backFromLed', mouseover_colors=Theme.mouseOver)]]

textureMenu = [
        [gui.Text('Resolution: 1080p:', background_color=textBackground), gui.Radio(text=None, group_id=('resRing'), key=('ring1080'), default=True), gui.Text('720p:', background_color=textBackground), gui.Radio(text=None, group_id=('resRing'), key=('ring720'))],
        [gui.Text('Click here to use a custom texture mask:', background_color=textBackground), gui.Checkbox(text=None, key='customTexture')],
        [gui.Text('Select a File (png only)                                                                          ', background_color=textBackground), gui.FileBrowse(button_text='browse', file_types = (('ALL Files', '*.*'),), key='customPath')],
        [gui.Button('Back', key='backFromTexture', mouseover_colors=Theme.mouseOver)]]

staticLayout = [
        [gui.Text('Office Portal',font=("Helcentica", 32), background_color=Theme.borderColor, size=(60, 1), key='-T0-'), gui.Text('Dependencies',font=("Helcentica", 32), background_color=Theme.borderColor, size=(60, 1), key='-T1-', visible=False), gui.Text('Options',font=("Helcentica", 32), background_color=Theme.borderColor, size=(60, 1), key='-T2-', visible=False), gui.Text('Advanced Options',font=("Helcentica", 32), background_color=Theme.borderColor, size=(60, 1), key='-T3-', visible=False), gui.Text('Connect',font=("Helcentica", 32), background_color=Theme.borderColor, size=(60, 1), key='-T4-', visible=False), gui.Text('Stream and Receive',font=("Helcentica", 32), background_color=Theme.borderColor, size=(60, 1), key='-T5-', visible=False)],
        [gui.Column(Introduction, key='-PG0-'), gui.Column(Dependencies, visible=False, key='-PG1-'), gui.Column(Options, visible=False, key='-PG2-'), gui.Column(advancedOptions, visible=False, key='-PG3-'), gui.Column(connectPI, visible=False, key='-PG4-'), gui.Column(receiveStream, visible=False, key='-PG5-'), gui.Column(ledstripMenu, key='ledstripmenu', visible=False), gui.Column(textureMenu, key='texturemenu', visible=False)],
        [gui.Column(navigationButtons, key='nbuttons')]]

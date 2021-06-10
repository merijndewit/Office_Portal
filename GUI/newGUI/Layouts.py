from typing import Text
import PySimpleGUI as gui

gui.theme('Default1')
Introduction = [
        [gui.Text('Office Portals', font=("Helcentica", 20))],
        [gui.Text('A nerdy solution to make distant colleagues feel nearby', font=("Helcentica", 12))],
        [gui.Text('Welcome to Office Portal!')],
        [gui.Text('Before we can start we need to do the setup first')],
        [gui.Text('Click on the button next page to start the setup.')]]
         

Dependencies = [
        [gui.Text('Dependencies:', font=("Helcentica", 20))],
        [gui.Text('To use Office Portal you need to have installed a few dependencies.')],
        [gui.Text('Click on check to check if you have the dependency installed.')],         
        [gui.Text('If you see a green check the dependency is installed.')],
        [gui.Text('If you see a red cross the dependency is not installed.')],
        [gui.Text('Click on the red cross to install the dependency.')],
        [gui.Text('Gstreamer-Tools:'), gui.Button(key=('checkGstreamer'), button_text=('check')), gui.Button(visible = False ,key=('gstreamer-toolsInstalled'),  image_filename='Pictures/Green_Check.png', border_width=0), gui.Button(visible = False ,key=('installGstreamer-tools'), image_filename='Pictures/Red_Cross.png', border_width=0), gui.Button(visible = False ,key=('Loading1'), image_filename='Pictures/loading.png', border_width=0)],
        [gui.Text('Gstreamer-dev packages:'), gui.Button(key=('checkGstreamerdev'), button_text=('check')), gui.Button(visible = False ,key=('gstreamerdevInstalled'),  image_filename='Pictures/Green_Check.png', border_width=0), gui.Button(visible = False ,key=('installGstreamerdev'), image_filename='Pictures/Red_Cross.png', border_width=0), gui.Button(visible = False ,key=('Loading2'), image_filename='Pictures/loading.png', border_width=0)],
        [gui.Text('RpiCamSrc:'), gui.Button(key=('checkRpicamsrc'), button_text=('check')), gui.Button(visible = False ,key=('rpicamsrcInstalled'),  image_filename='Pictures/Green_Check.png', border_width=0), gui.Button(visible = False ,key=('installRpicamsrc'), image_filename='Pictures/Red_Cross.png', border_width=0), gui.Button(visible = False ,key=('Loading3'), image_filename='Pictures/loading.png', border_width=0)]]

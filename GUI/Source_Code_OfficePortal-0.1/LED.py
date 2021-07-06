from typing import Awaitable
import board
import neopixel
import sys,os
import json

if getattr(sys, 'frozen', False):
    cd = os.path.dirname(sys.executable)
else:
    cd = os.path.dirname(os.path.abspath(__file__))

pixels = neopixel.NeoPixel(board.D18, 13)
pixels.fill((0, 0, 0))
def setcolor():
    global pixels
    with open(cd + '/config.txt') as json_file:
        config = json.load(json_file) 
        pixels.brightness = float(config['brightness'])
        if config['customcolor'] == True:
            pixels.fill((int(config['Rvalue']), int(config['Gvalue']), int(config['Bvalue'])))
        else:
            if config['blue'] == True:
                pixels.fill((0, 179, 255))
            else:
                pixels.fill((255, 60, 0))
                print('ledOrange')

def showColor(rgb):
    pixels.fill((int(rgb[0]), int(rgb[1]), int(rgb[2])))

def ledOff():
    try:
        pixels.fill((0, 0, 0))

    except:
        print('no led strip')
    

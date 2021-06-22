from typing import Awaitable
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 13)
pixels.fill((0, 0, 0))
def setcolor():
    global pixels
    with open('office_portal.txt') as f:
            configLines = [ line.strip() for line in f ]
    pixels.brightness = float(configLines[16])
    if configLines[15] == 'True':
        pixels.fill((int(configLines[17]), int(configLines[18]), int(configLines[19])))
    else:
        if configLines[11] == 'True':
            pixels.fill((0, 179, 255))
        else:
            pixels.fill((255, 60, 0))
            print('ledOrange')
    

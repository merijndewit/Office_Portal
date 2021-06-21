import board
import neopixel
pixels = neopixel.NeoPixel(board.D10, 13)

def setcolor():
    with open('office_portal.txt') as f:
        configLines = [ line.strip() for line in f ]
    if configLines[11] == 'True':
        pixels.fill((137, 207, 240))
        print('ledBlue')
    else:
        pixels.fill((255, 92, 0))
        print('ledOrange')
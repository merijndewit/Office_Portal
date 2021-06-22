import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 13)
pixels.fill((0, 0, 0))
def setcolor():
    global pixels
    pixels.brightness = 1
    with open('office_portal.txt') as f:
        configLines = [ line.strip() for line in f ]
    
    if configLines[11] == 'True':
        pixels.fill((0, 100, 0))
    else:
        pixels.fill((100, 0, 0))
        print('ledOrange')
    

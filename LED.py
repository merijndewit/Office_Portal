import board
import neopixel
pixels = neopixel.NeoPixel(board.D10, 13)

def setcolor(color):
    if color is False:
        pixels.fill((255, 92, 0))
    else:
        pixels.fill((137, 207, 240))


import sys,os
import json

if getattr(sys, 'frozen', False):
    cd = os.path.dirname(sys.executable)
else:
    cd = os.path.dirname(os.path.abspath(__file__))

def makeConfig(values, configspecs):
    config = {}
    config['streamInfo'] = []
    config = {
    'ip': values[configspecs[0]],
    'pixelWidth': values[configspecs[1]],
    'pixelHeight': values[configspecs[2]],
    'framerate': values[configspecs[3]],
    'ledStrip': values[configspecs[4]],
    'ledTexture': values[configspecs[5]],
    'none': values[configspecs[6]],
    'bitrate': values[configspecs[7]],
    'portSend': values[configspecs[8]],
    'portReceive': values[configspecs[9]],
    'blue': values[configspecs[10]],
    'orange': values[configspecs[11]],
    'ring1080': values[configspecs[12]],
    'ring720': values[configspecs[13]],
    'customcolor': values[configspecs[14]],
    'brightness': values[configspecs[15]],
    'Rvalue': values[configspecs[16]],
    'Gvalue': values[configspecs[17]],
    'Bvalue': values[configspecs[18]],
    'customTexture': values[configspecs[19]],
    'customPath': values[configspecs[20]]
    }
    with open(cd + '/config.txt', 'w+') as outfile:
        json.dump(config, outfile)

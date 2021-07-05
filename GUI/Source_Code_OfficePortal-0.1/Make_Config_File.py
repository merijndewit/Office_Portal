import sys,os
import json

if getattr(sys, 'frozen', False):
    cd = os.path.dirname(sys.executable)
else:
    cd = os.path.dirname(os.path.abspath(__file__))

def clearConfigfile():
    #f = open(cd + '/office_portal.txt', "w+")
    #f.truncate(0)
    #f.close()
    return(0)
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
    'autostart': values[configspecs[7]],
    'bitrate': values[configspecs[8]],
    'portSend': values[configspecs[9]],
    'portReceive': values[configspecs[10]],
    'blue': values[configspecs[11]],
    'orange': values[configspecs[12]],
    'ring1080': values[configspecs[13]],
    'ring720': values[configspecs[14]],
    'customcolor': values[configspecs[15]],
    'brightness': values[configspecs[16]],
    'Rvalue': values[configspecs[17]],
    'Gvalue': values[configspecs[18]],
    'Bvalue': values[configspecs[19]],
    'customTexture': values[configspecs[20]],
    'customPath': values[configspecs[21]]
    }
    with open(cd + '/config.txt', 'w+') as outfile:
        json.dump(config, outfile)

import subprocess
import sys,os
import signal

if getattr(sys, 'frozen', False):
    cd = os.path.dirname(sys.executable)
else:
    cd = os.path.dirname(os.path.abspath(__file__))

def makeTexture():
    global _ringTexture
    with open(cd + '/office_portal.txt') as f:
        configLines = [ line.strip() for line in f ]
    
    picture = None
    if str(configLines[13]) == "True": #if 1080p resulution is selected
        if configLines[11] == 'True': #if color blue is selected
            picture = '1080pblue.png'
        else:
            picture = '1080porange.png'
    else:
        if configLines[11] == 'True': #if color blue is selected
            picture = '720pblue.png'
        else:
            picture = '720porange.png'

    if configLines[20] == 'True':
        pathToPicture = configLines[21]
    else:
        pathToPicture = (cd + '/Pictures/' + picture)
    _ringTexture = subprocess.Popen(["./home/pi/raspidmx/pngview/pngview", "-b", "0", "-l", "3", pathToPicture], cwd='/', preexec_fn=os.setsid)

def stopRing():
    global _ringTexture
    try:
        os.killpg(os.getpgid(_ringTexture.pid), signal.SIGTERM)
        _ringTexture = None
        print("stopped ring")
    except:
        print("no ring running")
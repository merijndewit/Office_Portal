import subprocess
import os
import signal

def makeTexture():
    global _ringTexture
    
    with open('office_portal.txt') as f:
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
        pathToPicture = '/home/pi/Office_Portal/GUI/Source_Code_OfficePortal-0.1/Pictures/' + picture
    _ringTexture = subprocess.Popen(["./home/pi/raspidmx/pngview/pngview", "-b", "0", "-l", "3", pathToPicture], cwd='/', preexec_fn=os.setsid)

def stopRing():
    global _ringTexture
    try:
        os.killpg(os.getpgid(_ringTexture.pid), signal.SIGTERM)
        _ringTexture = None
        print("stopped ring")
    except:
        print("no ring running")
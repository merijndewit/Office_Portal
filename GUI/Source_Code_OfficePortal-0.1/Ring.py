import subprocess
import os
import signal

def makeTexture():
    global _ringTexture
    pathToPicture = 'Office_Portal/GUI/Source_Code_OfficePortal-0.1/Pictures/'
    _ringTexture = subprocess.Popen(["./raspidmx/pngview/pngview", "-b", "0", "-l", "3", pathToPicture + "test.png"], cwd='/home/pi/', preexec_fn=os.setsid)
    

def stopRing():
    global _ringTexture
    try:
        os.killpg(os.getpgid(_ringTexture.pid), signal.SIGTERM)
        _ringTexture = None
        print("stopped ring")
    except:
        print("no ring running")
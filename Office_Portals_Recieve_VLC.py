import subprocess
import signal
import os

_rcstream = None
def recieveStream():
    global _rcstream
    _rcstream = subprocess.Popen(["omxplayer", "--live", streamURL, "--aspect-mode", "full"], stdout=subprocess.PIPE, preexec_fn=os.setsid)
    print("recieving stream for CSI camera")

def stopreceivingstream():
    global _rcstream
    subprocess.Popen.kill(_rcstream)
    print(_rcstream)
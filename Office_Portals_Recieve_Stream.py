import subprocess
import signal
import os

_rcstream = None
def recieveStream():
    global _rcstream

    _rcstream = subprocess.Popen(["omxplayer","--live","stream.spd"], stdout=subprocess.PIPE, preexec_fn=os.setsid)
    print("recieving stream for CSI camera")

def stopreceivingstream():
    global _rcstream
    if '_stream' in globals() and hasattr(_rcstream, 'pid'):
        subprocess.Popen.kill(_rcstream)
        _stream = None
        print("stopped receiving stream")
    else:
        print("no stream to terminate")
    print(_rcstream)
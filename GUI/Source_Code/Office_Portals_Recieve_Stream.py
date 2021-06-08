import subprocess
import signal
import os
import time


def receiveStream():
    global _rcstream
    _rcstream = None
    _rcstream = subprocess.Popen(["omxplayer", "--live", "stream.spd"], preexec_fn=os.setsid)
    print("started stream")


def stopreceivingstream():
    global _rcstream
    if '_rcstream' in globals() and hasattr(_rcstream, 'pid'):
        #subprocess.Popen.kill(_rcstream)
        os.killpg(os.getpgid(_rcstream.pid), signal.SIGTERM)
        _rcstream = None
        print("stopped receiving stream")
    else:
        print("no stream to terminate")
    print(_rcstream)

def makespdfile():
    if ip == None:
        return("cant recieve stream, please enter the targetIP")
    else:
        f = open('/home/pi/Office_Portal/GUI/Source_Code/stream.spd', "w+")
        f.writelines(["v=0\n","m=video 5000 RTP/AVP 96\n","c=IN IP4 " + ip + "\n","a=rtpmap:96 H264/90000\n"])
        f.close()
        print("file created")
        time.sleep(1)
        receiveStream()
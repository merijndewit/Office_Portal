import subprocess
import signal
import os
import time



def receiveStream():
    global _rcstream
    _rcstream = None
    _rcstream = subprocess.Popen(["omxplayer", "--live", "stream.spd"], preexec_fn=os.setsid)
    print("started stream")

def makespdfile():
    config = open('office_portal.txt')
    configLines = config.readlines()
    f = open('stream.spd', "w+")
    f.writelines(["v=0\n","m=video 5000 RTP/AVP 96\n","c=IN IP4 " + configLines[0] + "\n","a=rtpmap:96 H264/90000"])
    f.close()
    config.close()
    print("file created")
    time.sleep(1)
    receiveStream()

def stream():
    config = open('office_portal.txt')
    configLines = config.readlines()
    global _stream
    _stream = None
    _stream = subprocess.Popen(["gst-launch-1.0","rpicamsrc","preview=False","name=videosrc","bitrate=",configLines[8],"!","h264parse","!","video/x-h264,framerate=",configLines[3] + "/1,","width=",configLines[1],",height=",configLines[2],"!","rtph264pay","pt=96","config-interval=5","!","udpsink","host=",configLines[0],"port=", configLines[9]], preexec_fn=os.setsid)
    print("started stream for CSI camera")
    config.close()

def stopstream():
    global _stream
    if '_stream' in globals() and hasattr(_stream, 'pid'):
        subprocess.Popen.kill(_stream)
        _stream = None
        print("stream termindated")
    else:
        print("no stream to terminate")

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
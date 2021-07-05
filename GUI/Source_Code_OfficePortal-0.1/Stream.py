import subprocess
import signal
import sys,os
import time
import json

if getattr(sys, 'frozen', False):
    cd = os.path.dirname(sys.executable)
else:
    cd = os.path.dirname(os.path.abspath(__file__))

def receiveStream():
    global _rcstream
    _rcstream = None
    _rcstream = subprocess.Popen(["omxplayer", "--live", cd + "/stream.spd"], preexec_fn=os.setsid)
    print("started stream")

def makespdfile():
    with open(cd + '/config.txt') as json_file:
        config = json.load(json_file)
        f = open(cd + '/stream.spd', "w+")
        f.writelines(["v=0\n","m=video 5000 RTP/AVP 96\n","c=IN IP4 " + config['ip'] + "\n","a=rtpmap:96 H264/90000"])
        f.close()
    print("file created")
    time.sleep(1)
    receiveStream()

def stream():
    with open(cd + '/config.txt') as json_file:
        config = json.load(json_file)
        global _stream
        _stream = None
        _stream = subprocess.Popen(["gst-launch-1.0","rpicamsrc","preview=False","name=videosrc","bitrate=",config['bitrate'],"!","h264parse","!","video/x-h264,framerate=" + config['framerate'] + "/1,","width=",config['pixelWidth'],",height=",config['pixelHeight'],"!","rtph264pay","pt=96","config-interval=5","!","udpsink","host=",config['ip'],"port=", config['portSend']], preexec_fn=os.setsid)
    print("started stream for CSI camera")

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
    try:
        if '_rcstream' in globals() and hasattr(_rcstream, 'pid'):
            #subprocess.Popen.kill(_rcstream)
            os.killpg(os.getpgid(_rcstream.pid), signal.SIGTERM)
            _rcstream = None
            print("stopped receiving stream")
    except:
        print("no stream to terminate")

def checkstream():
    time.sleep(2)
    if _stream.poll() == None:
        return(0)
    else:
        return(1)

def checkReceivestream():
    time.sleep(6)
    if _rcstream.poll() == None:
        return(0)
    else:
        return(1)
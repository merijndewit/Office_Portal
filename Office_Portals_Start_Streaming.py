import subprocess
import os

piCSI = None

def stream():
    global _stream
    _stream = None
    _stream = subprocess.Popen(["gst-launch-1.0","rpicamsrc","preview=False","name=videosrc","bitrate=4000000","!","h264parse","!","video/x-h264,framerate=",vidfps + "/1,","width=",vidwidth,",height=",vidheight,"!","rtph264pay","pt=96","config-interval=5","!","udpsink","host=",ip,"port=5000"], preexec_fn=os.setsid)
    print("started stream for CSI camera")

def stopstream():
    global _stream
    if '_stream' in globals() and hasattr(_stream, 'pid'):
        subprocess.Popen.kill(_stream)
        _stream = None
        print("stream termindated")
    else:
        print("no stream to terminate")
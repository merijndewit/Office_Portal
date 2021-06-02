import subprocess
import os

piCSI = None

def stream():
    global _stream
    _stream = None
    if piCSI is False:
        _stream = subprocess.Popen(["gst-launch-1.0","rpicamsrc","preview=False","name=videosrc","bitrate=4000000","!","h264parse","!","video/x-h264,framerate=20/1,width=1920,height=1080","!","rtph264pay","pt=96","config-interval=5","!","udpsink","host=",ip,"port=5000"], preexec_fn=os.setsid)
        print("started stream for CSI camera")
    elif piCSI is True:
        #_stream = subprocess.Popen(["gst-launch-1.0", "-vv", "-e", "v4l2src", "device=/dev/video0", "!",  "image/jpeg,width=640,height=480", "!", "queue", "!", "jpegdec", "!", "videoconvert", "!", "omxh264enc", "target-bitrate=1000000", "control-rate=variable", "!", "h264parse", "!", "rtph264pay", "config-interval=1", "pt=96", "!", "udpsink", "host=", ip, "port=5000"], preexec_fn=os.setsid)
        print("not available yet")
    else:
        return(0)

def stopstream():
    global _stream
    if '_stream' in globals() and hasattr(_stream, 'pid'):
        subprocess.Popen.kill(_stream)
        _stream = None
        print("stream termindated")
    else:
        print("no stream to terminate")
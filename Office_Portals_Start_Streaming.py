import subprocess
import os
import signal

stream = None
def stream(piCSI):
    global stream
    if piCSI == False:
        p1 = subprocess.Popen(["raspivid", "-t", "999999", "-b", "2000000", "-o", "-",], stdout=subprocess.PIPE)
        stream = subprocess.Popen(["gst-launch-1.0", "-e", "-vvv", "fdsrc", "!", "h264parse", "!", "rtph264pay", "pt=96", "config-interval=5", "!", "udpsink", "host=", ip ,"port=","5000"], stdin=p1.stdout, stdout=subprocess.PIPE, preexec_fn=os.setsid)
        p1.stdout.close()
        print("started stream for CSI camera")
    elif piCSI == True:
        stream = subprocess.Popen(["gst-launch-1.0", "-vv", "-e", "v4l2src", "device=/dev/video0", "!",  "image/jpeg,width=640,height=480", "!", "queue", "!", "jpegdec", "!", "videoconvert", "!", "omxh264enc", "target-bitrate=1000000", "control-rate=variable", "!", "h264parse", "!", "rtph264pay", "config-interval=1", "pt=96", "!", "udpsink", "host=", ip, "port=5000"], stdout=subprocess.PIPE, preexec_fn=os.setsid)
        print("started stream for USB camera")
    else:
        return(0)

def stopstream():
    global stream
    if hasattr(stream, 'pid'):
        os.killpg(os.getpgid(stream.pid), signal.SIGTERM)
        stream = None
    print(stream)
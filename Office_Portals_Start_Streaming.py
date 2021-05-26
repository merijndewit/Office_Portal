import subprocess
import os

piCSI = None

def stream():
    global _stream
    _stream = None
    if piCSI is False:
        _p1 = subprocess.Popen(["raspivid", "-t", "999999", "-b", "2000000", "-o", "-",], stdout=subprocess.PIPE)
        _stream = subprocess.Popen(["gst-launch-1.0", "-e", "-vvv", "fdsrc", "!", "h264parse", "!", "rtph264pay", "pt=96", "config-interval=5", "!", "udpsink", "host=", ip ,"port=","5000"], preexec_fn=os.setsid)
        _p1.stdout.close()
        print("started stream for CSI camera")
    elif piCSI is True:
        _stream = subprocess.Popen(["gst-launch-1.0", "-vv", "-e", "v4l2src", "device=/dev/video0", "!",  "image/jpeg,width=640,height=480", "!", "queue", "!", "jpegdec", "!", "videoconvert", "!", "omxh264enc", "target-bitrate=1000000", "control-rate=variable", "!", "h264parse", "!", "rtph264pay", "config-interval=1", "pt=96", "!", "udpsink", "host=", ip, "port=5000"], preexec_fn=os.setsid)
        print("started stream for USB camera")
    else:
        return(0)

def stopstream():
    global _stream
    #os.killpg(os.getpgid(stream.pid), signal.SIGTERM)

    subprocess.Popen.kill(_stream)
    _p1 = None
    _stream = None

    print("stream termindated")
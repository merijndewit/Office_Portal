import subprocess
import os
import signal


stream = None
def stream():
    global stream
    p1 = subprocess.Popen(["raspivid", "-t", "999999", "-b", "2000000", "-o", "-",], stdout=subprocess.PIPE)
    stream = subprocess.Popen(["gst-launch-1.0", "-e", "-vvv", "fdsrc", "!", "h264parse", "!", "rtph264pay", "pt=96", "config-interval=5", "!", "udpsink", "host=", ip ,"port=","5000"], stdin=p1.stdout, stdout=subprocess.PIPE, preexec_fn=os.setsid)
    p1.stdout.close()
    print("started stream")

def stopstream():
    global stream
    os.killpg(os.getpgid(stream.pid), signal.SIGTERM)
    stream = None
    print("stream stopped")
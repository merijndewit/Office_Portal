import subprocess
import os
import signal

stream = None
def stream():
    global stream
    stream = subprocess.Popen( "raspivid -t 999999 -b 2000000 -o - -n| gst-launch-1.0 -e -vvv fdsrc ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=192.168.1.139 port=5000",
    stdin=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    print("started stream")
    
def stopstream():
    global stream
    os.killpg(os.getpgid(stream.pid), signal.SIGTERM)
    stream = None
    print("stream stopped")
import subprocess

stream = None

def stream():
    global stream 
    stream = subprocess.Popen( "raspivid -t 999999 -b 2000000 -o - -n| gst-launch-1.0 -e -vvv fdsrc ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=192.168.1.139 port=5000",
    stdin=subprocess.PIPE, shell=True )
    
def stopstream():
    global stream
    stream.terminate()
    stream = None
    print("stream stopped")
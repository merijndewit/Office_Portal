import subprocess
import signal
import os

_rcstream = None
def recieveStream(targetpiCSI):
    global _rcstream
    if targetpiCSI == False:
        _rcstream = subprocess.Popen(["gst-launch-1.0", "udpsrc", "port=5000", "!", "application/x-rtp,", "payload=96", "!", "rtpjitterbuffer", "!", "rtph264depay", "!", "avdec_h264", "!", "fpsdisplaysink", "sync=false", "text-overlay=false"], stdout=subprocess.PIPE, preexec_fn=os.setsid)
        print("recieving stream for CSI camera")
    elif targetpiCSI == True:
        _rcstream = subprocess.Popen(["gst-launch-1.0", "udpsrc", "port=5000", "!", "application/x-rtp,", "payload=96", "!", "rtpjitterbuffer", "!", "rtph264depay", "!", "avdec_h264", "!", "fpsdisplaysink", "sync=false", "text-overlay=false"], stdout=subprocess.PIPE, preexec_fn=os.setsid)
        print("recieving stream for USB camera")
    else:
        return(0)

def stopreceivingstream():
    global _rcstream
    subprocess.Popen.kill(_rcstream)
    print(_rcstream)
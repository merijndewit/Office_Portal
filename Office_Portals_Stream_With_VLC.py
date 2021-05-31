import subprocess
import os

piCSI = None

def stream():
    global _stream
    _stream = None
    _stream = subprocess.Popen(['cvlc -v v4l2:///dev/video0:chroma="H264":width=720:height=480:fps=20 --rtsp-timeout 10 --sout="#rtp{sdp=rtsp://:8554/live}" :demux=h264'], shell=True, preexec_fn=os.setsid)


def stopstream():
    global _stream

    subprocess.Popen.kill(_stream)
    _stream = None

    print("stream termindated")
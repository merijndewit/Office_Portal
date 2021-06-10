import subprocess
import os

def installGstreamertools():
    global _stream
    _stream = subprocess.Popen(["sudo apt-get install gstreamer1.0-tools"], shell=True)
    
def installRpicamsrc():
    global _stream
    _stream = subprocess.Popen(["sudo apt-get install autoconf && git clone https://github.com/thaytan/gst-rpicamsrc.git && ./gst-rpicamsrc/autogen.sh --prefix=/usr --libdir=/usr/lib/arm-linux-gnueabihf/ && gst-rpicamsrc/make && sudo gst-rpicamsrc/make install"], shell=True)
    
def installGstreamerdev():
    global _stream
    _stream = subprocess.Popen(["sudo apt-get install autoconf automake libtool pkg-config libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libraspberrypi-dev"], shell=True)
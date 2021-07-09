import subprocess
import os

def installGstreamertools():
    global _install
    _install = subprocess.Popen(["sudo apt-get install -y gstreamer1.0-tools"], shell=True)
    _install.wait()

def installRpicamsrc():
    global _install
    try:
        _install = subprocess.check_call(["git clone https://github.com/thaytan/gst-rpicamsrc.git && cd gst-rpicamsrc && ./autogen.sh --prefix=/usr --libdir=/usr/lib/arm-linux-gnueabihf/ && make && sudo make install"], shell=True)
        _install.wait()
    except subprocess.CalledProcessError:
        _install = subprocess.Popen(["cd gst-rpicamsrc && ./autogen.sh --prefix=/usr --libdir=/usr/lib/arm-linux-gnueabihf/ && make && sudo make install"], shell=True)
        _install.wait()
def installGstreamerdev():
    global _install
    _install = subprocess.Popen(["sudo apt-get install -y autoconf automake libtool pkg-config libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libraspberrypi-dev"], shell=True)
    _install.wait()

def installRaspidmx():
    global _install
    _install = subprocess.Popen(["git clone https://github.com/AndrewFromMelbourne/raspidmx && cd raspidmx && sudo make"], shell=True)
    _install.wait()
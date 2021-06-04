# Office_Portal
Office_Portal
Introduction:
In this time of covid, we work a lot remotely from each other, for example in another space. One can feel lonely here. So we came up with the idea to create an office portal and make it accessible to everyone using Github. With the Office Portal, you can look into another room. With this project, we hope to reduce loneliness in the office by bringing your colleagues a little closer with the help of IT. The GitHub page contains all instructions on how to make an Office Portal yourself, as well as all the necessary code.


How to install:
First, get the latest release of “Raspberry Pi OS with desktop and recommended software”
(https://www.raspberrypi.org/software/operating-systems/)
After you installed raspberry pi os and booted into the os connect to a wifi network and check for updates with:


sudo apt-get update
sudo apt-get upgrade 


Then we have to enable the SPI interface and the camera to do this type:
  

sudo raspi-config


You should see a menu pop up like in the picture. Go to option 3 (interface options). And enable the camera interface and the SPI interface. When you are done click on “Finish” and reboot the pi.












Once we have enabled the camera and SPI interfaces we want to download a plugin for GStreamer so we can use our raspberry pi camera with GStreamer.
Before we can install the plugin we have to install the GStreamer with this command:
sudo apt-get install gstreamer1.0-tools
and we have to install the GStreamer dev packages:
sudo apt-get install autoconf automake libtool pkg-config libgstreamer1.0-dev \
 libgstreamer-plugins-base1.0-dev libraspberrypi-dev
then we clone the plugin from GitHub:
git clone https://github.com/thaytan/gst-rpicamsrc.git




then we go in the directory of the plugin
cd cd gst-rpicamsrc/
and then we install the plugin:
./autogen.sh --prefix=/usr --libdir=/usr/lib/arm-linux-gnueabihf/
make
sudo make install


At this point we are able to stream to the other pi. you can test it with this command:
gst-launch-1.0 rpicamsrc preview=False name=videosrc bitrate=2000000 !        h264parse ! video/x-h264,framerate=25/1,width=1280,height=720 !  rtph264pay pt=96    config-interval=5 ! udpsink host=<target-ip-here> port=5000
You should see something like this after you entered the command above:
  

Now there is an option if you want to make use of the GUI or if you wanna make use of the command line. There are different steps for both methods so go to the option GUI if you want to make use of the GUI. And option Command line if you wanna make use of the command line.


Option GUI:
To use the GUI for office portal we need to install a few dependencies for python that the program uses. To install them we need to type:
        pip3 install PySimpleGui
        pip3 install Netifaces
        pip3 install adafruit-circuitpython-ws2801
        sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
after we installed the dependencies we can clone the office portal from GitHub:
        git clone https://github.com/merijndewit/Office_Portal.git
then we go in the directory of office portal:
        cd Office_Portal/
and we start the program by typing:
        python3 Office_Portals.py
enjoy office portal!




        




Option Command-line:
The GUI automatically makes a .spd file. a .spd file is used to receive the stream so we have to make one manually. To make a .spd file we type:
touch stream.spd
now we’ve created a file named stream.spd, its still empty so we have to edit it by typing:
sudo nano stream.spd
now we have to copy this into the file: 
v=0
m=video 5000 RTP/AVP 96
c=IN IP4 <target-ip-here>
a=rtpmap:96 H264/90000
After u made sure that you’ve replaced <target-ip-here> press ctrl + x. It will ask if we want to save the changes to the file and we type “y” and then press enter. Now we’ve created a .spd file so we can receive the stream. 




How to begin streaming:
GUI:  
the GUI is pretty straightforward.
After you’ve launched the program you have to type the specifications for the stream. you can type the resolution, framerate, and target IP. all boxes have to be filled in correctly otherwise you won’t be able to receive the stream properly or at all. one you’ve filled in all the boxes you can press start streaming on both pi’s. Once you’ve done that you press start receiving stream on both pi’s and then everything should be working!

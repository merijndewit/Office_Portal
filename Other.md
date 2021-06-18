# Welcome to Office Portal!
In this File there are a few other ways to install and use Office Portal than in the readme.
If you didnt like using the GUI or if you encountered a problem you will probably be able to make it work by using one of the guides below.

In this file we have:
- How to install and run (command line only):
- How to install GUI (using shell):
- How to install (for using the source code):


> Note: If you encountered a problem please open an issue in the github page!

# How to install and run (command line only):
First, get the latest release of [Raspberry Pi OS with desktop and recommended software](https://www.raspberrypi.org/software/operating-systems/)

After you installed raspberry pi os and booted into the os connect to a wifi network and check for updates with:

  

	sudo apt-get update && sudo apt-get upgrade

  

Then we have to enable the SPI interface and the camera to do this type:

	sudo raspi-config

  
![](https://lh3.googleusercontent.com/N5ixPNQmhdGdpBPIRT9QnviQ9U4I8VzbxSc9oxz7mwE_Pi2Kz2-xPr5xk3ogaVI8aaA9b6JzIURP9MjG-w-Z-eqWHvUbEroG8IY3Mdf3h1qxTKxCTX9ItYy9goHzbiTeFQV3KtPs)


You should see a menu pop up like in the picture. Go to option 3 (interface options). And enable the camera interface and the SPI interface. When you are done click on “Finish” and reboot the pi.

  ## Installing dependencies

Once we have enabled the camera and SPI interfaces, we want to download a GStreamer plugin to use our raspberry pi camera with GStreamer.

Before we can install the plugin we have to install the GStreamer with this command:

	sudo apt-get install gstreamer1.0-tools

and we have to install the GStreamer dev packages:

	sudo apt-get install autoconf automake libtool pkg-config libgstreamer1.0-dev \ libgstreamer-plugins-base1.0-dev libraspberrypi-dev

then we clone the plugin from GitHub:

	git clone https://github.com/thaytan/gst-rpicamsrc.git

  
  

then we go in the directory of the plugin

	cd gst-rpicamsrc/

and then we install the plugin:

	./autogen.sh --prefix=/usr --libdir=/usr/lib/arm-linux-gnueabihf/

	make

	sudo make install

	cd ..

  

At this point we are able to stream to the other pi. you can test it with this command:

	gst-launch-1.0 rpicamsrc preview=False name=videosrc bitrate=2000000 ! h264parse ! video/x-h264,framerate=25/1,width=1280,height=720 ! rtph264pay pt=96 config-interval=5 ! udpsink host=<target-ip-here> port=5000

You should see something like this after you entered the command above:

  
![](https://lh3.googleusercontent.com/K11dl-RO63gX4hcpiJGiWNg0LWbLXIpSHF0tqAnsYB66hQZ8JSwLVEuVx87M5VYLib-7xKLSCGsFpFvl_or_IsGFBKjLNa50CVfVSGLXOUf3VKCApsDUNPdTjpDq3hyUz8vcHexB)

To stop the stream you can precc ctrl and c.

## Creating a .spd file
The GUI automatically makes a .spd file. a .spd file is used to receive the stream so we have to make one manually. To make a .spd file we type:

	touch stream.spd

now we’ve created a file named stream.spd, its still empty so we have to edit it by typing:

	sudo nano stream.spd

now we have to copy this into the file:

	v=0

	m=video 5000 RTP/AVP 96

	c=IN IP4 target-ip-here

	a=rtpmap:96 H264/90000

After u made sure that you’ve replaced **target-ip-here** press ctrl + x. It will ask if we want to save the changes to the file and we type “y” and then press enter. Now we’ve created a .spd file so we can receive the stream.

## Sending and Receiving
Now we want to send and receive the stream. First we want to stream from both PIs and then receive from both PIs.

To send the stream we enter:

	gst-launch-1.0 rpicamsrc preview=False name=videosrc bitrate=2000000 ! h264parse ! video/x-h264,framerate=25/1,width=1280,height=720 ! rtph264pay pt=96 config-interval=5 ! udpsink host=target-ip-here port=5000

Don't forget to change **target-ip-here**.

For receiving the stream we want to do to the directory of the .spd file we've just created. Then enter on both PIs:

	omxplayer --live stream.spd

Now the PI's should be streaming video and receiving video from eachother!

# How to install GUI (using shell):
The shell script will install all the dependencies you need using Office Portal. When you install it via the shell you are also able to run the uncompiled source code. 


First, get the latest release of [Raspberry Pi OS with desktop and recommended software](https://www.raspberrypi.org/software/operating-systems/)

After you installed raspberry pi os and booted into the os connect to a wifi network and check for updates with:

  

	sudo apt-get update && sudo apt-get upgrade

  

Then we have to enable the SPI interface and the camera to do this type:

	sudo raspi-config

  
![](https://lh3.googleusercontent.com/N5ixPNQmhdGdpBPIRT9QnviQ9U4I8VzbxSc9oxz7mwE_Pi2Kz2-xPr5xk3ogaVI8aaA9b6JzIURP9MjG-w-Z-eqWHvUbEroG8IY3Mdf3h1qxTKxCTX9ItYy9goHzbiTeFQV3KtPs)


You should see a menu pop up like in the picture. Go to option 3 (interface options). And enable the **camera interface** and the **SPI interface**. When you are done click on **Finish** and reboot the pi.

Then we have to clone Office_Portal from GitHub:

	git clone https://github.com/merijndewit/Office_Portal.git

	git clone https://github.com/thaytan/gst-rpicamsrc.git

Then we have to type:

	sudo chmod +x Office_Portal/Shell/Install_Office_Portal

To run the shell script we type:

	sudo ./Office_Portal/Shell/Install_Office_Portal

Sometimes the program asks if you want to continue, just press **y** on your keyboard, and the program will continue.

After the script is done Office Portal should launch automatically.

Enjoy Office Portal!


# How to install (for using the source code):
If you want run Office Portal from the source code then you need to install a few dependencies.

First, get the latest release of [Raspberry Pi OS with desktop and recommended software](https://www.raspberrypi.org/software/operating-systems/)

After you installed raspberry pi os and booted into the os connect to a wifi network and check for updates with:

  

	sudo apt-get update && sudo apt-get upgrade

  

Then we have to enable the SPI interface and the camera to do this type:

	sudo raspi-config

  
![](https://lh3.googleusercontent.com/N5ixPNQmhdGdpBPIRT9QnviQ9U4I8VzbxSc9oxz7mwE_Pi2Kz2-xPr5xk3ogaVI8aaA9b6JzIURP9MjG-w-Z-eqWHvUbEroG8IY3Mdf3h1qxTKxCTX9ItYy9goHzbiTeFQV3KtPs)


You should see a menu pop up like in the picture. Go to option 3 (interface options). And enable the camera interface and the SPI interface. When you are done click on “Finish” and reboot the pi.

  ## Installing dependencies

Once we have enabled the camera and SPI interfaces, we want to download a GStreamer plugin to use our raspberry pi camera with GStreamer.

Before we can install the plugin we have to install the GStreamer with this command:

	sudo apt-get install gstreamer1.0-tools

and we have to install the GStreamer dev packages:

	sudo apt-get install autoconf automake libtool pkg-config libgstreamer1.0-dev \ libgstreamer-plugins-base1.0-dev libraspberrypi-dev

then we clone the plugin from GitHub:

	git clone https://github.com/thaytan/gst-rpicamsrc.git

  
  

then we go in the directory of the plugin

	cd gst-rpicamsrc/

and then we install the plugin:

	./autogen.sh --prefix=/usr --libdir=/usr/lib/arm-linux-gnueabihf/

	make

	sudo make install

	cd ..

## Python dependencies
Now we need to install a few dependencies for python that the program uses. To install them we need to type:

	pip3 install PySimpleGui

	pip3 install Netifaces

	pip3 install adafruit-circuitpython-ws2801

	sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel

after we installed the dependencies we can clone the office portal from GitHub:

	git clone https://github.com/merijndewit/Office_Portal.git

then we go in the directory of office portal:

	cd Office_Portal/GUI

and we start the program by typing:

	python3 Office_Portal/Source_Office_Portal/main_Office_Portal.py

enjoy office portal!

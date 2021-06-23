# Welcome to Office Portal!

In this time of covid, we work a lot remotely from each other, for example in another space. One can feel lonely here. So we came up with the idea to create an office portal and make it accessible to everyone using Github. With the Office Portal, you can look into another room. With this project, we hope to reduce loneliness in the office by bringing your colleagues a little closer with the help of IT. The GitHub page contains all instructions on how to make an Office Portal yourself, as well as all the necessary code.

# Installing
We have multiple ways for installing Office Portal on your raspberry pi. The reccomended way is using the GUI. Its is really simple to install and only requires a few steps. But if you want to use/install Office Portal in a diffirent way then you can! We made a diffirent file for other ways of using/installing Office Portal [here](https://github.com/merijndewit/Office_Portal/blob/main/Other.md). If you are happy using the GUI then continue to **Installing GUI**. 

# Installing Office Portal (GUI)
These steps below will guide you with installing office portals. First we are going to enable a few things in raspi-config and then we are going to clone the github project and run it!

First, get the latest release of [Raspberry Pi OS with desktop and recommended software](https://www.raspberrypi.org/software/operating-systems/)

After you installed raspberry pi os and booted into the os connect to a wifi network and check for updates with:

  

	sudo apt-get update && sudo apt-get upgrade

  

Then we have to enable the SPI interface and the camera to do this type:

	sudo raspi-config
  
![](https://lh3.googleusercontent.com/N5ixPNQmhdGdpBPIRT9QnviQ9U4I8VzbxSc9oxz7mwE_Pi2Kz2-xPr5xk3ogaVI8aaA9b6JzIURP9MjG-w-Z-eqWHvUbEroG8IY3Mdf3h1qxTKxCTX9ItYy9goHzbiTeFQV3KtPs)

You should see a menu pop up like in the picture. Go to option 3 (interface options). And enable the camera interface and the SPI interface. When you are done click on “Finish” and reboot the pi.

  
Then we clone the project from github:

	git clone https://github.com/merijndewit/Office_Portal.git

After weve cloned the project we want to go to the executable:

	 cd Office_Portal/GUI/OfficePortal-0.1/
And start it:

	 ./main_Office_Portal 


Then Office Portal should launch and you can use the GUI!

# Using Office_Portal (GUI)
Once the GUI aplication of Office Portal has started we can see an instrduction screen. we can navigate through the pages with the arrow buttons on the bottom of the page, we can also exit the application by pressing on the ![](https://lh5.googleusercontent.com/qodMuUYRw6y9x0WXSMwhKf-ZAojzPM1lCM52Kvmn75560lSEYFjUx3Bp_xZyysHJOhWI725JOtboAflUWQ9DH3U2uC7x-_gL1oCRDz2QaHu1G_qEGMHmDwnfQ42YzawHteMh_hna) button.

## Dependencies
Once we go to the next page from the introduction page we can see all the dependencies that need to be installed. Click on the **check** button. if you see a **green check** next to the button you've just clicked then the dependency is installed. if you see a **download button** next to the button you've just clicked then the dependency is nit yet installed and it needs to be installed. To install it is really easy you just have to click on the **download button** and the program will install it for you. It can take a bit until its installed (approx 5 min) when the **download button** dissapeares the dependency has been installed. You can press check gain if you want to make sure the dependency has been installed correctly. 

## Options
In the option page we can change the stream specifications. You can change the resolution of the stream and framerate that you are sending to the other pi.

We also have an option for the portal ring. We can use the portal ring to make our portal look more like a portal. We can use an LED strip or a digital mask. If you dont want either of those you can click on **None** and continue to the next page. If you want to make use of an on-screen mask or LED strip then you can select **blue** or  **orange** depending wich color you want the mask/ledstrip to be of the portal. If you want to make use of an on-screen mask, example:

![](https://lh5.googleusercontent.com/X2p26R8XaFDW5qQZAvL3D1nfS4F5fgQ2VNSqUXmALaSQMEybxWikpIITuIYjHFoxezHeKY6f5l1cJ_QrcdaU0CRgtlsF1QLjLHCt0Rb7rjFzXMHfuhUoxevKXVNb15VyGmH3Yyw2)

Then you can select **Texture**. When you click on the button **Texture Settings** a menu opens with more options. The first option is the resolution (default is 1080p). If you have a 720p resolution screen then select **720p**. If you have a monitor with a diffirent resolution than 1080/720p or you want to use your a custom on-screen digital mask then cluck the checkbox and click on **Browse** and select your custom mask. 
>Note: Only .PNG is supported another filetype will not work.

If you want to use an LED strip then select **Ledstrip**. When you click on the button **Ledstrip Settings** a menu opens with extra settings. Here you can adjust the brightness of the led's. If you want to use a custom color for the LED strip select the checkbox and in the boxes below enter the Decimal RGB code. The first box is the red value, the second green and the third is blue. The values go from 0-255.
When you entered the options you want you can continue to the next page.
 

## Advanced Options
Here you can change the bitrate and port of the stream you are sending. 
You do not have to change the settings, only when you encounter a problem.

>Note: the port has to be the same on both PIs otherwise you may encounter problems
## Connect to other PI
Here we can see the ip address of this pi. When you are on the same screen on the other pi we need to enter this pis ip ino the **textbox** of the other pi's ip. then with the other pi we need to fill its ip into the **textbox**. once youve done that we can go to the final page!

## Stream and Receive
When you are on this page on **both PIs** we are ready to click receive on both pis. When we click on **Ready** the pi will try to receive the stream of the other pi. When you've clicked **Ready** on both pis the portal should be open! 

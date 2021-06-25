# Welcome to Office Portal!

In this time of covid, we work a lot remotely from each other, for example in another space. One can feel lonely here. So we came up with the idea to create an office portal and make it accessible to everyone using Github. With the Office Portal, you can look into another room. With this project, we hope to reduce loneliness in the office by bringing your colleagues a little closer with the help of IT. The GitHub page contains all instructions on how to make an Office Portal yourself, as well as all the necessary code.

# Installing

We have multiple ways for installing Office Portal on your raspberry pi. The recommended way is to use the GUI. It is really simple to install and only requires a few steps. But if you want to use/install Office Portal in a different way then you can! We made a different file (because it is so long) for other ways of using/installing Office Portal [here](https://github.com/merijndewit/Office_Portal/blob/main/Other.md). If you are happy using the GUI then continue to **Installing GUI**.

# Installing Office Portal (GUI)

The steps below will guide you in installing office portals. First, we are going to enable a few things in raspi-config and then we are going to clone the GitHub project and run it!

First, get the latest release of [Raspberry Pi OS with desktop and recommended software](https://www.raspberrypi.org/software/operating-systems/)

After you installed raspberry pi os and booted into the os connect to a wifi network and check for updates with:

	sudo apt-get update && sudo apt-get upgrade

Then we have to enable the SPI interface and the camera to do this type:

	sudo raspi-config

![](https://lh3.googleusercontent.com/N5ixPNQmhdGdpBPIRT9QnviQ9U4I8VzbxSc9oxz7mwE_Pi2Kz2-xPr5xk3ogaVI8aaA9b6JzIURP9MjG-w-Z-eqWHvUbEroG8IY3Mdf3h1qxTKxCTX9ItYy9goHzbiTeFQV3KtPs)

You should see a menu pop up like in the picture. Go to option 3 (interface options). And enable the camera interface and the SPI interface. When you are done click on “Finish” and reboot the pi.

Then we clone the project from GitHub:

	git clone https://github.com/merijndewit/Office_Portal.git

After we've cloned the project we want to go to the directory of the executable:

	cd Office_Portal/GUI/OfficePortal-0.1/

And start it:

	./main_Office_Portal

Then Office Portal should launch and you can use the GUI!

  

# Using Office_Portal (GUI)

Once the GUI application of Office Portal has started we can see an instruction screen. we can navigate through the pages with the arrow buttons on the bottom of the page, we can also exit the application by pressing on the ![](https://lh5.googleusercontent.com/qodMuUYRw6y9x0WXSMwhKf-ZAojzPM1lCM52Kvmn75560lSEYFjUx3Bp_xZyysHJOhWI725JOtboAflUWQ9DH3U2uC7x-_gL1oCRDz2QaHu1G_qEGMHmDwnfQ42YzawHteMh_hna) button.

  

## Dependencies

Once we go to the next page from the introduction page we can see all the dependencies that need to be installed. Click on the **check** button. if you see a **green check** next to the button you've just clicked then the dependency is installed. if you see a **download button** next to the button you've just clicked then the dependency is not yet installed and it needs to be installed. To install it is really easy you just have to click on the **download button** and the program will install it for you. It can take a bit until it’s installed (approx 5 min) when the **download button** disappears the dependency has been installed. You can press check gain if you want to make sure the dependency has been installed correctly.

## Options

On the options page, we can change the stream specifications. You can change the resolution of the stream and framerate that you are sending to the other pi.

We also have an option for the portal ring. We can use the portal ring to make our portal look more like a portal. We can use an LED strip or a digital mask. If you don’t want either of those you can click on **None** and continue to the next page. If you want to make use of an on-screen mask or LED strip then you can select **blue** or **orange** depending which color you want the mask/led strip to be of the portal. If you want to make use of an on-screen mask, for example:

![](https://lh4.googleusercontent.com/fTpMh55sUaVGSj0Lq7JHZtf2fOemiq-XaMOdPv3cz7747RRMTX-LyzBzjqQ03MI9pQcUK-kqBYx5FkxrgffkFeEEbTPRar3UJcl6CH5iBSYow7PKM5WnF8w3Y-Ad5RkRlLdedhgj)  
  
  
**
  

Then you can select **Texture**. When you click on the button **Texture Settings** a menu opens with more options. The first option is the resolution (default is 1080p). If you have a 720p resolution screen then select **720p**. If you have a monitor with a different resolution than 1080/720p or you want to use a custom on-screen digital mask then click the checkbox and click on **Browse** and select your custom mask.

>Note: Only .PNG is supported another file type will not work.

  

If you want to use an LED strip then select **Ledstrip**. When you click on the button **Ledstrip Settings** a menu opens with extra settings. Here you can adjust the brightness of the leds. If you want to use a custom color for the LED strip select the checkbox and in the boxes below enter the Decimal RGB code. The first box is the red value, the second green, and the third is blue. The values go from 0-255.

When you entered the options you want you can continue to the next page.

  

## Advanced Options

Here you can change the bitrate and port of the stream you are sending.
You do not have to change the settings, only when you encounter a problem.

>Note: the port has to be the same on both PIs otherwise you may encounter problems

## Connect to other PI

Here we can see the IP address of this pi. When you are on the same screen on the other pi we need to enter this pis IP into the **textbox** of the other pi's IP. then with the other pi, we need to fill its IP into the **textbox**. once you’ve done that we can go to the final page!

## Stream and Receive

When you are on this page on **both PIs** we are ready to click receive on both pis. When we click on **Ready** the pi will try to receive the stream of the other pi. When you've clicked **Ready** on both pis the portal should be open!

## Load config file

To make things easier for the next time using Office Portal you can click on the button **Load settings** on the first page of the program. This will look if you run the program once before. If you see "no config file found" next to the button then you cant load the config file. If a button appears that says "Load config" then you can click on it to load the previous configuration. It will take you directly to the **Stream and Receive** page

# Hardware
There are a lot of options for the hardware. In every category down here are things you need to look out for buying/using materials for the project.
If you want/need to buy all the materials its is going to cost you arround this:
|minimal         |Estimated price: |                     
|----------------|-----------------|
|Raspberry PI|        35€       
|Monitor/Television|     99€              
|Camera| 10€
|Cables and adapters| 20€
|Total:|164€

>Note: Dont forget that you need to multiple the price by 2, because you need 2 portals

|extensive       |Estimated price: |                     
|----------------|-----------------|
|Raspberry PI|35€       
|Monitor/Television|99€              
|Camera|10€
|LED strip|5€
|MDF Sheet|8€
|Paint/Sticker for MDF sheet| 10€
|Cables and adapters| 20€
|Total:|187€
>Note: Dont forget that you need to multiple the price by 2, because you need 2 portals

There are a lot of options for the hardware. To make sure that you are picking the right materials for the project, We wrote down what is required/reccomended for the project. 
## Raspberry PI
For the raspberry pi we have a lot of options. For this project ive tested the raspberry pi 4B, 3B+ and the zero w. The zero w was not powerfull enough for this project when testing, thats why i do not advertise using it or this project. 
Down here are the results from the test i did. with the pi 3B+ and pi 4B:
  
|                |Raspberry PI 3B+ |Raspberry PI 4B                     
|----------------|-----------------|---------------|
|1080p / 30fps|**X**       |✔           
|1080p / 20fps|✔           |✔           
|730p / 45fps |**X**	   |✔
|730p / 30fps | ✔     	   |✔

The PI 3B+ is not compatible with all resolutions because it has a hard time keeping up with the stream. This can result in a delay. The raspberry pi 4 is obviously the best choice for video quality. But if you dont mind a lower framerate or resolution then the pi 3B+ is the cheaper option. Just pick whichever you prefer!

## Monitor/Television
Its best for the Monitor/Television to be the same size. Otherwise it can look a bit odd if one portal is bigger than the other. We reccomend not choosing a resolution greater than 1080p, a higher resolution Monitor/Television is usually more expensive and the pi's cant handle a higher resolution than 1080p. The aspect ratio is also an important one. **16:9** and **4:3** is highly reccomended. The most important is that the Camera has to support that aspect ratio most camera modules for the raspberry pi can support 16:9 and 4:3, But make sure to check the documentation of that camera. If you do have a diffirent aspect ratio it can result in black bars on the screen or stretching (something you dont want). Also an important one is to be sure you can remove the foot of the Monitor/Television, also the flatter the better because you want to try to hide the Monitor/Television. 

>Note: The Monitor/Television is the most expensive part of the project, so maybe you can find a Monitor/Television at a second hand store. Or maybe at an online marketplace like ebay. This will bring the cost of the project down a lot! Just remember all the points written above!



## Camera
For this project only camera modules with CSI interface is supported. The CSI camera module is directly connected to the GPU, this means the cpu usage is really low using a CSI camera compared to an USB device. Camera modules are also really cheap (the cheapest ones arround 5€). Another advantage is that camera modules are really small so they are less noticable/easyer to hide.

A few important things to note when you are looking for a CSI camera is that you choose one that supports the aspect ratio of your television. Otherwise this can cause problems so make sure you check the documentation of the camera module. Also some camera's dont have their full fov when using 1080p. When you are using a camera module that is not using full fov then the video looks zoomed in you dont want this because it can look weird and you wont be able to see as much of the other room.

Some great documentation of the pi camera's can be found[Here](https://picamera.readthedocs.io/en/release-1.3/fov.html)

## Mask (optional)
If you want the portal to look as much as a portal then making a mask over the monitor/television is the best option. You can also combine it with an LED strip to make it even more special. You can make the mask as large or larger than the television. Below here is an example:
  
![](https://lh3.googleusercontent.com/qC-AriLLLJQyNeIzerTfIMCpIxaYq90gM5C05NwUfxgkgLpmzLxg1wMssx-HUAqA_D6cW7McOYKudOhqy0jdOms4DcYxBIy5YgNLQB1i3sV8ifEGsFy3GNJtHyHn0MP-4O1GvpVB)
If you want the portal to look like a portal from the game Portal then you can 



![](https://lh6.googleusercontent.com/iYh2_nIJ2SPGjofidpz-UiyobAopU85CWIAEa6G-duTu6ZzFpmKHvtRNHZQ1cWGnBXgWKBZYpq-LRP8Lm1W1QoUJ0oMZrjr8K6dN-u7_rF_s-1zd37K2Ur5LHZeYqhiKIlDEEKsj)**
## LED strip (optional)

#In this file we check if the required dependencies are installed
from subprocess import check_output
import os
import time

def checkGstreamer():
    #check if gstreamer is installed
    global _checkGstreamer
    #_checkGstreamer = subprocess.Popen(["sudo apt show gstreamer1.0-tools"], shell=True, preexec_fn=os.setsid, stdout=subprocess.PIPE)
    out = check_output(["sudo", "apt", "show", "gstreamer1.0-tools"])
    encoding = 'utf-8'
    encodedOutput = (str(out, encoding))
    o = encodedOutput.find("Version") #here we look in the output for "Version" because it will only show when gstreamer is installed and that is what we want to know
    if o != -1:
        #print("gstreamer is installed")
        return(1)
    else:
        #print("gstreamer is not installed")
        return(0)

def checkRpicamsrc():
    #check if rpicamsrc is installed
    global _checkGstreamer
    out = check_output(["gst-inspect-1.0", "rpicamsrc"])
    encoding = 'utf-8'
    encodedOutput = (str(out, encoding))
    o = encodedOutput.find("Version") #here we look in the output for "Version" because it will only show when rpicamsrc is installed and that is what we want to know
    if o != -1:
        #print("rpicamsrc is installed")
        return(1)
    else:
        #print("rpicamsrc is not installed")
        return(0)
 


 
checkRpicamsrc()
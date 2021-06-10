#In this file we check if the required dependencies are installed
from subprocess import check_output
import os
import time

def checkGstreamer():
    #check if gstreamer is installed
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
    try:
        out = check_output(["gst-inspect-1.0", "rpicamsrc"])
        if out == "No such element or plugin 'rpicamsrc'":
            return(0)
        else:
            encoding = 'utf-8'
            encodedOutput = (str(out, encoding))
            o = encodedOutput.find("Version") #here we look in the output for "Version" because it will only show when rpicamsrc is installed and that is what we want to know
        if o != -1:
            #print("rpicamsrc is installed")
            return(1)
        else:
            #print("rpicamsrc is not installed")
            return(0)
    except:
        return(0)
def checkGstreamerdev():
    #check if gstreamerdev is installed
    out = check_output(["dpkg -l | grep gstreamer"], shell = True)
    encoding = 'utf-8'
    encodedOutput = (str(out, encoding))
    o = encodedOutput.find("libgstreamer-plugins-base1.0-dev") #here we look in the output for "Version" because it will only show when rpicamsrc is installed and that is what we want to know
    if o != -1:
        print("gstreamerdev is installed")
        return(1)
    else:
        print("gstreamerdev is not installed")
        return(0)






 
checkGstreamerdev()
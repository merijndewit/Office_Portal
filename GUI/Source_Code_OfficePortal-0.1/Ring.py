import subprocess


def makeTexture():
    global _install
    _install = subprocess.Popen(["./raspidmx/pngview/pngview -b 0 -l 3 Office_Portal/GUI/Source_Code_OfficePortal-0.1/Pictures/test.png"], shell=True, cwd='/home/pi/')
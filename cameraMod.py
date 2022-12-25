import os
from picamera import PiCamera
from time import sleep

"""
------------ Setup Vars ------------
"""
# Time taken for Pi Camera to intialise
camInitTime = 2

outputFolder = "Output/"

# Image file output name
imgOutput = outputFolder + "img.jpg"

# Main object for camera
camera = PiCamera()

"""
------------- Main Code -------------
"""
def init():
    if os.path.isdir(outputFolder):
        pass
    else:
        os.mkdir(outputFolder)

def main():
    camera.resolution = (1920, 1080)
    camera.vflip = True
    camera.hflip = True
    camera.contrast = 10
    sleep(camInitTime)
    camera.capture(imgOutput)

if __name__ == '__main__':
    init()
    main()

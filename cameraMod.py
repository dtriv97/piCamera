import os
from picamera import PiCamera
from fractions import Fraction
from time import sleep

"""
------------ Setup Vars ------------
"""
# Time taken for Pi Camera to intialise
camInitTime = 2

outputFolder = "Output/"

# Image file output name
imgOutput = outputFolder + "img.jpg"

"""
------------- Main Code -------------
"""
def init(initType: str = None) -> PiCamera:
    if os.path.isdir(outputFolder):
        pass
    else:
        os.mkdir(outputFolder)

    camera = PiCamera()

    # Common camera settings for all mode types
    camera.resolution = (1920, 1080)
    camera.contrast = 10
    camera.hflip = True
    camera.vflip = True
    sleep(5)

    # Special parameters for long exposure image
    if initType == 'longExpo':
        camera.framerate = Fraction(1, 30)
        camera.sensor_mode = 3
        camera.shutter_speed = 500000
        camera.iso = 400
        camera.exposure_mode = 'off'
        sleep(30)

    return camera

def captureImage(camera):
    camera.capture(imgOutput)
    print("Image captured")
    sleep(6)
    camera.close()
    print("Camera closed")

def main():
    camera = init('longExpo')
    captureImage(camera)

if __name__ == '__main__':
    main()

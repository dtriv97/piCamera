import os
from picamera import PiCamera
from fractions import Fraction
from time import sleep

class CameraMod():
    # Default Vars
    outputFolder = "Output/"
    imgOutput = outputFolder + "img.jpg"
    closeDelay = 6

    def __init__(self, initType: str = None, outputName: str = None):
        if os.path.isdir(self.outputFolder):
            pass
        else:
            os.mkdir(self.outputFolder)
        
        # Set image file name to 'outputName' if given
        if outputName:
            self.imgOutput = outputName

        self.camera = PiCamera()

        # Common camera settings for all mode types
        self.camera.resolution = (1920, 1080)
        self.camera.contrast = 10
        self.camera.hflip = True
        self.camera.vflip = True
        delayTime = 5

        # Special parameters for long exposure image
        if initType == 'longExpo':
            self.camera.framerate = Fraction(1, 30)
            self.camera.sensor_mode = 3
            self.camera.shutter_speed = 1000000
            self.camera.iso = 400
            self.camera.exposure_mode = 'off'
            delayTime = 30

        sleep(delayTime)
    
    def takeImage(self):
        self.camera.capture(self.imgOutput)
        print("Image captured")
        sleep(self.closeDelay)
        self.camera.close()
        print("Camera closed")

def main():
    cam = CameraMod()
    cam.takeImage()

if __name__ == '__main__':
    main()

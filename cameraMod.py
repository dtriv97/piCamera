from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.vflip = True
camera.hflip = True
camera.contrast = 10

time.sleep(2)
camera.capture("img.jpg")

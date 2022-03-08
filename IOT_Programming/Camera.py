from picamera import PiCamera
import time

camera = PiCamera()
#camera.resolution = (2592, 1944) # 최대 해상도 2592 x 1944

camera.resolution = (1024, 768) # 해상도 1024 x 768
time.sleep(2)
camera.capture('example.jpg')
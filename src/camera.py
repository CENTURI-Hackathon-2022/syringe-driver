from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/mathias/Desktop/video.h264')
sleep(60)
camera.stop_recording()
camera.stop_preview()
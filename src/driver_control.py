import time
import serial
from gpiozero import LightSensor, LED, Button
from signal import pause
from serial import SerialException
import sys
from picamera import PiCamera
from time import sleep


def_wait_time = 7
syringe_len_mm = None
limit_len_mm = None
camera = PiCamera()

def stop_movement():
    pass

def set_soft_limit_mm(ser, val):
    ser.write(f"$130={val}\n".encode('utf-8'))
    time.sleep(def_wait_time)

def move_range(ser, range_mm, feed_rate):
    # $J=X10.0 Y-1.5 F100
    ser.write(f"$J=X{range_mm} F{feed_rate}\n".encode('utf-8'))
    time.sleep(def_wait_time)

def print_answer(self):
        ans = b''
        while ans == b'':
            ans = self.arduino.readline()
        line = ans.decode('utf-8').rstrip()
        print(line)
        if line[:5] == 'error' or line[:5]=='ALARM':
            print('Error, stopping program.')
            exit
        return line

def fill():
    pass
    
def move_z(ser, valx, valy):
    ser.write(f"g0x{valx}y{valy}\n".encode('utf-8'))
    time.sleep(def_wait_time)

if __name__ == '__main__':
    # Arduino Setup
    ser = ser = serial.Serial('/dev/ttyACM0', 115200)
    time.sleep(2)
    ser.reset_input_buffer()
    # Unlock
    ser.write(b"$H\n")
    time.sleep(def_wait_time)
    # Set absolute position mode
    ser.write(b"g91\n")
    time.sleep(def_wait_time)
    # Set soft limit
    camera.start_preview()
    camera.start_recording('/home/mathias/Desktop/video.h264')
    move_z(ser, 70, 60)
    move_z(ser, 20, 15)
    move_z(ser, 50, 0)
    move_z(ser, 10, 30)
    camera.stop_recording()
    camera.stop_preview()


    def setup(self):
        # Setup components connected to Raspberry Pi
        self.bottom_limit_switch = Button(3)
        self.bottom_limit_switch.when_pressed = self.stop_movement
        # Setup Arduino connected via self.arduinoial
        self.arduino = serial.Serial('/dev/ttyACM0', 115200)
        time.sleep(2)
        self.arduino.reset_input_buffer()
        # self.print_answer()
        # Unlock
        self.arduino.write(b"$X\n")
        time.sleep(self.default_wait_time)
        self.print_answer()
        # Set absolute position mode
        self.arduino.write(b"g91\n")
        time.sleep(self.default_wait_time)
        self.print_answer()
        # Set soft limit to default
        self.set_soft_limit_mm(self.limit_len_mm)
        self.print_answer()
        print('SETUP DONE')

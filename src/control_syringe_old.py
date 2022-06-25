"""
Syringe Driver code.
"""

# Module import
import time
import serial
from gpiozero import Button

class SyringeDriver:
    def __init__(self):
        self.arduino = None
        self.cal_factor = None
        self.default_wait_time = 1 # seconds
        self.syringe_len_mm = 100
        self.fill_speed = 100
        self.limit_len_mm = 200
        self.setup()
    
    def setup(self):
        # Setup components connected to Raspberry Pi
        self.bottom_limit_switch = Button(3)
        self.bottom_limit_switch.when_pressed = self.stop_movement
        # Setup Arduino connected via self.arduinoial
        self.arduino = serial.Serial('/dev/ttyACM0', 115200)
        time.sleep(2)
        self.arduino.reset_input_buffer()
        # Unlock and move home
        self.move_to_home()
        # Set absolute position mode
        self.arduino.write(b"g91\n")
        time.sleep(self.default_wait_time)
        # Set soft limit to default
        self.set_soft_limit_mm(self.limit_len_mm)
    
    def change_arduino_config(self, param_id, value):
        self.arduino.write(f"${param_id}={value}\n".encode('utf-8'))
        time.sleep(self.default_wait_time)
    
    def set_soft_limit_mm(self, soft_limit_value):
        self.change_arduino_config(130, soft_limit_value)
    
    def ml_to_mm(self, volume):
        """
        volume: in ml
        cal_factor: in mm/ml
        """
        return volume * self.cal_factor
    
    def move_to_home(self):
        self.arduino.write(b"$H\n")
        time.sleep(self.default_wait_time)
    
    def move_x(self):
        self.arduino.write(f"g0x{val}\n".encode('utf-8'))
        time.sleep(self.default_wait_time)
    
    def jogg_x(self, range_mm, feed_rate):
        # $J=X10.0 Y-1.5 F100
        self.arduino.write(f"$J=X{range_mm} F{feed_rate}\n".encode('utf-8'))
        time.sleep(self.default_wait_time) 
    
    def stop_movement(self):
        self.arduino.write(b"\x85\n")
        time.sleep(self.default_wait_time)
    
    def empty_syringe(self):
        self.move_to_home()
    
    def fill_syringe(self, syringe_len_mm, ):
        self.jogg_x(self.syringe_len_mm, self.fill_speed)
    
    def purge_air(self):
        self.fill_syringe(self.syringe_len_mm)
        time.sleep(self.default_wait_time)
        self.empty_syringe()

if __name__ == '__main__':
    sd = SyringeDriver()
    sd.jogg_x(100, 100)
    while True:
        if sd.arduino.in_waiting > 0:
            line = sd.arduino.readline().decode('utf-8').rstrip()
            print(line)
    
    
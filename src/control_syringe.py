"""
Syringe Driver code.

Note: We have tested two syringes, which have different calibration factor and speed.

Syringe 1 (the bigger one)
calibration_factor = 6.7 [ml to mm]
volume_deliver_speed = 10 [%]

Syringe 2 (the smaller one)
calibration_factor
volume_deliver_speed
"""

# Module import
import time
import serial
from gpiozero import Button

class SyringeDriver:
    def __init__(self):
        self.arduino = None
        self.default_wait_time = 1 # seconds
        self.limit_len_mm = 200
        self.home_coordinate = -199
        # Params for 10 mL syringe
        # self.cal_factor = 6.7
        # self.syringe_len_mm = 100
        # self.fill_speed = 100
        # self.volume_deliver_speed = 10
        # Params for 1 mL syringe
        self.cal_factor = 60
        self.syringe_len_mm = 100
        self.fill_speed = 100
        self.volume_deliver_speed = 10
        self.setup()
    
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
        self.print_answer()
    
    def move_x(self, value):
        self.arduino.write(f"g0x{value}\n".encode('utf-8'))
        time.sleep(self.default_wait_time)
        self.print_answer()
    
    def jogg_x(self, range_mm, feed_rate):
        # $J=X10.0 Y-1.5 F100
        self.arduino.write(f"$J=X{range_mm} F{feed_rate}\n".encode('utf-8'))
        time.sleep(self.default_wait_time)
        self.print_answer()
    
    def stop_movement(self):
        self.arduino.write(b"\x85\n")
        time.sleep(self.default_wait_time)
    
    def empty_syringe(self):
        self.move_to_home()
    
    def fill_syringe(self, volume=1):
        distance = self.ml_to_mm(volume)
        self.jogg_x(distance, self.fill_speed)
    
    def purge_air(self):
        self.fill_syringe()
        time.sleep(20)
        self.empty_syringe()

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

    def wait_idle(self):
        tic = time.time()
        self.arduino.write(b"?\n")
        ans = self.print_answer()
        print(ans[1:5])
        wait_time = 0
        while(ans[1:5]!='Idle' and wait_time < 60):
            wait_time = time.time()-tic
            self.arduino.write(b"?\n")
            ans = self.print_answer()
            print(ans[1:5])
        if wait_time >= 60:
            print('Wait time surpassed limit 60 s.')
    
    def get_current_state(self):
        self.arduino.write(b"?\n")
        ans = self.print_answer().strip('<>').split('|')
        print(ans)
        out_dict = {}
        out_dict['status'] = ans[0]
        for group in ans[1:]:
            key, val = group.split(':')
            out_dict[key] = val
        return out_dict
        
    def get_home_coordinate(self):
        ''' gets the x coordinate of home position'''
        self.move_to_home()
        time.sleep(2)
        params_dict = self.get_current_state()
        # print(params_dict)
        try:
            home_pos = float(params_dict['MPos'].split(',')[0])
            return home_pos
        except:
            print('There is no key MPos in the dictionary')
            exit

    def deliver_volume(self, volume):
        ''' 
        delivers volume in milliliters [ml]
        computes distance in millimiters [mm]
        here 1 ml = calibration_factor mm 
        '''
        if not self.cal_factor:
            print('No calibration factor defined!!!')
        else:
            distance = self.ml_to_mm(volume)
            self.jogg_x(-1 * distance, self.volume_deliver_speed)

if __name__ == '__main__':
    sd = SyringeDriver()
    # Test for 10 mL syringe
    # sd.fill_syringe(2)
    # time.sleep(20)
    # sd.deliver_volume(1)
    # Test for 1 mL syringe
    sd.fill_syringe(0.1)
    time.sleep(20)
    sd.deliver_volume(0.1)
    while True:
        if sd.arduino.in_waiting > 0:
            line = sd.arduino.readline().decode('utf-8').rstrip()
            print(line)
    
    
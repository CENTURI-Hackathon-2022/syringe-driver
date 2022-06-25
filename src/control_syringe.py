from cgitb import reset
import time
from tracemalloc import reset_peak
import serial
from gpiozero import LightSensor, LED, Button

def_wait_time = 1
syringe_len_mm = 100
fill_speed = 100
limit_len_mm = 200

def stop_movement():
    ser.write(b"\x85\n")
    time.sleep(def_wait_time)

def empty():
    ser.write(b"$H\n")
    time.sleep(def_wait_time)

def set_soft_limit_mm(ser, val):
    ser.write(f"$130={val}\n".encode('utf-8'))
    time.sleep(def_wait_time)

def move_range(ser, range_mm, feed_rate):
    # $J=X10.0 Y-1.5 F100
    ser.write(f"$J=X{range_mm} F{feed_rate}\n".encode('utf-8'))
    time.sleep(def_wait_time) 

def fill():
    move_range(ser, syringe_len_mm, fill_speed)

def ml_to_mm(volume, cal_factor):
    """
    volume: in ml
    cal_factor: in mm/ml
    """
    return volume * cal_factor
    
def move_z(ser, val):
    ser.write(f"g0x{val}\n".encode('utf-8'))
    time.sleep(def_wait_time)
    
def print_answer(ser):
    ans = b''
    while ans == b'':
        ans = ser.readline()
    line = ans.decode('utf-8').rstrip()
    print(line)
    if line[:5] == 'error' or line[:5]=='ALARM':
        print('Error, stopping program.')
        exit


if __name__ == '__main__':
    # Raspberry pi Setup
    bottom_limit_switch = Button(3)
    bottom_limit_switch.when_pressed = stop_movement

    # Arduino Setup
    ser = serial.Serial('/dev/ttyACM0', 115200)
    time.sleep(2)
    ser.reset_input_buffer()

    # Unlock
    ser.write(b"$H\n")
    time.sleep(def_wait_time)
    print_answer(ser)

    # Set absolute position mode
    ser.write(b"g91\n")
    time.sleep(def_wait_time)
    print_answer(ser)
    
    # Set soft limit
    set_soft_limit_mm(ser, limit_len_mm)
    print_answer(ser)
 
    # Move on a range
    # # fill()
    move_range(ser, 10, 100)
    print_answer(ser)

    # stop_movement()
    # # Move
    # # move_z(ser, 3)

    print('DONE')
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            if line[:5] == 'error' or line[:5]=='ALARM':
                print('Error, stopping program.')
                exit
             

    
        
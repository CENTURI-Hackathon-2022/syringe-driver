# import libraries
import RPi.GPIO as GPIO
import time
 
# clean and define pins
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# PIN = number on board
coil_A_1_pin = 7  #pi:4  # pink wire
coil_A_2_pin = 11 #pi:17 # orange wire
coil_B_1_pin = 16 #pi:23 # blue wire
coil_B_2_pin = 18 #pi:24 # yellow wire

# define them as outputs
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
# define steps
StepCount = 8 #number of combinations, adjust if different
Seq = [[] for _ in range(0, StepCount)]
Seq[0] = [1,0,0,0]
Seq[1] = [1,1,0,0]
Seq[2] = [0,1,0,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,0,1,0]
Seq[5] = [0,0,1,1]
Seq[6] = [0,0,0,1]
Seq[7] = [1,0,0,1]

# apply 1 step to motor
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

# loop through steps number of steps, going forward
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            print(i, j, Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

# same but backwards
def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

# ask for user how fast and how much they want to move in both directions
if __name__ == '__main__':
    while True:
        delay = input("Time Delay (ms)?") #1ms
        steps = input("How many steps forward? ")#512 for 360°
        forward(int(delay) / 1000.0, int(steps))
        steps = input("How many steps backwards? ")
        backwards(int(delay) / 1000.0, int(steps))

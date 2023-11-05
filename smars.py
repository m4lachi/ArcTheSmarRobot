from machine import Pin, I2C, Timer
from time import sleep
from range_finder import RangeFinder

class SMARS():
    name = ""

    def __init__(self, i2c, name=None, in1=None, in2=None, in3=None, in4=None):
        if in1 is None or in2 is None or in3 is None or in4 is None:
            in1 = 6  # Motor A Direction Input 1
            in2 = 7  # Motor A Speed Input 2
            in3 = 8  # Motor B Direction Input 3
            in4 = 9  # Motor B Speed Input 4

        # Set the motor inputs on the L293D Motor Driver board
        self.motor_A_forward = Pin(in1, Pin.OUT)
        self.motor_A_reverse = Pin(in2, Pin.OUT)
        self.motor_B_forward = Pin(in3, Pin.OUT)
        self.motor_B_reverse = Pin(in4, Pin.OUT)

        if not name:
            self.name = "Arc"
        else:
            self.name = name

        self.i2c = i2c
        # Define a range finder object here
        self.range_finder = RangeFinder(trigger_pin=12, echo_pin=13)

    def forward(self):
        # Make the robot go forward for half a second
        self.motor_A_forward.high()
        self.motor_A_reverse.low()
        self.motor_B_forward.low()
        self.motor_B_reverse.high()
        sleep(10)
        self.stop()

    def backward(self):
        # Make the robot go backward for half a second
        self.motor_A_forward.low()
        self.motor_A_reverse.high()
        self.motor_B_forward.high()
        self.motor_B_reverse.low()
        sleep(0.5)
        self.stop()

    def turnleft(self):
        # Make the robot turn left for half a second
        self.motor_A_forward.low()
        self.motor_A_reverse.high()
        self.motor_B_forward.low()
        self.motor_B_reverse.high()
        sleep(0.5)
        self.stop()

    def turnright(self):
        # Make the robot turn right for half a second
        self.motor_A_forward.high()
        self.motor_A_reverse.low()
        self.motor_B_forward.high()
        self.motor_B_reverse.low()
        sleep(0.5)
        self.stop()

    def stop(self):
        self.motor_A_forward.low()
        self.motor_A_reverse.low()
        self.motor_B_forward.low
        self.motor_B_reverse.low()


i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
Arc = SMARS(i2c=i2c)

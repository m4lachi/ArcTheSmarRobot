from machine import Pin, PWM, I2C
from smars import SMARS
from time import sleep

# I2C
sda = Pin(8)
scl = Pin(9)
id = 1

# create the i2c object
i2c = I2C(id=id, sda=sda, scl=scl) 

Arc = SMARS(i2c=i2c)

def avoid():
    while True:
        print("I'm working")
        if Arc.distance >= 5:
            Arc.forward()
            print('forward',Arc.distance)
        else:
            Arc.backward()
            Arc.turnright()
            print('backward',Arc.distance)

def motor_test():
    while True:
        print("Testing left")
        Arc.turnleft()
        sleep(0.25)
        print("Testing right")
        Arc.turnright()
        sleep(0.25)
        print("Testing forward")
        Arc.forward()
        sleep(0.25)
        print("Testing backward")
        Arc.backward()
        sleep(0.25)

def motor_stop():
    Arc.stop()

from machine import Pin
from time import sleep_us


class RangeFinder:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
        
    def ping(self):
        self.__trigger_pin.low()
        sleep_us(2)

        self.__trigger_pin.high()
        sleep_us(5)
        self.__trigger_pin.low()
        signalon = 0
        signaloff = 0
        while self.__echo_pin.value() == 0:
            signaloff = ticks_us()
        while self.__echo_pin.value() == 1:
            signalon = ticks_us()
        elapsed_micros = signalon - signaloff
        self.duration = elapsed_micros
        self.distance = (elapsed_micros * 0.343) / 2
        return self.distance
        
    t = Range_Finder(echo_pin=12, trigger_pin=13)
while True:
    print("The distance is: ", t.ping())

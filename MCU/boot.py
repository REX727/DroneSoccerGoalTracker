# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from machine import Pin
from time import sleep

buzzer = Pin(10, Pin.OUT)

def BuzzerOn():
    buzzer.on()
    sleep(0.05)
    buzzer.off()
    sleep(0.05)


BuzzerOn()


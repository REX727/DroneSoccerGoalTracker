# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from machine import Pin, Timer
import tm1637

import time
import os

tm = tm1637.TM1637(clk=Pin(1), dio=Pin(2))

tm.write([0, 0, 0, 0])

buzzer = Pin(10, Pin.OUT)

goal_data = [4,3,2,4,5,3]

for i in range(5):
    buzzer.on()
    time.sleep_ms(50)
    buzzer.off()
    time.sleep_ms(25)
    buzzer.on()
    time.sleep_ms(50)
    buzzer.off()
    tm.show(str(5-i))
    time.sleep(1)
    
tm.show("----")
time.sleep_ms(50)
tm.write([0, 0, 0, 0])
time.sleep_ms(50)
tm.show("----")
time.sleep_ms(50)
tm.write([0, 0, 0, 0])

for lap in range(len(goal_data)):
    buzzer.on()
    time.sleep_ms(50)
    buzzer.off()
    tm.show(str(lap+1))
    time.sleep(goal_data[lap])


tm.write([0, 0, 0, 0])
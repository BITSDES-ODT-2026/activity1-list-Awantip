#indicator with list and for loop
from machine import Pin
import time

ledb= Pin(12, Pin.OUT)
ledy= Pin(13, Pin.OUT)
ledg= Pin(4, Pin.OUT)
ledr= Pin(5, Pin.OUT)

val= [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

for i in val:
    ledb.value(i[0])
    ledy.value(i[1])
    ledg.value(i[2])
    ledr.value(i[3])
    time.sleep(.5)

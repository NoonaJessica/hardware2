import ssd1306
import fifo
import time
from machine import Pin


rb = fifo.Fifo(50)
print('I am main.py')

if rb.empty():
    print('Fifo is empty')

led = Pin("LED", Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)


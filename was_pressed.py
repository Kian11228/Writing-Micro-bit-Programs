#was_pressed.py

from microbit import *

while True:
    sleep(5000)
    if button_a.was_pressed():
        display.show(Image.YES)
    else:
        display.show(Image.NO)

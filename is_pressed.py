#is_pressed.py

from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.YES)
    else:
        display.show(Image.NO)

#ternary.py

from microbit import *
    
def add_one(value):
    value = value + 1
    return value
    
while True:
    computation = add_one(5 if button_a.is_pressed() else 10)
    display.scroll(computation)

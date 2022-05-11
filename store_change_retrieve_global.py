#store_change_retrieve_global.py

from microbit import *

k = 5    

def add_k(value):
    global k
    k += 1
    value = value + k
    return value

display.scroll(add_k(3))
display.scroll(add_k(3))

#more_decisions.py

from microbit import *

a = 89
b = 42
if a > b:
    display.scroll("a is greater than b")
elif a < b:
    display.scroll("b is greater than a")
else:
    display.scroll("a is equal to b")

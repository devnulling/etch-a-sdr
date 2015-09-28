#!/usr/bin/python

from pymouse import PyMouse
from pykeyboard import PyKeyboard

from time import sleep

m = PyMouse()
k = PyKeyboard()

xd, yd = m.screen_size()

k.tap_key(k.function_keys[11]) 

print xd
print yd
sleep(1)
m.click(1500,1080,1)

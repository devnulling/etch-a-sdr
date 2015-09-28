#!/usr/bin/python

from pymouse import PyMouse
from time import sleep

sleep(10)

m = PyMouse()

xd, yd = m.screen_size()

print xd
print yd
sleep(10)
m.click(5,5,1)
sleep(1)
m.click(30, 75, 1)
sleep(1)
m.click(285, 75, 1)
sleep(1)
m.click(375, 75, 1)

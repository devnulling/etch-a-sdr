import serial
import requests
from time import sleep
import redis
import os

sleep(15)

ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port
r = redis.StrictRedis(host='localhost', port=6379, db=0)

r0 = "R0"
l0 = "L0"

r1 = "R1"
r2 = "R2"
r3 = "R3"

l1 = "L1"
l2 = "L2"
l3 = "L3"

l_up = "LU"
l_down = "LD"

r_up = "RU"
r_down = "RD"

while True:
    newline = ser.readline()
    newline = newline.rstrip()
    
    key = newline[:2]
    print key
    
    if key == l_up:
        print 'left up'
	r.publish('etch', 'u')
        
    elif key == l_down:
        print 'left down'
	r.publish('etch', 'd')
  
    elif key == r_up:
        print 'right up'
        r.publish('etch', 'l')
    
    elif key == r_down:
        print 'right down'
	r.publish('etch', 'r')

    elif key == l1:
        print 'left up'
	r.publish('etch', 'U')
        
    elif key == l2:
        print 'left down'
	r.publish('etch', 'D')
  
    elif key == r1:
        print 'right up'
        r.publish('etch', 'L')
    
    elif key == r2:
        print 'right down'
	r.publish('etch', 'R')
        
    elif key == r3:
        r.publish('etch', 'a')
        
    elif key == l3:
	r.publish('etch', 'b')
        
    elif key == l0:
        cmd = 'echo "etch" > /home/odroid/startup'
	os.system(cmd)
	sleep(1)
        
    elif key == r0:
        cmd = 'echo "gqrx" > /home/odroid/startup'
        os.system(cmd)
        sleep(1)
        
    else:
        print 'fail'
        print key
    sleep(.1) # Delay for one tenth of a second
    
    


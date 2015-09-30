import serial
import requests
from time import sleep
import redis
import os
import subprocess
import time

sleep(15)

ser = serial.Serial('/dev/ttyACM0', 115200)
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

mp = "MP"

milli_time = lambda: int(round(time.time() * 1000))
last_clear = milli_time()
current_time = milli_time()

class L(list):
    def append(self, item):
        list.append(self, int(item))
        if len(self) > 5: self[:1]=[]

def test(list):
    global last_clear
    v = [list[i+1]-list[i] for i in range(len(list)-1)]
    for item in v:
        if item > 10000:
            print "shake shake shake"
            current_time = milli_time()
            print current_time
            if last_clear + 15000 <= current_time:
                print "clearring"
                last_clear = milli_time()
                clearEtch()

def clearEtch():
    r = requests.get('http://localhost:7200/post?c=etch&m=c')

mpus = L()

while True:
    newline = ser.readline()
    newline = newline.rstrip()
    
    key = newline[:2]
    print key
    
    if key == mp:
        mpu = newline.replace(' ','').split(',')
	print "MPU: %s" % mpu[1]
	mpus.append(mpu[1])

        test(mpus)

    elif key == l_up:
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
       
    elif key == l3:
        subprocess.Popen("/home/odroid/reboot.sh", shell=False)
        sleep(1)
  
    elif key == r1:
        print 'right up'
        r.publish('etch', 'L')
	
    elif key == r2:
        print 'right down'
	r.publish('etch', 'R')
    elif key == r3:
        subprocess.Popen("/home/odroid/clear_etch.sh", shell=False)
        sleep(.1)

    elif key == l0:
        cmd = 'echo "etch" > /home/odroid/startup'
	os.system(cmd)
	sleep(.1)
    elif key == r0:
        cmd = 'echo "gqrx" > /home/odroid/startup'
        os.system(cmd)
        sleep(.1)
        
    else:
        print 'fail'
        print key
    sleep(.01) # delay
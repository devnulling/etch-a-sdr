import serial
import telnetlib
import subprocess
from time import sleep
import os

debugMode = 0
currentMode = "OFF"
stepLeft = 1000000
stepRight = 10000

freqSteps = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
deModes = ['OFF', 'RAW', 'AM', 'FM', 'WFM', 'WFM_ST', 'LSB', 'USB', 'CW', 'CWL', 'CWU']

class Gqrx():

    def _request(self, request):
        global debugMode
        if debugMode == 1:
            print request
        else:
            con = telnetlib.Telnet('127.0.0.1', 7356)
            con.write(('%s\n' % request).encode('ascii'))
            response = con.read_some().decode('ascii').strip()
            con.write('c\n'.encode('ascii'))
            return response

    def set_frequency(self, frequency):
        return self._request('F %s' % frequency)

    def get_frequency(self):
        return self._request('f')

    def set_mode(self, mode):
        return self._request('M %s' % mode)

    def get_mode(self):
        return self._request('m')

    def get_level(self):
        return self._request('l')
    
    
def getlevel():
    gqrx = Gqrx()
    level = gqrx.get_level()
    print level
    
def switchmode():
    global currentMode
    global deModes
    
    curModePos = deModes.index(currentMode)
    newModePos = int(curModePos) + 1
    
    if newModePos >= len(deModes):
        newModePos = 0
    
    currentMode = deModes[newModePos]
    gqrx = Gqrx()
    result = gqrx.set_mode(currentMode)
    print result
    print currentMode
    
    
    
def incstep(side):
    global stepLeft
    global stepRight
    global freqSteps
    
    if side == "left":
        currentStep = stepLeft
        stepPos = freqSteps.index(currentStep)
        newPos = int(stepPos) + 1
        if newPos >= len(freqSteps):
            newPos = 0
        stepLeft = freqSteps[newPos]
    elif side == "right":
        currentStep = stepRight
        stepPos = freqSteps.index(currentStep)
        newPos = int(stepPos) + 1
        if newPos >= len(freqSteps):
            newPos = 0
        stepRight = freqSteps[newPos]
    

def decstep(side):
    global stepLeft
    global stepRight
    global freqSteps
    
    if side == "left":
        currentStep = stepLeft
        stepPos = freqSteps.index(currentStep)
        newPos = int(stepPos) - 1
        if newPos == -1:
            newPos = len(freqSteps)-1
        stepLeft = freqSteps[newPos]
    elif side == "right":
        currentStep = stepRight
        stepPos = freqSteps.index(currentStep)
        newPos = int(stepPos) - 1
        if newPos == -1:
            newPos = len(freqSteps)-1
        stepRight = freqSteps[newPos]
  
    
def incfreq(side):
    global stepLeft
    global stepRight
    currentStep = 0
    left = "left"
    right = "right"
    
    if side == left:
        currentStep = stepLeft
    elif side == right:
        currentStep = stepRight
    else:
        currentStep = 0
        
    print 'running'
    if debugMode == 1:
        freq = 1
    else:
        gqrx = Gqrx()
        freq = gqrx.get_frequency()
        print freq
        setfreq = int(freq) + currentStep
        set = gqrx.set_frequency(setfreq)
        nf = gqrx.get_frequency()
        print nf

def decfreq(side):
    global stepLeft
    global stepRight
    currentStep = 0
    left = "left"
    right = "right"
    
    if side == left:
        currentStep = stepLeft
    elif side == right:
        currentStep = stepRight
    else:
        currentStep = 0
        
    print 'running dec freq'
    if debugMode == 1:
        freq = 1
    else:
        gqrx = Gqrx()
        freq = gqrx.get_frequency()
        print freq
        setfreq = int(freq)-currentStep
        set = gqrx.set_frequency(setfreq)
        nf = gqrx.get_frequency()
        print nf
    

    
    
    
    
    
    


ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port

r0 = "R0"
l0 = "L0"

r1 = "R1"
r2 = "R2"
r3 = "R3"

l1 = "L1"
l2 = "L2"

l_up = "LU"
l_down = "LD"

r_up = "RU"
r_down = "RD"

while True:
    newline = ser.readline() # Read the newest output from the Arduino
    newline = newline.rstrip()
    
    key = newline[:2]
    print key
    
    if key == r1:
        print 'r1 button'
        print stepRight
        print 'increasing stepRight'
        incstep("right")
        print 'increased stepRight'
        print stepRight
        
    elif key == r2:
        print 'r2 button'
        print stepRight
        print 'decreasing stepRight'
        decstep("right")
        print 'decreased stepRight'
        print stepRight
    
    elif key == r3:
	if debugMode == 1:
		subprocess.Popen("/home/odroid/start.py", shell=False)
		sleep(1)
	        debugMode = 0
		sleep(1)
	else:
	        print 'r3 button'
	        print currentMode
	        print 'changing mode'
	        switchmode()
	        print 'done'
	        print currentMode
  
    elif key == l1:
        print 'l1 button'
        print stepLeft
        print 'increasing stepLeft'
        incstep("left")
        print 'increased stepLeft'
        print stepLeft
        
    elif key == l2:
        print 'l2 button'
        print stepLeft
        print 'decreasing stepLeft'
        decstep("left")
        print 'decreased stepLeft'
        print stepLeft
        
        
    elif key == l_up:
        print 'left up'
        knobval = newline[2:]
        print knobval
        print 'increasing freq'
        incfreq("left")
        print 'inc done'
        
    elif key == l_down:
        print 'left down'
        knobval = newline[2:]
        print knobval
        print 'decreasing freq'
        decfreq("left")
        print 'dec done'
  
    elif key == r_up:
        print 'right up'
        knobval = newline[2:]
        print knobval
        print 'increasing freq'
        incfreq("right")
        print 'inc done'
    
    elif key == r_down:
        print 'right down'
        knobval = newline[2:]
        print knobval
        print 'decreasing freq'
        decfreq("right")
        print 'dec done'
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
    
    

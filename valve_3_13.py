import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13,GPIO.HIGH)
t_end = time.time() + 60 * 19
while time.time() < t_end:
        # do whatever you d
        #print str(t_end-time.time())
        with open('/home/pi/python/valve_3_13.log', 'w') as file:
                file.write(str(t_end-time.time()))
GPIO.output(13,GPIO.LOW)
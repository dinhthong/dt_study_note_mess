import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
count=0
while True:
    inputValue=GPIO.input(24)
    if (inputValue==True):
        count=count+1
    print("Nut duoc nhan"+str(count)+"lan.")
    time.sleep(.01)

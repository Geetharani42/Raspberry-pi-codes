import RPi.GPIO as GPIO
import time

ir=2
#pir=3
ma=26
mb=19

GPIO.setmode(GPIO.BCM)
GPIO.setup(ir,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(pir,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(ma,GPIO.OUT)
GPIO.setup(mb,GPIO.OUT)

GPIO.output(ma,GPIO.LOW)
GPIO.output(mb,GPIO.LOW)

while True:
    if GPIO.input(ir):
        GPIO.output(ma,GPIO.HIGH)
        GPIO.output(mb,GPIO.LOW)
    else:
        GPIO.output(ma,GPIO.LOW)
        GPIO.output(mb,GPIO.LOW)

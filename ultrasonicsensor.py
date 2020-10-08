import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

trig=23
echo=24

print("Distance measurement in progress")

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

while True:
    GPIO.output(trig,False)
    print("Waiting for sensor to settle")
    time.sleep(2)
    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)
    while GPIO.input(echo) == 0:
       pulse_start=time.time()


    while GPIO.input(echo)==1:
       pulse_end=time.time()


    pulse_duration =pulse_end - pulse_start

    distance=pulse_duration*17150
    distance=round(distance,2)

    if distance>2 and distance<400:
       print("Distance:",distance-0.5,"cm")
    else:
       print("Out of range")

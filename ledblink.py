import RPi.GPIO as IO
import time

led=23
button=25

IO.setmode(IO.BCM)
IO.setup(led,IO.OUT)
IO.setup(button,IO.IN,pull_up_down=IO.PUD_UP)

IO.output(led,IO.LOW)

while True:
   if IO.input(button): 
    IO.output(led,IO.LOW)
    #time.sleep(0.5)
   else:
    IO.output(led,IO.HIGH)
    #time.sleep(0.5)

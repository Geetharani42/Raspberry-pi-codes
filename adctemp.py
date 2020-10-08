import spidev
from numpy import interp
from time import sleep
import RPi.GPIO as GPIO

spi= spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

#led=20

GPIO.setmode(GPIO.BCM)
#GPIO.setup(led,GPIO.OUT)

#pwm=GPIO.PWM(led,100)
#pwm.start(0)

def analogInput(channel):
    
    adc=spi.xfer2([1,(8+channel)<<4,0])
    data=((adc[1]&3)<<8)+adc[2]
    return data
def Volts(data):
    volts=(data*3.3)/float(1023)
    volts=round(volts,2)
    return volts
def Temp(data):
    temp=((data*330)/float(1023))-50
    temp=round(temp,2)
    return temp
while True:
    temp_output=analogInput(0)
    temp_volts=Volts(temp_output)
    temp=Temp(temp_output)
    print("Temp: {} ({}v) {} deg c".format(temp_output,temp_volts,temp))
    sleep(5)

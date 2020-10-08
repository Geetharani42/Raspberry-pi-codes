import serial
import os,time
import RPi.GPIO as GPIO
but=37

port=serial.Serial("/dev/ttyAMA0",baudrate=9600,timeout=1)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(but,GPIO.IN,pull_up_down=GPIO.PUD_UP)


port.write(b'AT\r')
rcv=port.read(10)
print(rcv)
time.sleep(1)
port.write(b"AT+CMGF=1\r")
rcv=port.read(10)
print(rcv)
time.sleep(1)
print("Text mode enabled...")
time.sleep(3)
port.write(b'AT+CMGS="7387389299"\r')
rcv=port.read(10)
print(rcv)
time.sleep(1)
msg="text message fromSIM800L"
time.sleep(3)
port.write(str.encode(msg+chr(26)))
time.sleep(3)
#for i in range(10):
#port.write(b"AT+CMGD=1\r")
#rcv=port.read(10)
#print(rcv)
#time.sleep(1)
port.write(b"AT+CMGR=1\r")
rcv=port.read(10)
print(rcv)
time.sleep(1)
#for i in range(26):
rcv=port.read(88)
print(rcv)

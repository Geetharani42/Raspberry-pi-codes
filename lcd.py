import RPi.GPIO as GPIO
import time

ir=2
LCD_RS=27
LCD_E=22
LCD_D4=6
LCD_D5=13
LCD_D6=19
LCD_D7=26

LCD_WIDTH=16
LCD_CHR= True
LCD_CMD= False

LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xc0

E_PULSE = 0.001
E_DELAY = 0.001

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LCD_E, GPIO.OUT)
    GPIO.setup(LCD_RS,GPIO.OUT)
    GPIO.setup(LCD_D4,GPIO.OUT)
    GPIO.setup(LCD_D5,GPIO.OUT)
    GPIO.setup(LCD_D6,GPIO.OUT)
    GPIO.setup(LCD_D7,GPIO.OUT)
    GPIO.setup(ir,GPIO.IN,pull_up_down=GPIO.PUD_UP)

    lcd_init()

    while True:
         if GPIO.input(ir):
             lcd_string("IR DEACTIVATED",LCD_LINE_1)
             time.sleep(0.5)
         else :
             lcd_byte(0x01,LCD_CMD)
             lcd_string("IR ACTIVATED",LCD_LINE_1)
             time.sleep(0.5)
def lcd_init():
    lcd_byte(0x33,LCD_CMD)
    lcd_byte(0x32,LCD_CMD)
    lcd_byte(0x06,LCD_CMD)
    lcd_byte(0x0c,LCD_CMD)
    lcd_byte(0x28,LCD_CMD)
    lcd_byte(0x01,LCD_CMD)
    time.sleep(E_DELAY)

def lcd_byte(bits,mode):
    GPIO.output(LCD_RS,mode)
    GPIO.output(LCD_D4,False)
    GPIO.output(LCD_D5,False)
    GPIO.output(LCD_D6,False)
    GPIO.output(LCD_D7,False)
    if bits&0x10==0x10:
        GPIO.output(LCD_D4,True)
    if bits&0x20==0x20:
        GPIO.output(LCD_D5,True)
    if bits&0x40==0x40:
        GPIO.output(LCD_D6,True)
    if bits&0x80==0x80:
        GPIO.output(LCD_D7,True)
    lcd_toggle_enable()

    GPIO.output(LCD_D4,False)
    GPIO.output(LCD_D5,False)
    GPIO.output(LCD_D6,False)
    GPIO.output(LCD_D7,False)
    if bits&0x01==0x01:
        GPIO.output(LCD_D4,True)
    if bits&0x02==0x02:
        GPIO.output(LCD_D5,True)
    if bits&0x04==0x04:
        GPIO.output(LCD_D6,True)
    if bits&0x08==0x08:
        GPIO.output(LCD_D7,True)

    lcd_toggle_enable()

def lcd_toggle_enable():
    time.sleep(E_DELAY)
    GPIO.output(LCD_E,True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E,False)
    time.sleep(E_DELAY)

def lcd_string(message,line):
    message=message.ljust(LCD_WIDTH," ")
    lcd_byte(line,LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
            lcd_byte(0x01,LCD_CMD)
            lcd_string("BYE",LCD_LINE_1)
            time.sleep(1)
            GPIO.cleanup()
         

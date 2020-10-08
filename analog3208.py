from mcp3208 import MCP3208

import time

adc=MCP3208()

while True:
    #for i in range(1):
         print('ADC[{}]:{:.2f}'.format(0,adc.read(0)))
         voltage = adc.read(0) * 3.3 / float(1024)
         temp = ((adc.read(0) * 330)/float(1023))-50
         print("Voltage=%f\ttemp=%f" % (voltage,temp))
         time.sleep(1)

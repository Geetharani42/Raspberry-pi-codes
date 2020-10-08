import time
import Adafruit_DHT


sensor_name=Adafruit_DHT.DHT11
sensor_pin=17
time.sleep(2)
while 1:
    humidity,temperature= Adafruit_DHT.read_retry(sensor_name,sensor_pin)
    print("temp={0:0.1f}*c humidity={1:0.1f}%".format(temperature,humidity))
    time.sleep(2)

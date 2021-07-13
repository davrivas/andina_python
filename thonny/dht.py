from dht import DHT11
from machine import Pin
import utime

sensorDHT = DHT11(Pin(15))

while True:
    utime.sleep(1)
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    print("T={:02d} °C, H={:02d}%".format(temp, hum))
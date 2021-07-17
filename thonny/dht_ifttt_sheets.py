import network, time, urequests
from dht import DHT11
from machine import Pin

def conectaWifi(red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff(time.time(), timeout) > 10):
                  return False
      return True

sensorDHT = DHT11(Pin(15))

if conectaWifi("Claro_61039A", "M5C9A3W7P3W8"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://maker.ifttt.com/trigger/sensor_dht/with/key/CS5bYnTkWNS01hQSP5rYU"
    
    while (True):        
        sensorDHT.measure()

        temp=sensorDHT.temperature()
        hum=sensorDHT.humidity()

        print ("T={:02d} ºC, H={:02d} %".format (temp,hum))

        endpoint = url + "?value1=" + str(temp) + "&value2=" + str(hum)
        respuesta = urequests.get(endpoint)
        print("Respuesta:", respuesta.text)
        print ("Status:", respuesta.status_code)
        respuesta.close()
        time.sleep(30)
else:
    print ("Imposible conectar")
    miRed.active (False)

print()

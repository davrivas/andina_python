import network
import umail
from machine import Pin
import utime

push = Pin(13, Pin.IN, Pin.PULL_DOWN)
uno = Pin(2, Pin.OUT)

def do_connect(SSID, PASSWORD):
    import network                            # importa el módulo network
    global sta_if
    sta_if = network.WLAN(network.STA_IF)     # instancia el objeto -sta_if- para controlar la interfaz STA
    if not sta_if.isconnected():              # si no existe conexión...
        sta_if.active(True)                       # activa el interfaz STA del ESP32
        sta_if.connect(SSID, PASSWORD)            # inicia la conexión con el AP
        print('Conectando a la red', SSID +"...")
        while not sta_if.isconnected():           # ...si no se ha establecido la conexión...
            pass                                  # ...repite el bucle...
    print('Configuración de red (IP/netmask/gw/DNS):', sta_if.ifconfig())

   
do_connect("FAMILIA PENA", "Hupe6493$")



    
while True:

    def send_mail():
        smtp = umail.SMTP('smtp.gmail.com', 465)
        smtp.login('cuentaesp32arduino@gmail.com', 'esp32arduino',ssl= True)
        smtp.to('hugo.alex30@gmail.com')
        smtp.write("From:ghgfgdfd")
        smtp.write("This is an example esp32 micropython")
        smtp.send()
        smtp.quit()
        
    estado = push.value()
    print(estado)
    utime.sleep(2)
    
    if estado == 1:
        send_mail()
        utime.sleep(5)
    else:
        uno.value(0) 

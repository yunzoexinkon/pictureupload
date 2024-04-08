import network
import led
def connect():
  wlan = network.WLAN(network.STA_IF)
  wlan.active(False)
  wlan.active(True)
  
  if not wlan.isconnected():
      for i in range(4) :
          led.LEDconnect()
      print('connecting to network...')
      #wlan.connect('B510_Wifi', 'mjchen0821')
      wlan.connect('墜神   漆夜', '00000000')
      #wlan.ifconfig(('192.168.0.125', '255.255.255.0', '192.168.0.1', '192.168.0.1'))
      while not wlan.isconnected():
          pass
  if wlan.isconnected():
      led.LEDready()
  if not wlan.isconnected():
      led.LEDfail()
      
  print('network config: ', wlan.ifconfig())
#connect()
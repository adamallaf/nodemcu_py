import network
import time
from machine import Pin
#from m_wifi import get_wifi_creds


class MyWLAN:
    def __init__(self):
        self.__wlan = network.WLAN(network.STA_IF)
        self.__wlan.active(True)
        self.__builtin_led = Pin(2, Pin.OUT)

    def connect(self, ssid=None, key=""):
        if ssid:
            self.__wlan.connect(ssid, key)
        else:
            pass
            #self.__wlan.connect(*get_wifi_creds())
        self.__blink_led(10, 40, 60)

    def is_connected(self):
        return self.__wlan.isconnected()

    def disconnect(self):
        self.__wlan.disconnect()
        self.__blink_led(20, 20, 40)

    def __blink_led(self, count, l, h):
        for i in range(count):
            self.__builtin_led.off()
            time.sleep_ms(l)
            self.__builtin_led.on()
            time.sleep_ms(h)

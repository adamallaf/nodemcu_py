import network
from machine import Pin
from m_wifi import get_wifi_creds


class MyWLAN:
    def __init__(self):
        self.__wlan = network.WLAN(network.STA_IF)
        self.__wlan.active(True)
        self.__builtin_led = Pin(2)

    def connect(self, ssid=None, key=""):
        if ssid:
            self.__wlan.connect(ssid, key=key)
        else:
            self.__wlan.connect(*get_wifi_creds())
        self.__builtin_led.off()

    def is_connected(self):
        return self.__wlan.isconnected()

    def disconnect(self):
        self.__wlan.disconnect()
        self.__builtin_led.on()

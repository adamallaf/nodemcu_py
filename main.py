import time
import ujson
from i2c import I2CBus
from server import HTTPServer
from tmp102 import TMP102
from wlan import MyWLAN


wlan = MyWLAN()
i2c = I2CBus()
tmp = TMP102(i2c)
http = HTTPServer()

__ts1970_2000 = 946684800


def temperature():
    t = tmp.read_temperature()
    return ujson.dumps({"t": t, "ts": time.mktime() + __ts1970_2000})


while True:
    wlan.connect()
    while wlan.is_connected():
        http.handle(temperature)
    time.sleep(10)

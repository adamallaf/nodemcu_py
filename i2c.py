from machine import Pin, I2C


class I2CBus:
    def __init__(self, freq=100000):
        self.__i2c = I2C(scl=Pin(5), sda=Pin(4), freq=freq)

    def write(self, address, data):
        _d = "".join([chr(_byte) for _byte in data])
        self.__i2c.writeto(address, _d)

    def read(self, address, count):
        return self.__i2c.readfrom(address, count)

    def scan(self):
        return self.__i2c.scan()

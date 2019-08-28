class TMP102:
    def __init__(self, i2c_bus, address=0x48):
        self.__i2c = i2c_bus
        self.__address = address
        self.__i2c.write(self.__address, [1, 0x60, 0xa0])  # set 12bit resolution

    def read_temperature(self):
        data = self.__i2c.read(self.__address, 2)
        temp = data[0]
        i = 1
        mask = 4
        fraction = data[1] >> 4
        while i < 5:
            temp += ((fraction & mask) >> (4 - i)) * 2 ** -i
            mask = mask >> 1
            i += 1
        return temp

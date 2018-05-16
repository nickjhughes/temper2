import sys
import time
import hid


class Temper2:

    vendor_id = 0x413D
    product_id = 0x2107

    def __init__(self):
        self.h = hid.device(self.vendor_id, self.product_id)
        self.h.open(self.vendor_id, self.product_id)

    def get_name(self):
        self.h.write([0x01, 0x86, 0xff, 0x01, 0x00, 0x00, 0x00, 0x00])
        resp1 = self.h.read(8)
        resp2 = self.h.read(8)
        resp1_chars = ''.join([chr(r) for r in resp1])
        resp2_chars = ''.join([chr(r) for r in resp2])
        return resp1_chars + resp2_chars

    def get_temp(self):
        self.h.write([0x01, 0x80, 0x33, 0x01, 0x00, 0x00, 0x00, 0x00])
        resp1 = self.h.read(8)
        # FIXME: This second read will hang if there's no external
        #        temperature probe connected
        resp2 = self.h.read(8)
        int_temp = ((resp1[2] << 8) + resp1[3]) / 100
        ext_temp = ((resp2[2] << 8) + resp2[3]) / 100
        return int_temp, ext_temp


if __name__ == '__main__':
    t = Temper2()
    name = t.get_name()
    print(name)
    while True:
        int_temp, ext_temp = t.get_temp()
        print(int_temp, ext_temp)
        time.sleep(1)

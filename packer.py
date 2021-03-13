import struct, io,  fcntl

class formatting:
    def __init__(self, byte):
       self._io = byte 

    def _fmt_h(self):
        fmt = "h" + "x"* (len(self._io.read())- 2)
        byte.seek(0)
        return struct.unpack(fmt, byte.read())

    def _fmt_l(self):
        self._io.seek(0) 
        fmt ="l" + "x"* (len(self._io.read()) - 8)
        self._io.seek(0) 
        return struct.unpack(fmt, self._io.read())

    def _fmt_x(self):
        self._io.seek(0) 
        fmt = "x"* len(self._io.read())
        self._io.seek(0) 
        return struct.unpack(fmt, self._io.read())

def packer(fmt):
    fmt.split("h")

byte = struct.pack("lx", 1)
byte =io.BytesIO(byte)
fmt = formatting(byte)
print(fmt._fmt_x())

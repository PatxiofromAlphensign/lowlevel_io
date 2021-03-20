#!/usr/bin/python3 
import struct, io,  fcntl, tempfile, termios 

class formatting:
    def __init__(self, byte):
        self._io = byte 
    
    @classmethod
    def get_values_fmt(cls,fmt):
        ret = []
        for val in ("l", "h"):
            ret.append([1 for i in range(len(fmt.split(val)) - 1)])
        return ret[0] + ret[1]
    
    def _fmt_h(self):
        self.fmt =  fmt = "h" + "x"* (len(self._io.read())- 2)
        self._io.seek(0)
        struct.pack(fmt, *formatting.get_values_fmt(fmt))  # why the hell are we doing it?
        return struct.unpack(fmt, self._io.read()[:len(fmt) + 1]) # fail safe

    def _fmt_l(self):
        self._io.seek(0) 
        self.fmt = fmt ="l" + "x"* (len(self._io.read()) - 8)
        self._io.seek(0) 
        if self._io.read().__len__() < 8:
            self._io.write(struct.pack(fmt, 1))
        size = struct.calcsize(fmt) # fail safe
        self._io.seek(0) 
        return struct.unpack(fmt, self._io.read()[:size])

    def _fmt_x(self):
        self._io.seek(0) 
        fmt = self.fmt = "x"* len(self._io.read())
        self._io.seek(0) 
        return struct.unpack(fmt, self._io.read())

class DevCtl:
    def __init__(self, fd):
        self._fd = fd
        self.ids  =  self.nums()  

    def nums(self):
        i = 0
        ret = [2]
        while i < 1e6:
            try:
                fcnlt.ioctl(self._fd.fileno(), i, "test")
                ret.append(i)
            except:
                pass
            i+=1
        return ret

    def fcntl(self):
        self.fd = fd = tempfile.SpooledTemporaryFile()
        fd.write(self._fd.read())
        fd.seek(0)
        return fcntl.fcntl(fd, 1, fd.read())

    def flock(self):
        self.fcntl()
        fcntl.flock(self.fd, 1)

    def ioctl(self, choose_system_calls=None):
        self.flock()
        fcntl.ioctl(1, termios.TIOCGPGRP, self.fd.read(), choose_system_calls if choose_system_calls is not None else 1)

def packer(fmt):
    byte = struct.pack(fmt, *formatting.get_values_fmt(fmt))
    byte =io.BytesIO(byte)
    d = DevCtl(byte)
    d.ioctl(choose_system_calls = fcntl.LOCK_SH)

    fmt = formatting(byte)
    ret = []
    for f in ("l","h"):
        x, = getattr(fmt , "_fmt_"+f)()
        ret.append(x)
    return ret

if __name__ == "__main__":
    print(packer("lllllhhhh"))


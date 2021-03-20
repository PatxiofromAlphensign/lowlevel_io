import io, struct, fcntl
from packer import DevCtl, formatting
import socket

class IO:
    def __init__(self, buf):
        buf = io.BytesIO(buf)
        self._io = io.TextIOWrapper(buf)
        self.dev = DevCtl(buf)
        self.size = self._io.read().__len__()
        # self.__io.ioctl()

def main():
    buf =struct.pack("l", 1)
    _io = io.BytesIO(buf)
    fmt= formatting(_io)
    io = IO(buf)
    fcntl.ioctl(2,2,"")

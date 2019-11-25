import struct
from serial import Serial

def openSerial():
    s = Serial()
    s.port = 'COM6'
    s.baudrate = 115200
    s.timeout = 0.5
    s.dtr = 0
    s.open()
    state = s.isOpen()
    return s

from serial import Serial
s = Serial()
s.port = 'COM6'
s.baudrate = 115200
s.timeout = 0.5
s.dtr = 0
s.open()
state = s.isOpen()
print(state)
data = [300] ##WRITING
data.insert(0, 85)
data.insert(0, 22)
print(data)
s.write(data) ##start and data
data2 = [22, 34, 99]
s.write(data2) ##done condition
data2 = s.read() ##READING
print(type(data2))
print(int.from_bytes(data2, 'little')) ##convert from bytes (little endian)








import smbus
import time
bus = smbus.SMBus(1)
address = 0x68

def write(value):
	bus.write_byte_data(address, 0, value)
	return -1

def range(add):
	range1 = bus.read_byte_data(address, add)
	return range1

while True:
	print ((range(0x3B)<<8) + range(0x3C))
	print type(range(0x3B))
	time.sleep(1)

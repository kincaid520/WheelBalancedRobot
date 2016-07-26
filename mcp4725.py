import smbus
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ADDRESS1 = [0x62,4] # only work with rotation
ADDRESS2 = [0x63,14] # work with all functions

CMD_FAST = 0b00000000
CMD_DAC = 0b01000000
CMD_DACEEPROM = 0b01100000
CMD_RESET = 0b00000110


class MCP4725:
	bus = None
	address = None
	voltage = 0 # from 0 to 4095
	GPIOPIN = 0 # 4 or 14

	def __init__(self, addr = ADDRESS1, voltage = 0):
		self.bus = smbus.SMBus(1)
		self.address = addr[0]
		self.voltage = voltage
		self.GPIOPIN = addr[1]
		GPIO.setup(self.GPIOPIN, GPIO.OUT)
		GPIO.output(self.GPIOPIN, GPIO.LOW)

	def setVoltage(self, voltage):
		if voltage > 4095:
			voltage = 4095
			print "WARNING: voltage more than 4095"
		elif voltage < 0:
			voltage = 0
			print "WARNING: voltage less than 0"

		self.voltage = voltage

		return self.bus.write_i2c_block_data(self.address, CMD_FAST + (voltage >> 8), [voltage])

	def clockwise(self):
		GPIO.output(self.GPIOPIN, GPIO.LOW)

	def counterclockwise(self):
		GPIO.output(self.GPIOPIN, GPIO.HIGH)

if __name__ == "__main__":
	test1 = MCP4725(0x62)
	#test2 = MCP4725(0x63)
	test1.setVoltage(2048)
	#test2.setVoltage(4095)


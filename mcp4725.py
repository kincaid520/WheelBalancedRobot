import smbus
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ADDRESS1 = [0x62,4] # dac_left
ADDRESS2 = [0x63,14] # dac_right

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
                self.set_voltage(0)
                self.set_clockwise()

	def set_voltage(self, voltage):
		if voltage > 4095:
			voltage = 4095
			print "WARNING: voltage more than 4095"
                        print "Voltage has been setting to 4095"
		elif voltage < 0:
			voltage = 0
			print "WARNING: voltage less than 0"
                        print "Voltage has been setting to 0"

		self.voltage = voltage

		return self.bus.write_i2c_block_data(self.address, CMD_FAST + (voltage >> 8), [voltage])

	def set_clockwise(self):
		GPIO.output(self.GPIOPIN, GPIO.LOW)

	def set_counterclockwise(self):
		GPIO.output(self.GPIOPIN, GPIO.HIGH)

if __name__ == "__main__":
	dacLeft = MCP4725(ADDRESS1)
	dacRight = MCP4725(ADDRESS2)


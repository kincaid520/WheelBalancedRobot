import smbus
import math
from time import sleep

#bus = smbus.SMBus(1)

#motion gyro address_bit (read only)---------
ACCEL_XH	= 0X3B
ACCEL_XL	= 0X3C
ACCEL_YH	= 0X3D
ACCEL_YL	= 0X3E
ACCEL_ZH	= 0X3F
ACCEL_ZL	= 0X40
GYRO_XH		= 0X43
GYRO_XL		= 0X44
GYRO_YH		= 0X45
GYRO_YL		= 0X46
GYRO_ZH		= 0X47
GYRO_ZL		= 0X48
TEMP_H		= 0X41
TEMP_L		= 0X42

#Configure-------------------------
ACCEL_CONFIG	= 0x1C
ACCELSCALE_2G	= 0b00000000
ACCELDIVIDER_2G	= 16384.0
ACCELSCALE_4G	= 0b00001000
ACCELDIVIDER_4G	= 8192.0
ACCELSCALE_8G	= 0b00010000
ACCELDIVIDER_8G	= 4096.0
ACCELSCALE_16G	= 0b00011000
ACCELDIVIDER_16G= 2048.0

GYRO_CONFIG		= 0x1B
GYROSCALE_250	= 0b00000000
GYRODIVIDER_250	= 131.0
GYROSCALE_500	= 0b00001000
GYRODIVIDER_500	= 65.5
GYROSCALE_1000	= 0b00010000
GYRODIVIDER_1000= 32.8
GYROSCALE_2000	= 0b00011000
GYRODIVIDER_2000= 16.4

# ..---------------------------------
WHOAMI		= 0X75

#Parameter---------------------------------
ADDRESS		= 0x68
ACCELSCALE	= ACCELSCALE_2G
ACCELDIVIDER= ACCELDIVIDER_2G
GYROSCALE	= GYROSCALE_250
GYRODIVIDER = GYRODIVIDER_250

class MPU9250:
	address = None
	bus = smbus.SMBus(1)
	accel = [None, None, None]
	gyro = [None, None, None]
	accelscale = None
	acceldivider = None
	gyroscale = None
	gyrodivider = None

	def __init__(self, address = ADDRESS, accelscale = ACCELSCALE, acceldivider = ACCELDIVIDER, gyroscale = GYROSCALE, gyrodivider = GYRODIVIDER):
		self.address = address
		self.setAccelScale(accelscale)
		self.setGyroScale(gyroscale)
		self.accelscale = accelscale
		self.acceldivider = acceldivider
		self.gyroscale = gyroscale
		self.gyrodivider = gyrodivider

	def ReadReg(self, addr):
		return self.bus.read_byte_data(self.address, addr)

	def WriteReg(self, addr, data):
		return self.bus.write_byte_data(self.address, addr, data)

	def testConnection(self):
		if self.ReadReg(WHOAMI) == 113:
			return True
		else:
			return False

	def getTemp(self):
		temparature = self.ReadReg(TEMP_H)<<8
		temparature += self.ReadReg(TEMP_L)
		return temparature

	def setAccelScale(self, scale):
		return self.WriteReg(ACCEL_CONFIG, scale)

	def setGyroScale(self, scale):
		return self.WriteReg(GYRO_CONFIG, scale)

	def get_accel(self):
		AccelXH = self.ReadReg(ACCEL_XH)
		AccelXL = self.ReadReg(ACCEL_XL)
		AccelX = (AccelXH<<8) + AccelXL
		#if AccelXH>>7 == 1:
		#	AccelX = AccelX-65536.0

		AccelYH = self.ReadReg(ACCEL_YH)
		AccelYL = self.ReadReg(ACCEL_YL)
		AccelY = (AccelYH<<8) + AccelYL
		#if AccelYH>>7 == 1:
		#	AccelY = AccelY-65536.0

		AccelZH = self.ReadReg(ACCEL_ZH)
		AccelZL = self.ReadReg(ACCEL_ZL)
		AccelZ = (AccelZH<<8) + AccelZL
		#if AccelZH>>7 == 1:
		#	AccelZ = AccelZ-65536.0

		return AccelX, AccelY, AccelZ

	def get_gyro(self):
		GyroXH = self.ReadReg(GYRO_XH)
		GyroXL = self.ReadReg(GYRO_XL)
		GyroX = (GyroXH<<8) + GyroXL
		#if GyroXH>>7 ==1:
		#	GyroX = GyroX-65536.0

		GyroYH = self.ReadReg(GYRO_YH)
		GyroYL = self.ReadReg(GYRO_YL)
		GyroY = (GyroYH<<8) + GyroYL
		#if GyroYH>>7 ==1:
		#	GyroY = GyroY-65536.0

		GyroZH = self.ReadReg(GYRO_ZH)
		GyroZL = self.ReadReg(GYRO_ZL)
		GyroZ = (GyroZH<<8) + GyroZL
		#if GyroZH>>7 ==1:
		#	GyroZ = GyroZ-65536.0

		return GyroX, GyroY, GyroZ

if __name__ == "__main__":
	mpu9250 = MPU9250()
	print "Connection: ", mpu9250.testConnection()

	times = 0.0
	while True:
		mpu9250.accel = mpu9250.get_accel()

		print mpu9250.get_angle()[1]; print mpu9250.get_accel()[2]

		sleep(0.05)
